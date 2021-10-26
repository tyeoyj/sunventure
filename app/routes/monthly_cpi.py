from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask import jsonify, abort

from app.models import monthly_cpi
from ..alphavantage import get_latest_CPI
from app import db
from app.models.monthly_cpi import MonthlyCPI 


class MonthlyCPIRoute(Resource):
    def get(self):
        latest_CPI = get_latest_CPI()
        date = latest_CPI["date"]
        cpi = latest_CPI["cpi"]
        monthly_cpi = MonthlyCPI(date=date, cpi=cpi)
        db.session.add(monthly_cpi)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, "This cpi for this month already exists in the db")


        return jsonify(latest_CPI) 
