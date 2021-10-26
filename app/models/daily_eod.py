from app import db

class DailyEOD(db.Model):
    date = db.Column(db.Date, primary_key=True)
    close = db.Column(db.Float)