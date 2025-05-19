from app.extensions import mongo
from app.schemas.user_schema import UserSchema
from app.utils.jwt_helper import create_token
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify

class UserService:
    @staticmethod
    def register_user(data):
        required_fields = ["email", "password", "name"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400

        user_data = data

        if mongo.db.users.find_one({"email": user_data["email"]}):
            return jsonify({"error": "Email already exists"}), 409

        user_data["password"] = generate_password_hash(user_data["password"])
        mongo.db.users.insert_one(user_data)
        return jsonify({"message": "User registered successfully"}), 201

    @staticmethod
    def login_user(data):
        user = mongo.db.users.find_one({"email": data.get("email")})
        if user and check_password_hash(user["password"], data.get("password")):
            token = create_token(user["email"])
            return jsonify({"access_token": token}), 200
        return jsonify({"error": "Invalid credentials"}), 401

    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        return jsonify([user for user in users]), 200
