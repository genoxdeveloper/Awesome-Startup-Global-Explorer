from flask import Flask, render_template, request, jsonify
from data_mock import generate_mock_data
from datetime import datetime, timedelta

import os
import threading
from models import db, GlobalOpportunity, init_db
from startup_crawler_global import run_crawler_and_save

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_PATH = os.path.join(BASE_DIR, 'instance')
if not os.path.exists(INSTANCE_PATH):
    os.makedirs(INSTANCE_PATH)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(INSTANCE_PATH, "global_data.db")}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)

# ---------------------------------------------------------------------------
# Auto-cleanup: delete records older than 3 months
# ---------------------------------------------------------------------------
def cleanup_old_records():
    """Remove records with created_at older than 3 months."""
    with app.app_context():
        cutoff = datetime.utcnow() - timedelta(days=90)
        old_count = GlobalOpportunity.query.filter(
            GlobalOpportunity.created_at is not None,
            GlobalOpportunity.created_at < cutoff
        ).count()
        if old_count > 0:
            GlobalOpportunity.query.filter(
                GlobalOpportunity.created_at is not None,
                GlobalOpportunity.created_at < cutoff
            ).delete(synchronize_session=False)
            db.session.commit()
            print(f"🗑️  Cleaned up {old_count} records older than 3 months (before {cutoff.strftime('%Y-%m-%d')})")
        else:
            print("✅ No records older than 3 months. Nothing to clean up.")

# ---------------------------------------------------------------------------
# Initial seed: only runs if DB is completely empty (first deploy)
# After that, data accumulates via crawler without any cap
# ---------------------------------------------------------------------------
def sync_mock_to_db():
    with app.app_context():
        # Step 1: Clean up old records (older than 3 months)
        cleanup_old_records()

        # Step 2: Seed ONLY if the DB is completely empty (first-time init)
        current_count = GlobalOpportunity.query.count()
        if current_count == 0:
            print("Database is empty. Seeding with initial dataset...")
            records = generate_mock_data()
            for r in records:
                opp = GlobalOpportunity(
                    title=r.get('title'),
                    description=r.get('description'),
                    country=r.get('country'),
                    category=r.get('category'),
                    industries=",".join(r.get('industries', [])) if isinstance(r.get('industries'), list) else r.get('industries', ''),
                    status=r.get('status'),
                    funding=r.get('funding'),
                    equity=r.get('equity'),
                    provider=r.get('provider'),
                    fit_score=r.get('fit_score', 50),
                    created_at=datetime.utcnow()
                )
                db.session.add(opp)
            db.session.commit()
            print(f"✅ Initial seed complete: {len(records)} records inserted (NO hardcoded limit)")
        else:
            print(f"📊 Database has {current_count} records. No limit — data accumulates indefinitely.")

sync_mock_to_db()

# ---------------------------------------------------------------------------
# Auto-crawl scheduler: runs every 6 hours in background
# ---------------------------------------------------------------------------
AUTO_CRAWL_INTERVAL = 6 * 60 * 60  # 6 hours in seconds

def auto_crawl_scheduler():
    """Background scheduler that automatically runs the global crawler every 6 hours."""
    import time as _time
    while True:
        _time.sleep(AUTO_CRAWL_INTERVAL)
        print(f"\n🕐 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Auto-crawl starting (Global)...")
        try:
            run_crawler_and_save()
            print("✅ Auto-crawl (Global) complete.")
        except Exception as e:
            print(f"❌ Auto-crawl (Global) error: {e}")

_scheduler_thread = threading.Thread(target=auto_crawl_scheduler, daemon=True)
_scheduler_thread.start()
print(f"🕐 Auto-crawl scheduler started (every {AUTO_CRAWL_INTERVAL // 3600} hours)")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/refresh', methods=['POST'])
def api_refresh():
    # Run the crawler in a background thread to prevent request timeout
    thread = threading.Thread(target=run_crawler_and_save)
    thread.start()
    return jsonify({"status": "success", "message": "Background recrawl initiated. New data will be APPENDED (no limit)."})

@app.route('/api/data')
def api_data():
    country = request.args.get('country', '')
    industry = request.args.get('industry', '')
    category = request.args.get('category', '')
    search = request.args.get('search', '').lower()

    query = GlobalOpportunity.query

    if country and country != 'Global':
        query = query.filter(db.or_(
            GlobalOpportunity.country == country,
            GlobalOpportunity.country == 'Global'
        ))
    if category and category != 'All':
        query = query.filter(GlobalOpportunity.category == category)
    if industry and industry != 'All':
        query = query.filter(db.or_(
            GlobalOpportunity.industries.ilike("%All%"),
            GlobalOpportunity.industries.ilike(f"%{industry}%")
        ))
    if search:
        query = query.filter(db.or_(
            GlobalOpportunity.title.ilike(f"%{search}%"),
            GlobalOpportunity.description.ilike(f"%{search}%"),
            GlobalOpportunity.provider.ilike(f"%{search}%")
        ))

    # NO hardcoded limit — return ALL matching results
    results = query.order_by(GlobalOpportunity.fit_score.desc()).all()
    filtered = []
    for r in results:
        filtered.append({
            "title": r.title, "description": r.description,
            "country": r.country, "category": r.category,
            "industries": r.industries.split(',') if r.industries else [],
            "status": r.status,
            "funding": r.funding, "equity": r.equity,
            "provider": r.provider, "fit_score": r.fit_score,
            "created_at": r.created_at.strftime('%Y-%m-%d') if r.created_at else None
        })

    # Stats calculation from ALL records (no limit)
    stats = {'countries': {}, 'categories': {}, 'industries': {}}
    all_res = GlobalOpportunity.query.with_entities(
        GlobalOpportunity.country, GlobalOpportunity.category, GlobalOpportunity.industries
    ).all()
    
    total_records = len(all_res)
    for c_val, cat_val, ind_str in all_res:
        stats['countries'][c_val] = stats['countries'].get(c_val, 0) + 1
        stats['categories'][cat_val] = stats['categories'].get(cat_val, 0) + 1
        inds = ind_str.split(',') if ind_str else []
        for ind in inds:
            stats['industries'][ind] = stats['industries'].get(ind, 0) + 1

    return jsonify({
        'total': len(filtered),
        'total_in_db': total_records,
        'stats': stats,
        'records': filtered,
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
