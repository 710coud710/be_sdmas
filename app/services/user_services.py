from app.extensions import mongo
from app.schemas.user_schema import UserSchema
from app.utils.jwt_helper import create_token
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify

def register_user(data):
    schema = UserSchema()
    try:
        user_data = schema.load(data)
    except Exception as err:
        return jsonify({"error": str(err)}), 400

    if mongo.db.users.find_one({"email": user_data["email"]}):
        return jsonify({"error": "Email already exists"}), 409

    user_data["password"] = generate_password_hash(user_data["password"])
    mongo.db.users.insert_one(user_data)
    return jsonify({"message": "User registered successfully"}), 201

def login_user(data):
    user = mongo.db.users.find_one({"email": data.get("email")})
    if user and check_password_hash(user["password"], data.get("password")):
        token = create_token(user["email"])
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
