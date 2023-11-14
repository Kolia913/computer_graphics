import base64
import io
import json
from flask import Blueprint, request, jsonify, send_file
from PIL import Image

from models import colors


color_model_bp = Blueprint("color_model", __name__)


@color_model_bp.route("/change_color_model", methods=["POST"])
def change_color_model():
    
    # get image from form request
    if request.files:
        img = request.files["image"]
        input_img = img.read()
    else: 
        return jsonify({"error": {"message": "No image provided."}}), 400

    pil_img = Image.open(io.BytesIO(input_img))
    data = request.files['document'].read()
    data = json.loads(data)
    
    try:
        color_model = data["scheme"].lower()
        if color_model not in ('hsv', 'cmyk', 'rgb'):
            raise ValueError
    except (ValueError, KeyError):
        return jsonify({"error": {"message": "'Invalid color model. Expected hsv or cmyk."}}), 400

    brightness = data.get("lightness", 50)
    saturation = data.get("saturation", 50)

    x1 = data.get("x1", 0)
    y1 = data.get("y1", 0)
    x2 = data.get("x2", 0)
    y2 = data.get("y2", 0)

    if not all(x >= 0 for x in (x1, y1, x2, y2)):
        return jsonify({"error": {"message": "Invalid coordinates. Expected positive integers."}}), 400
    elif (x1 > x2) or (y1 > y2):
        return jsonify({"error": {"message": "Invalid coordinates. Expected x1 < x2 and y1 < y2."}}), 400
    elif (x1 > pil_img.width) or (x2 > pil_img.width) or (y1 > pil_img.height) or (y2 > pil_img.height):
        return jsonify({"error": {"message": f"Invalid coordinates. Expected x1, x2 < image width "
                                 f"({pil_img.width}) and y1, y2 < image height ({pil_img.height})."}}), 400
    elif all (x == 0 for x in (x1, y1, x2, y2)):
        x1 = y1 = 0
        x2 = pil_img.width
        y2 = pil_img.height

    area_to_edit = get_coordinates_are(x1, y1, x2, y2)

    if color_model == 'hsv':
        converted_image = colors.rgb_to_hsv_colorsys(pil_img, area_to_edit)
    elif color_model == 'cmyk':
        converted_image = colors.rgb_to_cmyk_colorsys(pil_img, area_to_edit)
    else:
        converted_image = pil_img

    modified_image = colors.change_image_sat_and_brightness(converted_image, saturation, brightness, area_to_edit)

    img_io = io.BytesIO()
    modified_image.save(img_io, 'JPEG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.getvalue()).decode()
    prefix = "data:image/jpeg;base64,"

    pixel_to_convert = (x1, y1)
    if not all(pixel_to_convert):
        pixel_to_convert = (
            round(pil_img.width / 2),
            round(pil_img.height / 2)
        )

    pixel_conversion = convert_pixel(pil_img, pixel_to_convert[0], pixel_to_convert[1], color_model)

    return jsonify({
        "image": prefix + img_base64,
        "pixel_conversion": pixel_conversion,
    })
    # return send_file(img_io, mimetype='image/jpeg')
    

def get_coordinates_are(x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
    # generate square of coordinates
    result = [(x, y) for x in range(x1, x2) for y in range(y1, y2)]
    print(len(result))

    return result


def convert_pixel(image: Image, x: int, y: int, to_scheme: str) -> dict:
    pixel = image.getpixel((x, y))
    if to_scheme == 'hsv':
        converted = colors.rgb_to_hsv(pixel)
    elif to_scheme == 'cmyk':
        converted = colors.rgb_to_cmyk(*pixel)
    else:
        to_scheme = 'rgb'
        converted = pixel

    return {
        "rgb": f"rgb{pixel}",
        "converted": to_scheme + str(converted),
    }