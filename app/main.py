from flask import Flask

from app.adapters.controllers.campaign_controller import bp
from app.adapters.db.models import db
from app.config import Config
from app.container import Container
from app.utils.logging_config import init_logging

init_logging()


def create_app():
    app = Flask(__name__)
    config = Config()

    app.config['SQLALCHEMY_DATABASE_URI'] = config.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.container = Container()
    app.container.wire(modules=["app.adapters.controllers.campaign_controller"])

    app.register_blueprint(bp)

    @app.route("/health")
    def health():
        return "OK", 200

    return app
