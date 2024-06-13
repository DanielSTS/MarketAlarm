import os
import sys

from flask import Flask
from flask_jwt import JWT

from src.application.use_cases import authenticate, identity
from src.infra.db import db
from src.infra.web import routes

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(parent_dir, ".."))


def create_app():
    application = Flask(__name__)
    application.config.from_object("src.config.Config")
    db.init_app(application)
    jwt = JWT(application, authenticate, identity)
    routes.init_app(application, jwt)
    return application


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
