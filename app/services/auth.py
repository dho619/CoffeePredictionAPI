from flask_httpauth import HTTPTokenAuth
from functools import wraps

from utils.gets import getUsuario, getPerfis
from utils.login import decode_auth_token

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def user_logged(token):
    user = decode_auth_token(token)

    auth.current_user = user['id'] if 'id' in user else ''
    return 'id' in user

#criando um decorador para autentificar se e admin
def is_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        perfis= getPerfis({'id': auth.current_user})
        if 'admin' in perfis:
            return f(*args, **kwargs)
        return "Not authorized.", 401
    return wrapper

#funcao para verificar se id passado e o id da pessoa logada
def is_your(id):
    usuario = getUsuario({'id': auth.current_user})
    return usuario and ('admin' in usuario['perfis'] or usuario['id'] == id)
