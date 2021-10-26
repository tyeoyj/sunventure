import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {"connect_args": {"options":f"-c search_path={os.environ.get('SCHEMA')}"}}
