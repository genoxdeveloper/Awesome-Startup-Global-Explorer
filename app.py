from flask import Flask, render_template, request, jsonify, Response, session
from flask_babel import Babel, _
from datetime import datetime, timedelta
import math
import csv
import io
import os
import threading
import secrets
import logging
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
from deep_translator import GoogleTranslator
from flask import request
from models import db, GlobalOpportunity, init_db
from startup_crawler_global import run_crawler_and_save

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@lru_cache(maxsize=5000)
def translate_title(text, target_lang):
    if not text or target_lang == 'en': return text
    
    # Skip translating likely brand names (short, title-cased)
    words = text.split()
    if len(words) <= 4 and all(w[0].isupper() for w in words if w.isalpha()):
        # Exclude common generic words that SHOULD be translated
        generic_words = {"Fund", "Program", "Grant", "Package", "Support", "Challenge"}
        if not any(g in text for g in generic_words):
            return text

    try:
        lang_map = {'zh_Hans': 'zh-CN', 'zh_Hant': 'zh-TW', 'ja': 'ja', 'ko': 'ko'}
        t_lang = lang_map.get(target_lang, target_lang.split('_')[0])
        return GoogleTranslator(source='auto', target=t_lang).translate(text)
    except Exception as e:
        logging.warning(f"Translation failed for '{text}': {e}")
        return text

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_PATH = os.path.join(BASE_DIR, 'instance')
if not os.path.exists(INSTANCE_PATH):
    os.makedirs(INSTANCE_PATH)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(INSTANCE_PATH, "global_data.db")}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'ko', 'ja', 'zh_Hans', 'zh_Hant', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ru', 'tr', 'id', 'vi', 'th']
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))

def get_locale():
    return request.args.get('lang') or session.get('lang') or 'en'

babel = Babel(app, locale_selector=get_locale)

init_db(app)

# ---------------------------------------------------------------------------
# Security Headers (production hardening)
# ---------------------------------------------------------------------------
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=()'
    return response

# ---------------------------------------------------------------------------
# Auto-cleanup: delete records older than 3 months
# ---------------------------------------------------------------------------
def cleanup_old_records():
    """Remove records with created_at older than 3 months."""
    with app.app_context():
        cutoff = datetime.utcnow() - timedelta(days=90)
        old_count = GlobalOpportunity.query.filter(
            GlobalOpportunity.created_at.isnot(None),
            GlobalOpportunity.created_at < cutoff
        ).count()
        if old_count > 0:
            db.session.delete(GlobalOpportunity.query.filter(
                GlobalOpportunity.created_at.isnot(None),
                GlobalOpportunity.created_at < cutoff
            ))
            db.session.commit()
            logging.info(f"Cleaned up {old_count} records older than 3 months (before {cutoff.strftime('%Y-%m-%d')})")
        else:
            logging.info("No records older than 3 months. Nothing to clean up.")

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
            logging.info("Database is empty. Seeding with 100% real global dataset in background...")
            run_crawler_and_save()
            logging.info("Initial real data seed complete.")
        else:
            logging.info(f"Database has {current_count} records. No limit — data accumulates indefinitely.")

def sync_real_data_to_db():
    logging.info("Initiating async data sync check...")
    thread = threading.Thread(target=_sync_real_data_blocking, daemon=True)
    thread.start()

