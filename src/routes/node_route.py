from flask import Blueprint, jsonify, request, render_template
from ..config import nodes

node_bp = Blueprint("node_bp", __name__, template_folder="../templates")

@node_bp.route("/plug", methods=["POST"])
def plug_route():
    node_data = request.json
    node_id = node_data.get('id')
    node_ip = request.remote_addr
    if node_id:
        nodes[node_id] = {'ip': node_ip, "status": "on"}
        return jsonify({"message": f"Node {node_id} is plugged"}), 201
    return jsonify({"message": "Node id is required"}), 400


@node_bp.route("/list", methods=["GET"])
def list_route():
    return render_template("NodesList_templates.html", nodes=nodes)