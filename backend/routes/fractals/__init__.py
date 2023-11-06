from flask import Blueprint
from .mandelbrot import mandelbrot_bp
from .julia import julia_bp
from .vicsek import vicsek_bp
from .general import general_bp


fractals_bp = Blueprint("fractals", __name__, url_prefix="/fractals")
fractals_bp.register_blueprint(mandelbrot_bp)
fractals_bp.register_blueprint(julia_bp)
fractals_bp.register_blueprint(vicsek_bp)
fractals_bp.register_blueprint(general_bp)