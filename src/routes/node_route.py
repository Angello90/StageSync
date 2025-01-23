from flask import Blueprint, jsonify, request, render_template
from flask_sock import Sock
from socketio import AsyncServer
from ..config import nodes
from flask_cors import CORS

node_bp = Blueprint("node_bp", __name__, template_folder="../templates")


CORS(node_bp)


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