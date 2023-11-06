import base64
import io
from flask import Blueprint, jsonify, request, send_file
from matplotlib import pyplot as plt

from models.fractals import julia, utils


julia_bp = Blueprint("julia", __name__)


@julia_bp.route("/julia", methods=["POST"])
def julia_fractal():
    data = request.get_json()

    try:
        max_iterations = int(data["max_iterations"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid max_iterations value."}), 400

    try:
        zoom_percentage = float(data["zoom_percentage"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid zoom_percentage value."}), 400

    try:
        c_real = float(data["c_real"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid c_real value."}), 400

    try:
        c_imag = float(data["c_imag"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid c_imag value."}), 400

    color_map = data.get("color_map", "hot")
    save_to_file = data.get("save_to_file", False)

    # check color map exists in plotly
    if color_map not in plt.colormaps():
        return jsonify({"error": "Color map not found."}), 400

    print("Generating julia set...")
    julia_set = julia.generate_julia_set(
        c_real, c_imag, zoom_percentage, max_iterations
    )
    print("Converting julia set to image...")
    img = utils.convert_set_to_image(julia_set, color_map, "nearest")

    if save_to_file:
        return send_file(
            io.BytesIO(base64.b64decode(img)),
            as_attachment=True,
            mimetype="image/png",
            download_name="julia.png",
        )

    # return send_file(img, mimetype="image/png")
    return jsonify({"image": img})