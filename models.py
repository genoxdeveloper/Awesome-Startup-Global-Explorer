from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class GlobalOpportunity(db.Model):
    __tablename__ = 'global_opportunities'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    country = db.Column(db.String(100), index=True)
    category = db.Column(db.String(100), index=True)
    industries = db.Column(db.String(500)) # Stored as comma separated
    status = db.Column(db.String(100))
    funding = db.Column(db.String(200))
    equity = db.Column(db.String(100))
    provider = db.Column(db.String(200))
    fit_score = db.Column(db.Integer, default=50, index=True)
    deadline = db.Column(db.String(100))
    url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

class CrawlerSource(db.Model):
    __tablename__ = 'crawler_sources'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    method = db.Column(db.String(50), default="GET")
    status = db.Column(db.String(50), default="Active")
    last_crawled_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CrawlLog(db.Model):
    __tablename__ = 'crawl_logs'
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('crawler_sources.id'))
    status = db.Column(db.String(50))
    items_found = db.Column(db.Integer, default=0)
    error_message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class APIKey(db.Model):
    __tablename__ = 'api_keys'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    owner = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
