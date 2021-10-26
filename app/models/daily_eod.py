from app import db

class DailyEOD(db.Model):
    date = db.Column(db.Date, primary_key=True)
    close = db.Column(db.Float)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}