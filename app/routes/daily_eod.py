from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask import jsonify, abort
from ..alphavantage import get_latest_EOD_close
from app import db
from app.models.daily_eod import DailyEOD


class DailyEODRoute(Resource):
    def get(self):
        latest_EOD_close = get_latest_EOD_close()
        date = latest_EOD_close["date"]
        close = latest_EOD_close["close"]
        daily_eod = DailyEOD(date=date, close=close)
        db.session.add(daily_eod)
        try:
            db.session.commit()
        except IntegrityError as e:
            print(e.__dict__)
            db.session.rollback()
            abort(400, "This closing price for this day already exists in the db")


        return jsonify(latest_EOD_close) 
