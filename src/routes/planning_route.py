from flask import Blueprint, jsonify, request, render_template
from ..config import nodes
from flask_cors import CORS
from ..config import planning

planning_bp = Blueprint("planning_bp", __name__, template_folder="../templates")


CORS(planning_bp)


@planning_bp.route("/planning", methods=["GET"])
def planning_route():
    return render_template("planning.html", planning=planning)


@planning_bp.route("/planning", methods=["POST"])
def planning_post_route():
    data = request.json
    nom = data.get('nom')
    temps = data.get('duree')
    print(data)
    if nom and temps:
        if not any(group["nom"] == nom for group in planning):
            id = len(planning) + 1
        else:
            return jsonify({"message": "Name already exists in planning"}), 400
        push_data = {"id": id, "nom": nom, "duree": temps}
        planning.append(push_data)
        print(planning)
        return jsonify({"message": f"Planning {id} is updated"}), 201
    return jsonify({"message": "Planning id is required"}), 400