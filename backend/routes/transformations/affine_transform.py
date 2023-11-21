import base64
import io
import json
from flask import Blueprint, request, jsonify, send_file
from numpy import diag

from models.transformations.transform import is_square, transform_square


affine_bp = Blueprint("affine_transform", __name__, url_prefix="/")


@affine_bp.route("/affine_transform", methods=["POST"])
def affine_transform():
    data = request.get_json()

    # get diagonal coordinates from request
    diagonal_1 = data.get("diagonal_1", [0, 0])
    diagonal_2 = data.get("diagonal_2", [2, 2])

    if diagonal_1 == diagonal_2 or len(diagonal_1) != len(diagonal_2):
        return jsonify({"error": {"message": "Invalid square."}}), 400

    # check all coordinates in range (-10, 10)
    if not all(-10 <= x <= 10 for x in (diagonal_1 + diagonal_2)):
        return jsonify({"error": {"message": "Please enter range from -10 to 10"}}), 400

    if not is_square(diagonal_1, diagonal_2):
        return jsonify({"error": {"message": "Invalid square."}}), 400

    # get translation values
    move_top = data.get("move_top", 0)
    move_right = data.get("move_right", 0)

    # get scaling values
    scale_a = data.get("scale_a", 0)
    scale_d = data.get("scale_d", 0)

    # get rotation value
    rotation = data.get("rotation", 0)

    transformed_square_byte_arr = transform_square(
        (diagonal_1, diagonal_2), (move_right, move_top), (scale_a, scale_d), rotation
    )

    # convert image to base64 encoded string
    img_base64 = base64.b64encode(transformed_square_byte_arr.getvalue()).decode()

    prefix = "data:image/jpeg;base64,"
    return jsonify({"image": prefix + img_base64}), 200
