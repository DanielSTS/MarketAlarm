from flask import Flask

from src.infra.web.routes import alarms_bp, users_bp

app = Flask(__name__)
app.debug = True
app.register_blueprint(users_bp)
app.register_blueprint(alarms_bp)
