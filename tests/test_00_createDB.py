import requests
from .token import user, password

def test_createBank():

    response = requests.post(
                'http://127.0.0.1:5000/create_database',
                json = {"user": user, "password": password},
            )
    assert response.status_code == 201
