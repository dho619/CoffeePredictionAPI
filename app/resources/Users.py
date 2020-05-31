from werkzeug.security import generate_password_hash
from flask import request, jsonify
from app import db
from ..models.Users import Users, user_schema, users_schema

def post_user():
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    pass_hash = generate_password_hash(password)
    user = Users(email, pass_hash, name)
    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except Exception as e:
        if ('Duplicate entry' in e.orig.args[1]):#se isso for true, significa que teve duplicida e nesse caso so pode ser o email
            return jsonify({'message': 'This email is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
