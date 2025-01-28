from flask import Flask, render_template
from .routes import registration_routes
from flask_socketio import SocketIO


def create_app():
    app = Flask("Api_server_web")
    
    app = Flask(__name__, static_folder='static')
    app.config["DEBUG"] = True
    
    @app.route("/favicon.ico")
    def favicon():
        return app.send_static_file("images/logo.png")

    registration_routes(app)
    socketio = SocketIO(app, cors_allowed_origins="*")
    
    @app.errorhandler(404)
    def error_404(error):
        return render_template("404.html"), 404

    return app, socketio