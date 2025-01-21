from flask import Flask
from .routes import registration_routes

def create_app():
    app = Flask("Api_server_web")
    app = Flask(__name__, static_folder='static')
    app.config["DEBUG"] = True

    registration_routes(app)
    
    @app.errorhandler(404)
    def error_404(error):
        return {"message": "Resource not found"}, 404

    return app