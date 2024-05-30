from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.api.routes import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
