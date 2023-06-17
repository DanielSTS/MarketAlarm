from flask import Flask
from flask_jwt import JWT, jwt_required
from app.db.db import db
from app.use_cases.auth import authenticate, identity
from app.interfaces import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    jwt = JWT(app, authenticate, identity)
    routes.init_app(app, jwt)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
