from flask_restful import Resource
from flask import request
from json import dumps
from utils.login import login_Usuario  #funcao implementada em outro arquivo
from db.dbRedis import dbRedis

class Login(Resource):
    def post(self):
        data = request.json#busca o json da requisicasso
        try:
            email = data['email']
            password = data['password']
        except:
            return {
                        'status': 'Error',
                        'Message': 'Esperado email e password'
                    }
        usuario, token = login_Usuario(email, password) #criando o token
        if usuario:
            perfil = usuario['perfil']
            #Postar no banco Chave-Valor as informacoes do usuario logado por 3hrs
            key = token.decode("utf-8")

            value = dumps(usuario)#dicionario para json

            try:
                dbRedis.set(key, value, ex=60*60*3)#seg*min*hrs

                return {
                            'status': 'Sucess',
                            'Token': key
                        }
            except Exception as e:
                print(e)
                return {
                            'status': 'Error',
                            'Message': 'Erro ao gravar as informações no Banco'
                       }
        else:
            return {
                        'status': 'Error',
                        'Message': 'Email ou senha inválidos'
                    }
