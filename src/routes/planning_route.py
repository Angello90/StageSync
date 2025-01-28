from flask import Blueprint, jsonify, request, render_template
from ..config import nodes
from flask_cors import CORS
from ..config import planning


planning_bp = Blueprint("planning_bp", __name__, template_folder="../templates")


CORS(planning_bp)


@planning_bp.route("/planning", methods=["GET"])
def planning_route():
    return render_template("planning.html", planning=planning)


@planning_bp.route("/planning/new", methods=["POST"])
def planning_post_route():
    data = request.json
    nom = data.get('nom')
    debut = data.get('debut')
    fin = data.get('fin')
    
    print(data)
    if nom and debut and fin:
        if not any(group["nom"] == nom for group in planning):
            id = len(planning) + 1
        else:
            return jsonify({"message": "Name already exists in planning"}), 400
        push_data = {"id": id, "nom": nom, "debut": debut, "fin": fin}
        planning.append(push_data)
        print(planning)
        return jsonify({"message": f"Planning {id} is updated"}), 201
    return jsonify({"message": "Planning id is required"}), 400


@planning_bp.route("/planning/delete", methods=["POST"])
def planning_delete_route():
    data = request.json
    id = data.get('id')
    print(f"ID: {id}")
    if id:
        for event in planning:
            if str(event["id"]) == str(id):
                planning.remove(event)
                return jsonify({"message": f"Planning {id} is deleted"}), 200
        return jsonify({"message": "Planning id not found"}), 404
    return jsonify({"message": "Planning id is required"}), 400



@planning_bp.route("/planning/update", methods=["POST"])
def planning_update_route():
    data = request.json
    id = data.get('id')
    nom = data.get('nom')
    debut = data.get('debut')
    fin = data.get('fin')
    print(data)
    if id:
        for group in planning:
            if group["id"] == id:
                group["nom"] = nom
                group["debut"] = debut
                group["fin"] = fin
                return jsonify({"message": f"Planning {id} is updated"}), 200
        return jsonify({"message": "Planning id not found"}), 404
    return jsonify({"message": "Planning id is required"}), 400