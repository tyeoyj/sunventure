from app import db

class MonthlyCPI(db.Model):
    date = db.Column(db.Date, primary_key=True)
    cpi = db.Column(db.Float)