import jwt, json
from werkzeug.security import check_password_hash
from datetime import datetime
from flask import jsonify
from app import app
from ..models.Users import Users, user_schema
from ..utils.gets import get_profile_by_user

def encode_auth_token(user):
    try:
        print(get_profile_by_user(user))
        payload = {
            #'exp': datetime.now() + timedelta(days=3), #valido por tres dias
            'iat': datetime.now(),
            'sub': user.id,
            'admin': get_profile_by_user(user) == 'admin',
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

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config['SECRET_KEY'])
        return payload
    except Exception as e:
        return None

def login_Usuario(user_email, password):
    user_email = user_email.lower()
    try:
        user = Users.query.filter_by(email=user_email).first()
    except Exception as e:
        user = None
    if user and check_password_hash(user.password, password):
        return encode_auth_token(user)
    else:
        return None
