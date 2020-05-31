import jwt, json

#criar o token
def encode_auth_token(email, password):
    try:
        payload = {
                    'email': email,
                    'password': password
                }
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
    with open('db/db.json') as arq:
        usuarios = json.load(arq)
    usuario = [ user for user in usuarios if user['email'] == email]
    if len(usuario) > 0 and usuario[0]['password'] == password:
        del usuario[0]['password']
        return usuario[0], encode_auth_token(email, password)
    else:
        return None, ''
