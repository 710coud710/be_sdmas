from flask import Flask
from app.config import Config
from app.extensions import mongo, jwt
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)

    register_blueprints(app)

    return app
