from flask import jsonify
from flask_httpauth import HTTPTokenAuth
from functools import wraps
from ..utils.login import decode_auth_token
from ..utils.gets import get_user_by_email_or_id, get_profile_by_user

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def user_logged(token):
    user = decode_auth_token(token)
    if not user:
        return False
    try:
        auth.current_user = user['sub']
        return True
    except:
        return False


def is_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if get_profile_by_user(get_user_by_email_or_id({'id': auth.current_user})) == 'admin':
            return f(*args, **kwargs)
        return jsonify({'message': "Unauthorized, admin-only access."}), 401
    return wrapper


def is_your(id):
    if id == None:
        return False
    user = get_user_by_email_or_id({'id': auth.current_user})
    isAdmin = get_profile_by_user(user) == 'admin'
    return user and (isAdmin or user.id == id)

def token_user():
    user = get_user_by_email_or_id({'id': auth.current_user})
    isAdmin = get_profile_by_user(user) == 'admin'
    return {'admin': isAdmin, 'id': auth.current_user}
