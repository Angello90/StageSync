from .get_route import get_bp


def registration_routes(app):
    app.register_blueprint(get_bp, url_prefix="/api")