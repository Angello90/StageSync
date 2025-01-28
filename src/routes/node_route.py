from flask import Blueprint, jsonify, request, render_template

from ..config import nodes
from flask_cors import CORS

node_bp = Blueprint("node_bp", __name__, template_folder="../templates", static_folder="../static")

CORS(node_bp)


@node_bp.route("/plug", methods=["POST"])
def plug_route():
    data = request.json
    id = data.get('id')
    ip = request.remote_addr
    if id and ip:
        print(nodes)
        if id in nodes or str(ip) in [node['ip'] for node in nodes.values()]:
            return jsonify({"message": "Node with this id or ip is already plugged"}), 400
        nodes[id] = {'ip': ip, "status": "on"}
        print(f"Nouveau noeud: IP:{ip}, ID:{id}, Status: ON")
        return jsonify({"message": f"Node {id} is plugged"}), 201
    return jsonify({"message": "Node id is required"}), 400



@node_bp.route("/list", methods=["GET"])
def list_route():
    return render_template("NodesList_templates.html", nodes=nodes)