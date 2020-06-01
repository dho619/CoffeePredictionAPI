from flask import jsonify
from ..services.login import login_Usuario

def login():
    data = request.json#busca o json da requisicasso
    try:
        email = data['email']
        password = data['password']
    except:
        return jsonify({'message': 'Expected email and password'}), 400
    usuario, token = login_Usuario(email, password) #criando o token
    if usuario:
        perfis = usuario['perfis']
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
