
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)


class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    order = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
