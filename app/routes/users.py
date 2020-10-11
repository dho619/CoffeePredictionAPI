from app import app
from flask import jsonify
from ..resources import Users, Login
from ..services.auth import auth, is_admin, is_your

@app.route('/login', methods=['POST'])
def login():
    return Login.login()

@app.route('/users', methods=['GET'])
@auth.login_required
@is_admin
def get_users():
    return Users.get_users()

@app.route('/users/<id>', methods=['GET'])
@auth.login_required
def get_user(id):
    if is_your(id):
        return Users.get_user(id)
    else:
        return jsonify({'message': "Unauthorized action."}), 401

@app.route('/users', methods=['POST'])
def post_user():
    return Users.post_user()

@app.route('/users/<id>', methods=['PUT'])
@auth.login_required
def update_user(id):
    if is_your(id):
        return Users.update_user(id)
    else:
        return jsonify({'message': "Unauthorized action."}), 401

@app.route('/users/<id>', methods=['DELETE'])
@auth.login_required
@is_admin
def delete_user(id):
    return Users.delete_user(id)
