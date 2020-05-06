from flask_httpauth import HTTPTokenAuth
from functools import wraps

from utils.gets import getUsuario, getPerfil
from utils.login import decode_auth_token

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def user_logged(token):
    user = decode_auth_token(token)

    auth.current_user = user['email'] if 'email' in user else ''
    return 'email' in user

#criando um decorador para autentificar se e admin
def is_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        perfil = getPerfil({'email': auth.current_user})
        if perfil == 'admin':
            return f(*args, **kwargs)
        return "Not authorized.", 401
    return wrapper

#funcao para verificar se email passado e o email da pessoa logada
def is_your(email):
    usuario = getUsuario({'email': auth.current_user})
    return usuario and (usuario['perfil'] == 'admin' or usuario['email'] == email)
