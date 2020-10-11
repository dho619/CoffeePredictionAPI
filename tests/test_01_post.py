#TESTE DE CRIACAO DE REGISTROS NAS TABELAS
#menos de classifications

import requests
from .config_tests import token_comum, token_admin, baseURL
headerComum = token_comum
headerAdmin = token_admin

def test_post_Users():
    response = requests.post(
                baseURL + 'users',
                json = {'name':'teste', 'email':'teste@teste.com', 'password': '123'}
            )
    assert response.status_code == 201

def test_post_Contacts():
    response = requests.post(
                baseURL + 'contacts',
                json = {"contact": "35998398509","description": "Meu Xiaomi Redmi", "type_contact_id": 1, "user_id": 2},
                headers=headerComum
            )
    assert response.status_code == 201
