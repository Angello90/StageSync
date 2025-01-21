from flask import Blueprint, jsonify, request
from ..config import nodes
from ..services.timer_services import get_elapsed_time

get_bp = Blueprint("get_bp", __name__)


@get_bp.route("/get", methods=["GET"])
def timer_route():
    node_id = request.args.get('id')
    
    print(nodes)
    print(node_id)
    
    if node_id:
        for node in nodes:
            if str(node) == str(node_id):
                return jsonify({"time": f"{get_elapsed_time()}"}), 200

        
        return jsonify({"message": f"Node {node_id} not found"}), 404