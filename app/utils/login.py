import jwt, json
from werkzeug.security import check_password_hash
from datetime import datetime
from flask import jsonify
from app import app
from ..models.Users import Users, user_schema
from .gets import isAdmin

#criar o token
def encode_auth_token(user):
    try:
        payload = {
            #'exp': datetime.now() + timedelta(days=3), #valido por tres dias
            'iat': datetime.now(), #data de criacao
            'sub': user.id,
            'admin': isAdmin(user),
            'name': user.name,
            'email': user.email
        }
        return jwt.encode(
            payload,
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
    except Exception as e:
        # print(e)
        return None

#Transformar o token e dicionario denovo
def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config['SECRET_KEY'])
        return payload
    except Exception as e:
        return None

#Faz as validações de usuario e retorna o token
def login_Usuario(user_email, password):
    user_email = user_email.lower()
    try:
        user = Users.query.filter_by(email=user_email).first()
    except Exception as e:
        user = None
    print(type(user))
    if user and check_password_hash(user.password, password):
        return encode_auth_token(user)
    else:
        return None
