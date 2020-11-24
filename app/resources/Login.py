from flask import jsonify, request
from ..utils.login import login_Usuario

def login():
    data = request.json
    try:
        email = data['email']
        password = data['password']
    except:
        return jsonify({'message': 'Expected email and password'}), 400

    token = login_Usuario(email, password)

    if token:
        return jsonify({'message': 'Sucessfully', 'token': token.decode('utf-8')}), 201

    else:
        return {'message': 'Invalid email or password', 'token': ''}, 401
