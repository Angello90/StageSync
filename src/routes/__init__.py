from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from .get_route import get_bp
from .home_route import home_bp
from .node_route import node_bp
from .planning_route import planning_bp
import os


def registration_routes(app: Flask):
    # Enregistrer les Blueprints pour les routes API
    app.register_blueprint(get_bp, url_prefix="/api")
    app.register_blueprint(node_bp, url_prefix="/api")
    app.register_blueprint(home_bp)
    app.register_blueprint(planning_bp, url_prefix="/api")

    SWAGGER_URL = '/api/docs'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    API_SPEC_PATH = os.path.join(BASE_DIR, '../swagger/swagger.yaml')

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        '/swagger/spec',  
        config={
            'app_name': "My Flask API"
        }
    )

    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    @app.route('/swagger/spec')
    def swagger_spec():
        directory = os.path.join(BASE_DIR, '../swagger')
        return send_from_directory(directory, 'swagger.yaml')