if os.environ.get('VERCEL') != '1':
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
        logging.info(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Auto-crawl starting (Global)...")
        try:
            from startup_crawler_global import run_crawler_and_save
            run_crawler_and_save()
            logging.info("Auto-crawl (Global) complete.")
        except Exception as e:
            logging.error(f"Auto-crawl (Global) error: {e}", exc_info=True)

if os.environ.get('VERCEL') != '1':
    _scheduler_thread = threading.Thread(target=auto_crawl_scheduler, daemon=True)
    _scheduler_thread.start()
    logging.info(f"Auto-crawl scheduler started (every {AUTO_CRAWL_INTERVAL // 3600} hours)")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@app.route('/explore')
def dashboard():
    return render_template('dashboard.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

def require_admin_key():
    api_key = request.headers.get('X-Admin-Key') or request.args.get('api_key')
    expected_key = os.environ.get('ADMIN_API_KEY')
    
    # Fail fast if ADMIN_API_KEY is not configured in environment
    if not expected_key:
        logging.warning("ADMIN_API_KEY is not set in environment! Rejecting admin action.")
        return False
        
    return api_key == expected_key

@app.route('/api/admin/sources', methods=['GET', 'POST'])
def admin_sources():
    if not require_admin_key():
        return jsonify({"status": "error", "message": "Unauthorized"}), 401
        
    from models import CrawlerSource
    if request.method == 'GET':
        sources = CrawlerSource.query.all()
        return jsonify([{
            "id": s.id, "name": s.name, "url": s.url, 
            "method": s.method, "status": s.status, 
            "last_crawled_at": s.last_crawled_at.strftime('%Y-%m-%d %H:%M:%S') if s.last_crawled_at else None
        } for s in sources])
        
    if request.method == 'POST':
        data = request.json
        new_source = CrawlerSource(
            name=data.get('name'), url=data.get('url'), method=data.get('method', 'GET')
        )
        db.session.add(new_source)
        db.session.commit()
        return jsonify({"status": "success", "id": new_source.id}), 201
def api_health():
    """Health check endpoint for monitoring."""
    try:
        count = GlobalOpportunity.query.count()
        return jsonify({'status': 'ok', 'records': count, 'version': '2.5.0'})
    except Exception:
        return jsonify({'status': 'initializing', 'records': 0, 'version': '2.5.0'})

@app.route('/robots.txt')
def robots_txt():
    host_url = request.host_url.rstrip('/')
    return Response(
        f'User-agent: *\nAllow: /\nSitemap: {host_url}/sitemap.xml\n',
        mimetype='text/plain'
    )

@app.route('/sitemap.xml')
def sitemap_xml():
    host_url = request.host_url.rstrip('/')
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{host_url}/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>
  <url><loc>{host_url}/api/health</loc><changefreq>always</changefreq><priority>0.3</priority></url>
</urlset>'''
    return Response(xml, mimetype='application/xml')

last_refresh_time = 0

@app.route('/api/refresh', methods=['POST'])
def api_refresh():
    if not require_admin_key():
        return jsonify({"status": "error", "message": "Unauthorized"}), 401
        
    global last_refresh_time
    import time
    now = time.time()
    if now - last_refresh_time < 300: # 5 minutes limit
        return jsonify({"status": "error", "message": "Rate limit exceeded. Please wait 5 minutes between manual refreshes."}), 429
    
    last_refresh_time = now
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
        deadline_filter = request.args.get('deadline', 'All')
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 50, type=int)
        per_page = min(per_page, 100)  # Safety cap
        sort_by = request.args.get('sort_by', 'fit_score')
        sort_dir = request.args.get('sort_dir', 'desc')

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
        if deadline_filter == 'rolling':
            query = query.filter(GlobalOpportunity.deadline.in_(['Rolling', 'Next Month']))
        elif deadline_filter == 'fixed':
            query = query.filter(~GlobalOpportunity.deadline.in_(['Rolling', 'Next Month']))
            query = query.filter(GlobalOpportunity.deadline.is_not(None))
        if search:
            query = query.filter(db.or_(
                GlobalOpportunity.title.ilike(f"%{search}%"),
                GlobalOpportunity.description.ilike(f"%{search}%"),
                GlobalOpportunity.provider.ilike(f"%{search}%")
            ))

        # Server-side pagination: get total filtered count first (lightweight)
        total_filtered = query.count()

        # Server-side sorting
        sort_columns = {
            'title': GlobalOpportunity.title,
            'country': GlobalOpportunity.country,
            'fit_score': GlobalOpportunity.fit_score,
            'created_at': GlobalOpportunity.created_at,
            'deadline': GlobalOpportunity.deadline,
        }
        # Default: newest first (created_at desc) — shows today's opportunities first
        default_sort_col = GlobalOpportunity.created_at
        sort_col = sort_columns.get(sort_by, default_sort_col)
        order = sort_col.asc() if sort_dir == 'asc' else sort_col.desc()

        # Paginated query - only fetch ONE page of results
        results = query.order_by(order) \
                       .offset((page - 1) * per_page) \
                       .limit(per_page) \
                       .all()

        filtered = []
        target_lang = get_locale()
        
        # Parallel translation
        with ThreadPoolExecutor(max_workers=10) as executor:
            translated_titles = list(executor.map(
                lambda r: translate_title(r.title, target_lang) if target_lang != 'en' else r.title,
                results
            ))

        for idx, r in enumerate(results):
            # Build a safe apply URL — never show fake apply.genox.one links
            raw_url = r.url or ''
            if raw_url and 'apply.genox.one' not in raw_url:
                apply_url = raw_url
            else:
                # Use real portal per country
                portals = {
                    # Asia Pacific
                    'South Korea': 'https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do',
                    'Japan': 'https://j-net21.smrj.go.jp/startup/index.html',
                    'India': 'https://www.startupindia.gov.in/content/sih/en/government_schemes.html',
                    'Singapore': 'https://www.enterprisesg.gov.sg/financial-assistance',
                    'Australia': 'https://business.gov.au/grants-and-programs',
                    'New Zealand': 'https://www.callaghaninnovation.govt.nz/grants',
                    'China': 'https://innofund.most.gov.cn/',
                    'Taiwan': 'https://startup.sme.gov.tw/',
                    'Hong Kong': 'https://www.hkstp.org/our-programmes/',
                    'Indonesia': 'https://startup.hub.id/',
                    'Thailand': 'https://www.nia.or.th/',
                    'Vietnam': 'https://www.startup.gov.vn/',
                    'Malaysia': 'https://www.mdec.my/digital-economy-initiatives',
                    'Philippines': 'https://dict.gov.ph/startup-grant-fund/',
                    # Europe
                    'UK': 'https://www.gov.uk/business-finance-support',
                    'Germany': 'https://www.foerderdatenbank.de/FDB/DE/Foerderprogramme/foerderprogramme.html',
                    'France': 'https://www.bpifrance.fr/nos-offres',
                    'Netherlands': 'https://www.rvo.nl/subsidies-financiering',
                    'Sweden': 'https://www.vinnova.se/en/apply-for-funding/',
                    'Finland': 'https://www.businessfinland.fi/en/do-business-with-finland/funding',
                    'Denmark': 'https://www.innovationsfonden.dk/en/apply',
                    'Norway': 'https://www.innovasjonnorge.no/en/',
                    'Estonia': 'https://eas.ee/en/apply-for-funding/',
                    'Spain': 'https://www.cdti.es/index.asp?idIdioma=2',
                    'Italy': 'https://www.mise.gov.it/',
                    'Switzerland': 'https://www.innosuisse.ch/inno/en/home.html',
                    'EU': 'https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home',
                    'Israel': 'https://innovationisrael.org.il/en/program/',
                    # Americas
                    'USA': 'https://www.sbir.gov/solicitations',
                    'Canada': 'https://innovation.ised-isde.canada.ca/innovation/s/?language=en_CA',
                    'Brazil': 'https://www.bndes.gov.br/wps/portal/site/home/financiamento',
                    'Mexico': 'https://www.inadem.gob.mx/',
                    'Chile': 'https://www.corfo.cl/sites/cpp/home',
                    'Colombia': 'https://www.innpulsa.gov.co/',
                    'Argentina': 'https://www.argentina.gob.ar/produccion/sepyme',
                    # MEA
                    'UAE': 'https://hub71.com/apply/',
                    'Saudi Arabia': 'https://www.monsha.at.gov.sa/',
                    'South Africa': 'https://www.seda.org.za/funding-support/',
                    'Nigeria': 'https://tonyelumelufoundation.org/teep/application/',
                    'Kenya': 'https://www.ilab.co.ke/',
                    'Ghana': 'https://mest.co/apply/',
                    'Egypt': 'https://www.itida.gov.eg/',
                    'Zimbabwe': 'https://www.zimtrade.co.zw/',
                    'Zambia': 'https://www.zda.org.zm/',
                    'Tanzania': 'https://www.costech.or.tz/',
                    'Uganda': 'https://www.tic.co.ug/',
                    'Rwanda': 'https://risa.rw/',
                    'Ethiopia': 'https://www.ethiopianembassy.org/investment',
                    'Morocco': 'https://www.maroc.ma/',
                    'Tunisia': 'https://www.startup.gov.tn/',
                    # Default
                    'Global': 'https://www.f6s.com/programs',
                }
                country_key = r.country or 'Global'
                apply_url = portals.get(country_key, f'https://www.google.com/search?q={r.title.replace(" ", "+")}')

            filtered.append({
                "title": r.title,
                "translated_title": translated_titles[idx],
                "description": r.description,
                # Do NOT Babel-translate country/category — these are proper nouns/tech terms
                "country": r.country or "Global",
                "category": r.category or "",
                "industries": r.industries.split(',') if r.industries else [],
                "status": r.status,
                "funding": r.funding, "equity": r.equity,
                "provider": r.provider, "fit_score": r.fit_score,
                "deadline": r.deadline or 'Rolling',
                "url": apply_url,
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

@app.route('/api/export')
def api_export():
    """Export filtered results as CSV (max 5000 rows for safety)."""
    try:
        country = request.args.get('country', '')
        category = request.args.get('category', '')
        industry = request.args.get('industry', '')
        search = request.args.get('search', '').lower()

        query = GlobalOpportunity.query
        if country and country != 'Global':
            query = query.filter(GlobalOpportunity.country == country)
        if category and category != 'All':
            query = query.filter(GlobalOpportunity.category == category)
        if search:
            query = query.filter(db.or_(
                GlobalOpportunity.title.ilike(f"%{search}%"),
                GlobalOpportunity.description.ilike(f"%{search}%"),
                GlobalOpportunity.provider.ilike(f"%{search}%")
            ))
        if industry and industry != 'All':
            query = query.filter(db.or_(
                GlobalOpportunity.industries.ilike("%All%"),
                GlobalOpportunity.industries.ilike(f"%{industry}%")
            ))

        results = query.order_by(GlobalOpportunity.fit_score.desc()).limit(5000).all()

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Title', 'Category', 'Country', 'Provider', 'Funding', 'Equity', 'Industries', 'Fit Score', 'Status'])
        for r in results:
            writer.writerow([r.title, r.category, r.country, r.provider, r.funding, r.equity, r.industries, r.fit_score, r.status])

        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': f'attachment; filename=startup_opportunities_{datetime.now().strftime("%Y%m%d")}.csv'}
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
