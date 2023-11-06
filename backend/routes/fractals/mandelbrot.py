import base64
import io
from flask import Blueprint, jsonify, request, send_file
from matplotlib import pyplot as plt

from models.fractals import mandelbrot, utils


mandelbrot_bp = Blueprint("mandelbrot", __name__)


@mandelbrot_bp.route("/mandelbrot", methods=["POST"])
def mandelbrot_fractal():
    data = request.get_json()

    try:
        max_iterations = int(data["max_iterations"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid max_iterations value."}), 400

    try:
        zoom_percentage = float(data["zoom_percentage"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid zoom_percentage value."}), 400

    color_map = data.get("color_map", "hot")
    save_to_file = data.get("save_to_file", False)

    # check color map exists in plotly
    if color_map not in plt.colormaps():
        return jsonify({"error": "Color map not found."}), 400

    print("Generating mandelbrot set...")
    mandelbrot_set = mandelbrot.generate_mandelbrot_set(zoom_percentage, max_iterations)
    print("Converting mandelbrot set to image...")
    img = utils.convert_set_to_image(mandelbrot_set, color_map, "bilinear")

    if save_to_file:
        return send_file(
            io.BytesIO(base64.b64decode(img)),
            as_attachment=True,
            mimetype="image/png",
            download_name="mandelbrot.png",
        )

    # return send_file(img, mimetype="image/png")
    return jsonify({"image": img})