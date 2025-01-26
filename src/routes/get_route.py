from flask import Blueprint, jsonify, request
from ..config import nodes
from ..services.timer_services import get_elapsed_time
from flask_cors import CORS
get_bp = Blueprint("get_bp", __name__)


CORS(get_bp)

@get_bp.route("/get", methods=["GET"])
def timer_route():
    id = request.args.get('id')
    if id:
        for node in nodes:
            if str(node) == str(id):
                if nodes[node]['status'] == "on" and nodes[node]['ip'] == request.remote_addr:
                    return jsonify(get_elapsed_time()), 200

        return jsonify({"message": "Node is not plugged"}), 400