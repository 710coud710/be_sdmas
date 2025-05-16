from .user_routes import user_bp
from .main import main_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix='/api/users')
