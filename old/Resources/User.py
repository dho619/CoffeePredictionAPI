from flask_restful import Resource
from flask import request
from werkzeug.security import  generate_password_hash
import json

from db.dbRedis import dbRedis
from Api import db
from utils.gets import getUsuario
from services.auth import auth, is_admin, is_your
from models.Users import Users, user_schema, users_schema

with open('db/db.json') as arq:
    usuarios = json.load(arq)

class User(Resource):
    @auth.login_required#estar logado
    @is_admin #ser administrador
    def get(self):
        #pegando argumentos
        args = {arg: request.args[arg] for arg in request.args}

        #sem nao tem args retorna todos
        if len(args) == 0:
            return usuarios

        #se tem args manda buscar o usuario especificado
        else:
            usuario = getUsuario(args)
            return usuario

    def post(self):
        data = request.json#busca o json da requisicasso
        try:
            name = data['name']
            email = data['email'].lower()
            password = data['password']
        except:
            return {
                'status': 'error',
                'mensage': 'Verifique se passou todos os campos nescessários'
            }
        usuario = getUsuario({"email": email})

        if usuario:
            return {
                'status': 'error',
                'mensage': 'Usuario informado já foi cadastrado'
            }
        else:
            perfil = data['perfil'] if 'perfil' in data else 'comum'
            return {
                'name': name,
                'email': email,
                'password': password,
                'perfil': perfil
            }

    @auth.login_required
    def put(self):
        args = {arg: request.args[arg] for arg in request.args}#pegando os argumentos
        usuario = getUsuario(args)
        if not usuario:
            return {
                'status': 'error',
                'mensage': 'Usuario informado não está cadastrado'
            }
        data = request.json#busca o json da requisicasso
        if not is_your(usuario['email']):
            return "Not authorized.", 401
        try:
            name = data['name'] if 'name' in data else usuario['name']
            email = data['email'].lower() if 'email' in data else usuario['email']
            password = data['password'] if 'password' in data else usuario['password']
            perfil = data['perfil'] if 'perfil' in data else usuario['perfil']
        except Exception as e:
            print(e)
            return {
                'status': 'error',
                'mensage': 'Verifique se passou todos os campos nescessários'
            }

        return {
            'name': name,
            'email': email,
            'password': password,
            'perfil': perfil
        }

    @auth.login_required
    def delete(self):
        args = {arg: request.args[arg] for arg in request.args}#pegando os argumentos
        usuario = getUsuario(args)

        if usuario:
            if not is_your(usuario['email']):
                return "Not authorized.", 401
            #Apagar:
            return{
                'status': 'OK',
                'message': 'Usuario excluido com suceso'
            }
        else:
            return{
                'status': 'Error',
                'message': 'Usuario não encontrado'
            }





# usuario = [u for usuario in usuarios if usuarios['id'] == filter['id']]
