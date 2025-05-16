from flask import Blueprint
from flask import jsonify


main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/', methods=['GET'])
def get_products():
    return jsonify({"message": "Hello, World!"})
