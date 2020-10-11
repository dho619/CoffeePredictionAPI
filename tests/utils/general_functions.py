import jwt
from ..config_tests import SECRET_KEY

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY)
        return payload
    except Exception as e:
        return None
