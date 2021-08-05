from flask import Blueprint
signup_blueprint = Blueprint(
    'signup',
    __name__,
    template_folder='templates/signup'
    )