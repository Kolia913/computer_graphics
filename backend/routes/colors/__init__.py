from flask import Blueprint

from .color_model import color_model_bp


colors_bp = Blueprint('colors', __name__, url_prefix='/colors')
colors_bp.register_blueprint(color_model_bp)