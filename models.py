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
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
