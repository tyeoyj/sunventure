from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from app.routes import daily_eod as de, monthly_cpi as mc
api.add_resource(de.DailyEODRoute, "/api/dailyeod")
api.add_resource(mc.MonthlyCPIRoute, "/api/monthlycpi")

from app.models import daily_eod, monthly_cpi

