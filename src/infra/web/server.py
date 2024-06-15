from flask import Flask, jsonify

from src.error_handler import error_handler
from src.infra.web.routes import alarms_bp, users_bp

app = Flask(__name__)
app.debug = True
app.register_blueprint(users_bp)
app.register_blueprint(alarms_bp)


@app.errorhandler(Exception)
def handle_exception(ex):
    response = error_handler(ex)
    return jsonify(response.body), response.status_code
