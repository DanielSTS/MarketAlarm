from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

from src.application.use_cases import identity
from src.domain.models import User
from src.infra.database.user_repository import create_user, get_alarms_by_user

app_blueprint = Blueprint("app_blueprint", __name__)


def init_app(app, jwt):
    @app_blueprint.route("/register", methods=["POST"])
    def register():
        username = request.json.get("username")
        password = request.json.get("password")
        if not username or not password:
            return jsonify({"error": "Invalid username or password"}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Username already exists"}), 409

        user = create_user(username, password)
        return jsonify({"user_id": user.id, "username": user.name}), 201

    @app_blueprint.route("/alarms", methods=["POST"])
    @jwt_required()
    def create_alarm():
        asset = request.json.get("asset")
        target_price = request.json.get("target_price")

        if not asset or not target_price:
            return jsonify({"error": "Invalid asset or target_price"}), 400

        user = identity(request.headers.get("Authorization").split(" ")[1])
        alarm = create_alarm(user, asset, target_price)
        return (
            jsonify(
                {
                    "alarm_id": alarm.id,
                    "asset": alarm.asset,
                    "target_price": alarm.target_price,
                }
            ),
            201,
        )

    @app_blueprint.route("/alarms", methods=["GET"])
    @jwt_required()
    def get_alarms():
        user = identity(request.headers.get("Authorization").split(" ")[1])
        alarms = get_alarms_by_user(user)
        alarms_data = [
            {
                "id": alarm.id,
                "asset": alarm.asset,
                "target_price": alarm.target_price,
            }
            for alarm in alarms
        ]
        return jsonify({"alarms": alarms_data}), 200

    @jwt.jwt_error_handler
    def jwt_error_handler(error):
        return jsonify({"error": error.description}), error.status_code

    app.register_blueprint(app_blueprint)
