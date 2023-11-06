import base64
import io
from flask import Blueprint, jsonify, request, send_file

from models.fractals import vicsek, utils


vicsek_bp = Blueprint("vicsek", __name__)


@vicsek_bp.route("/vicsek", methods=["POST"])
def vicsek_fractal():
    data = request.get_json()

    try:
        levels = int(data["levels"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid levels value."}), 400

    if not 0 < levels < 5:
        return jsonify({"error": "Levels value must be between 0 and 5."}), 400

    save_to_file = data.get("save_to_file", False)

    print("Generating vicsek fractal...")
    fig = vicsek.get_vicsek_fractal(levels)
    print("Converting vicsek fractal to image...")
    img = utils.convert_figure_to_image(fig)

    if save_to_file:
        return send_file(
            io.BytesIO(base64.b64decode(img)),
            as_attachment=True,
            mimetype="image/png",
            download_name="vicsek.png",
        )

    return jsonify({"image": img})