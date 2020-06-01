import jwt, json
from werkzeug.security import check_password_hash


#criar o token
def encode_auth_token(user):
    try:
        payload = user
        return jwt.encode(
            payload,
            'SENHA_MUITO_DIFICIL',
            algorithm='HS256'
        )
    except Exception as e:
        print(e)

#Transformar o token e dicionario denovo
def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, 'SENHA_MUITO_DIFICIL')
        return payload
    except Exception as e:
        print(e)
        return {}

#Faz as validações de usuario e retorna o token
def login_Usuario(email, password):
    email = email.lower()

    user = db.query.get(email)
    if user and check_password_hash(user['password'], password):
        return user, encode_auth_token(user)
    else:
        return None, ''
