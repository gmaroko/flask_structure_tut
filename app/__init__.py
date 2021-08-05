from flask import Flask
from app.core import *
from app.login import *
from app.signup import *

def SET_UP(**kwargs):
    flask_app = Flask(__name__,**kwargs)

    # register our blueprints
    flask_app.register_blueprint(login_blueprint, url_prefix="/auth")
    flask_app.register_blueprint(signup_blueprint, url_prefix="/auth")
    flask_app.register_blueprint(core_blueprint, url_prefix="/shop")

    return flask_app

