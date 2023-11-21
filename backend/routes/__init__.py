from flask import Blueprint
from .fractals import fractals_bp
from .colors import colors_bp
from .transformations import transformations_bp

api_bp = Blueprint("api", __name__, url_prefix="/api")
api_bp.register_blueprint(fractals_bp)
api_bp.register_blueprint(colors_bp)
api_bp.register_blueprint(transformations_bp)