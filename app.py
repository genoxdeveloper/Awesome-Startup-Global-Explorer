from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import math
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
def _sync_real_data_blocking():
    with app.app_context():
        # Step 1: Clean up old records (older than 3 months)
        cleanup_old_records()

        # Step 2: Seed ONLY if the DB is completely empty (first-time init)
        current_count = GlobalOpportunity.query.count()
        if current_count == 0:
            print("Database is empty. Seeding with 100% real global dataset in background...")
            run_crawler_and_save()
            print("✅ Initial real data seed complete.")
        else:
            print(f"📊 Database has {current_count} records. No limit — data accumulates indefinitely.")

def sync_real_data_to_db():
    print("Initiating async data sync check...")
    thread = threading.Thread(target=_sync_real_data_blocking, daemon=True)
    thread.start()

sync_real_data_to_db()

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
    try:
        country = request.args.get('country', '')
        industry = request.args.get('industry', '')
        category = request.args.get('category', '')
        search = request.args.get('search', '').lower()
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 50, type=int)
        per_page = min(per_page, 100)  # Safety cap

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

        # Server-side pagination: get total filtered count first (lightweight)
        total_filtered = query.count()

        # Paginated query - only fetch ONE page of results
        results = query.order_by(GlobalOpportunity.fit_score.desc()) \
                       .offset((page - 1) * per_page) \
                       .limit(per_page) \
                       .all()

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

        # Lightweight stats using SQL aggregation (no full table load)
        total_in_db = GlobalOpportunity.query.count()

        # Build stats from lightweight queries instead of loading all records
        stats = {'countries': {}, 'categories': {}, 'industries': {}}
        cat_counts = db.session.query(
            GlobalOpportunity.category, db.func.count(GlobalOpportunity.id)
        ).group_by(GlobalOpportunity.category).all()
        for cat_val, cnt in cat_counts:
            if cat_val:
                stats['categories'][cat_val] = cnt

        country_counts = db.session.query(
            GlobalOpportunity.country, db.func.count(GlobalOpportunity.id)
        ).group_by(GlobalOpportunity.country).all()
        for c_val, cnt in country_counts:
            if c_val:
                stats['countries'][c_val] = cnt

        # Industries are comma-separated so we need a lightweight scan
        # But limit the scan to avoid OOM
        ind_rows = GlobalOpportunity.query.with_entities(
            GlobalOpportunity.industries
        ).filter(GlobalOpportunity.industries.isnot(None)).limit(5000).all()
        for (ind_str,) in ind_rows:
            if ind_str:
                for ind in ind_str.split(','):
                    ind = ind.strip()
                    if ind:
                        stats['industries'][ind] = stats['industries'].get(ind, 0) + 1

        return jsonify({
            'total': total_filtered,
            'total_in_db': total_in_db,
            'page': page,
            'per_page': per_page,
            'total_pages': math.ceil(total_filtered / per_page) if per_page > 0 else 1,
            'stats': stats,
            'records': filtered,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        })
    except Exception as e:
        # Graceful fallback during DB rebuild / cold boot
        print(f"API Error (likely DB rebuilding): {e}")
        return jsonify({
            'total': 0,
            'total_in_db': 0,
            'page': 1,
            'per_page': 50,
            'total_pages': 0,
            'stats': {'countries': {}, 'categories': {}, 'industries': {}},
            'records': [],
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'),
            'status': 'loading',
            'message': 'Database is initializing. Please refresh in 1-2 minutes.'
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
