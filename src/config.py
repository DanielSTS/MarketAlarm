import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "postgresql://postgres:example@db/monitor_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
