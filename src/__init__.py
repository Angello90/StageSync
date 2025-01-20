from flask import Flask
from .routes import registration_routes

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    registration_routes(app)

    return app