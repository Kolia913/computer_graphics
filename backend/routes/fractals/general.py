from flask import Blueprint, jsonify
from matplotlib import pyplot as plt


general_bp = Blueprint("general", __name__)

@general_bp.route("/color_maps")
def color_maps():
    return jsonify({"color_maps": plt.colormaps()})