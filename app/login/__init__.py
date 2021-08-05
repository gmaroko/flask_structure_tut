from flask import Blueprint
login_blueprint = Blueprint(
    'login',
    __name__,
    url_prefix = "/auth",
    template_folder='templates/login'
    )