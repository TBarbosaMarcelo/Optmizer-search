from flask import Flask
from flask_cors import CORS
from blueprints.bp_index import bp_index as index

def app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(index)

    return app


if __name__ == "__main__":
    server = Flask(__name__)
    CORS(server)
    server.register_blueprint(index)

    server.run("0.0.0.0", 6789)
