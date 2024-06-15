from flask import Blueprint, jsonify, request

from src.composer import (
    create_user_composer,
    create_alarm_composer,
    login_composer,
    get_alarm_by_id_composer,
    get_alarms_composer,
)
from src.infra.web.flask_adapter import request_adapter

users_bp = Blueprint("users_bp", __name__)
alarms_bp = Blueprint("alarms_bp", __name__)


@users_bp.route("/user", methods=["POST"])
def create_user():
    http_response = request_adapter(request, create_user_composer())
    return jsonify(http_response.body), http_response.status_code


@alarms_bp.route("/alarm", methods=["POST"])
def create_alarm():
    http_response = request_adapter(request, create_alarm_composer())
    return jsonify(http_response.body), http_response.status_code


@alarms_bp.route("/alarm", methods=["GET"])
def get_alarm_by_id():
    http_response = request_adapter(request, get_alarm_by_id_composer())
    return jsonify(http_response.body), http_response.status_code


@alarms_bp.route("/alarm", methods=["GET"])
def get_alarms():
    http_response = request_adapter(request, get_alarms_composer())
    return jsonify(http_response.body), http_response.status_code


@users_bp.route("/login", methods=["POST"])
def login():
    http_response = request_adapter(request, login_composer())
    return jsonify(http_response.body), http_response.status_code
