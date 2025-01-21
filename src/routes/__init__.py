from .get_route import get_bp
from .home_route import home_bp
from .node_route import node_bp


def registration_routes(app):
    app.register_blueprint(get_bp, url_prefix="/api")
    app.register_blueprint(node_bp, url_prefix="/api")
    app.register_blueprint(home_bp)