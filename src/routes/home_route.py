from flask import Blueprint, jsonify, render_template

home_bp = Blueprint("home_bp", __name__, template_folder="../templates", static_folder="../static")

@home_bp.route("/", methods=["GET"])
def home_route():
    return render_template("home_template.html")