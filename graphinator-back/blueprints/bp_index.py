from flask import Blueprint, make_response, request
from optimizer import readCommand

bp_index = Blueprint("bp_index", __name__)

@bp_index.route("/")
def get_index():
    return "<h1>HELLO WORLD</h1>"

@bp_index.route("/optimize", methods=["POST"])
def get_optimized_sql():
    req = request.json

    optimized = readCommand(req['sql'].lower())

    return make_response({"alg": optimized}, 200)