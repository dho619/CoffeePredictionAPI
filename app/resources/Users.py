from werkzeug.security import generate_password_hash
from flask import request, jsonify
from app import db
from ..models.Users import Users, user_schema, users_schema
from ..models.Profiles import Profiles

def post_user():
    #pegando os campos da requisicao
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    pass_hash = generate_password_hash(password)#criptografa a senha
    user = Users(email, pass_hash, name)

    profile = Profiles.query.get(2) #buscando perfil comum
    user.profiles.append(profile) #adicionando perfil comum
    try:
        db.session.add(user)#adiciona
        db.session.commit()# commit no banco
        result = user_schema.dump(user)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except Exception as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o email
            return jsonify({'message': 'This email is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def update_user(id):
    user = Users.query.get(id)#procura o usuario pelo id

    if not user:#se nao existir o usuario
        return jsonify({'message': "User don't exist", 'data': {}}), 404

    pass_hash = generate_password_hash(request.json['password']) if 'password' in request.json else ''

    #substitui ou mantem os campos
    user.email = request.json['email'] if 'email' in request.json else user.email
    user.name = request.json['name'] if 'name' in request.json else user.name
    user.password = pass_hash if pass_hash != '' else user.password

    try:
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 201
    except Exception as e:
        if ('Duplicate entry' in e.orig.args[1]):#se isso for true, significa que teve duplicida e nesse caso so pode ser o email
            return jsonify({'message': 'This email is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_users():
    users = Users.query.all()#pega todos usuarios

    if users:
        result = users_schema.dump(users)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 201
    return jsonify({"message": "nothing found", "data":{}})

def get_user(id):
    user = Users.query.get(id)#busca usuario pelo id

    if user:#se existir
        result = user_schema.dump(user)
        return jsonify({"message": "Sucessfully fetched", "data": result})
    #se nao existir
    return jsonify({'message': "User don't exist", 'data': {}}), 404

def delete_user(id):
    user = Users.query.get(id)#busca usuario pelo id

    if not user:#se nao existir
        return jsonify({'message': "User don't exist", 'data': {}}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
