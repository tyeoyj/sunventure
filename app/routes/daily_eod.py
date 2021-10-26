from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from flask import jsonify
from ..alphavantage import get_latest_EOD_close
from app import db
from app.models.daily_eod import DailyEOD


class DailyEODRoute(Resource):

    def get(self):
        return jsonify([dailyeod.as_dict() for dailyeod in DailyEOD.query.all()]) 

    def post(self):
        latest_EOD_close = get_latest_EOD_close()
        date = latest_EOD_close["date"]
        close = latest_EOD_close["close"]
        daily_eod = DailyEOD(date=date, close=close)
        db.session.add(daily_eod)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=f"This closing price for {date} already exists in the db")
        else:
            print(f"daily eod for {date} added to db")
        return jsonify(daily_eod.as_dict())
            

    