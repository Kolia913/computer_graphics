from flask import Blueprint, jsonify


general_bp = Blueprint("general", __name__)


@general_bp.route("/")
def home():
    return jsonify({"error": "API Mode. /api/.."}), 404