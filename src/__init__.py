from flask import Flask, render_template
from .routes import registration_routes

def create_app():
    app = Flask("Api_server_web")
    app = Flask(__name__, static_folder='static')
    app.config["DEBUG"] = True

    registration_routes(app)
    
    @app.errorhandler(404)
    def error_404(error):
        return render_template("404.html"), 404

    return app