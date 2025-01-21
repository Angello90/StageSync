from flask import Blueprint, jsonify, request, render_template
from flask_socketio import SocketIO
from ..config import nodes

node_bp = Blueprint("node_bp", __name__, template_folder="../templates")

socketio = SocketIO()

@node_bp.route("/plug", methods=["POST"])
def plug_route():
    data = request.json
    id = data.get('id')
    ip = request.remote_addr
    if id:
        nodes[id] = {'ip': ip, "status": "on"}
        return jsonify({"message": f"Node {id} is plugged"}), 201
    return jsonify({"message": "Node id is required"}), 400


@node_bp.route("/list", methods=["GET"])
def list_route():
    return render_template("NodesList_templates.html", nodes=nodes)