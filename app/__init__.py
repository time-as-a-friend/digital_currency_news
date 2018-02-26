from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    from .apis.api_1_0 import api_1_0 as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app
