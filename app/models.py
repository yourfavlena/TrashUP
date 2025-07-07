from app import db
from datetime import datetime

class TrashImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    annotation = db.Column(db.String(10))  # 'pleine' ou 'vide'
    file_size = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    avg_red = db.Column(db.Float)
    avg_green = db.Column(db.Float)
    avg_blue = db.Column(db.Float)
    histogram = db.Column(db.PickleType)
    contrast = db.Column(db.Float)
    edges = db.Column(db.PickleType)
    luminance_hist = db.Column(db.PickleType)
    localisation = db.Column(db.String(120))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    # Ajouter d'autres champs si besoin