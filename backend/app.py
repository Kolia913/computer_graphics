from flask import Flask, request, jsonify, send_file
from matplotlib import pyplot as plt

from fractals import mandelbrot

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"error": "API Mode. /api/.."}), 404


@app.route("/api/color_maps")
def color_maps():
    return jsonify({"color_maps": plt.colormaps()})


@app.route("/api/mandelbrot", methods=["POST"])
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

    # check color map exists in plotly
    if color_map not in plt.colormaps():
        return jsonify({"error": "Color map not found."}), 400

    print("Generating mandelbrot set...")
    mandelbrot_set = mandelbrot.generate_mandelbrot_set(zoom_percentage, max_iterations)
    print("Converting mandelbrot set to image...")
    img = mandelbrot.convert_set_to_image(mandelbrot_set, color_map)

    return send_file(img, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True, port=8001)
