from flask import Blueprint

userAdmin = Blueprint('userAdmin', __name__)

from app.userAdmin import routes