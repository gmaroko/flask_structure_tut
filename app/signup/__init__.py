from flask import Blueprint
signup_blueprint = Blueprint(
    'signup',
    __name__,
    url_prefix = "/auth",
    template_folder='templates/signup'
    )