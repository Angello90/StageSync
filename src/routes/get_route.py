from flask import Blueprint, jsonify

get_bp = Blueprint("get_bp", __name__)


@get_bp.route("/get", methods=["GET"])
def get_route():
    data = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
        {"id": 3, "name": "Doe"}
    ]
    return jsonify(data)