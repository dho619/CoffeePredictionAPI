from flask import jsonify
from flask_httpauth import HTTPTokenAuth
from functools import wraps
from ..utils.login import decode_auth_token
from ..utils.gets import getUsuario, isAdmin

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def user_logged(token):
    user = decode_auth_token(token)
    if not user:
        return False
    try:
        auth.current_user = user['sub']#id do usuario logado
        return True
    except:
        return False


#criando um decorador para autentificar se e admin
def is_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if isAdmin(getUsuario({'id': auth.current_user})):#pega o usuario e manda pro is Admin que retorna se e admin
            return f(*args, **kwargs)
        return jsonify({'message': "Unauthorized, admin-only access."}), 401
    return wrapper


# funcao para verificar se id passado e o id da pessoa logada
def is_your(id):
    if id == None:
        return False
    usuario = getUsuario({'id': auth.current_user})
    return usuario and (isAdmin(usuario) or usuario.id == int(id))

#funcao que retorna o id do usario logado e se ele é admin
def token_user():
    usuario = getUsuario({'id': auth.current_user})
    admin = isAdmin(usuario)
    return {'admin': admin, 'id': auth.current_user}
