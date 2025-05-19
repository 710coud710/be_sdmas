from flask import Blueprint, request, jsonify
from app.services.user_services import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return UserService.register_user(data)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return UserService.login_user(data)

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    user_email = get_jwt_identity()
    return jsonify({"email": user_email})

@user_bp.route('/all', methods=['GET'])
def get_all_users():
    return UserService.get_all_users()
