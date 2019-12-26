import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-easy-to-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AMQP_HOST = os.environ.get('AMQP_HOST') or 'amqp://transport'
    AMQP_PORT = os.environ.get('AMQP_PORT') or 5672
