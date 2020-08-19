#ROTA PARA CRIACAO DE BANCO PARA TESTE

import requests
from .myToken import token_admin, baseURL

headerAdmin = token_admin

def test_createBank():
    response = requests.post(
                baseURL + 'create_database',
                headers=headerAdmin
            )
    assert response.status_code == 201
