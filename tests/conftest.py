import pytest
from flask import Flask
from flask_jwt import JWT, jwt_required
from app.use_cases.auth import authenticate, identity
from app.interfaces import routes
from app.db.db import db

@pytest.fixture(scope='session')
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    jwt = JWT(app, authenticate, identity)
    
    routes.init_app(app, jwt)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
