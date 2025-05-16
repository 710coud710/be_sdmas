from marshmallow import Schema, fields

class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
