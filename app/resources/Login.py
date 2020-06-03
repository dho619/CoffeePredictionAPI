from flask import jsonify, request
from ..utils.login import login_Usuario


def login():
    data = request.json#busca o json da requisicasso
    try:
        email = data['email']
        password = data['password']
    except:
        return jsonify({'message': 'Expected email and password'}), 400

    token = login_Usuario(email, password) #criando o token

    if token:
        return jsonify({'message': 'Sucessfully', 'token': token}), 201

    else:
        return {'message': 'Invalid email or password', 'token': ''}, 401
