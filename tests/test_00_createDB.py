#ROTA PARA CRIACAO DE BANCO PARA TESTE

import requests
from .myToken import user, password, baseURL

def test_createBank():

    response = requests.post(
                baseURL + 'create_database',
                json = {"user": user, "password": password},
            )
    assert response.status_code == 201
