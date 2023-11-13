import base64
import io
from flask import Blueprint, request, jsonify, send_file

from models import colors


color_model_bp = Blueprint("color_model", __name__)


@color_model_bp.route("/change_color_model", methods=["POST"])
def change_color_model():
    
    # get image from form request
    if request.files:
        img = request.files["image"]
        input_img = img.read()

    data = request.get_json()
    
    try:
        color_model = data["color_model"].lower()
        if color_model not in ('hsv', 'cmyk'):
            raise ValueError
    except (ValueError, KeyError):
        return jsonify({"error": "'Invalid color model. Expected hsv or cmyk."}), 400

    input_img = 'imgs/girl.jpg'
    # img = request.files["image"]

    if color_model == 'hsv':
        converted_image = colors.rgb_to_hsv_colorsys(input_img)
    else:
        converted_image = colors.rgb_to_cmyk_colorsys(input_img)

    img_io = io.BytesIO()
    converted_image.save(img_io, 'JPEG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.getvalue()).decode()

    # return jsonify({"image": img_base64})
    return send_file(img_io, mimetype='image/jpeg')
    

