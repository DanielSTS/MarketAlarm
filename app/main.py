import sys
import os
from flask import Flask
from flask_jwt import JWT

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(parent_dir, '..'))

from app.db.db import db
from app.use_cases.auth import authenticate, identity
from app.interfaces import routes


def create_app():
    application = Flask(__name__)
    application.config.from_object('app.config.Config')
    db.init_app(application)
    jwt = JWT(application, authenticate, identity)
    routes.init_app(application, jwt)
    return application


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
