from flask import Flask, g, current_app
from app.config import Config
from app.transport.rmq import Transport


def create_app(appConfig):
    app = Flask(__name__)
    app.config.from_object(appConfig)

    with app.app_context() as ctx:
        ctx.app.transport = Transport(appConfig.AMQP_HOST, appConfig.AMQP_PORT)

    from app.userAdmin import userAdmin as ua
    app.register_blueprint(ua)

    return app

application = create_app(Config)

