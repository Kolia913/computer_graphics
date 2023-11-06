from flask import Flask
from flask_cors import CORS

from routes import api_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"

    app.register_blueprint(api_bp)

    print("Available routes:", app.url_map)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8001)
