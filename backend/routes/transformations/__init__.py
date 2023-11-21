from flask import Blueprint

from .affine_transform import affine_bp


transformations_bp = Blueprint("transformations", __name__, url_prefix="/transformations")
transformations_bp.register_blueprint(affine_bp)
