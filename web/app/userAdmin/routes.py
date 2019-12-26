from app.userAdmin import userAdmin as ua
from flask import current_app


@ua.route('/userAdmin/ping')
def ping():
    with current_app.app_context() as ctx:
        ctx.app.transport.producer('a', 'b')
    return "Response from the service..."