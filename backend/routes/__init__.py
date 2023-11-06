from flask import Blueprint
from .fractals import fractals_bp

api_bp = Blueprint("api", __name__, url_prefix="/api")
api_bp.register_blueprint(fractals_bp)