from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 500,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

api = Api(app, errors=errors)

from app.routes import daily_eod as de, monthly_cpi as mc
api.add_resource(de.DailyEODRoute, "/api/dailyeod")
api.add_resource(mc.MonthlyCPIRoute, "/api/monthlycpi")

from app.models import daily_eod, monthly_cpi

