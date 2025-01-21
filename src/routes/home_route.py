from flask import Blueprint, jsonify

home_bp = Blueprint("home_bp", __name__)

@home_bp.route("/", methods=["GET"])
def home_route():
    return jsonify({"message": "Hello, World!"})