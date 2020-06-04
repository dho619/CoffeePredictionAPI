import requests
from .token import token_comum, token_admin
headerComum = token_comum
headerAdmin = token_admin

def test_put_Profile():
    response = requests.put(
                'http://127.0.0.1:5000/profiles/3',
                json = {'description':'Teste atualizado'},
                headers=headerAdmin
            )
    assert response.status_code == 200


def test_put_Users():
    response = requests.put(
                'http://127.0.0.1:5000/users/2',
                json = {'name':'Name atualizado'},
                headers=headerComum
            )
    assert response.status_code == 200

def test_put_Contacts():
    response = requests.put(
                'http://127.0.0.1:5000/contacts/1',
                json = {'description':'Name atualizado'},
                headers=headerComum
            )
    assert response.status_code == 200

def test_put_TypeContacts():
    response = requests.put(
                'http://127.0.0.1:5000/typeContacts/4',
                json = {'description':'Name atualizado'},
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_put_Area():
    response = requests.put(
                'http://127.0.0.1:5000/areas/1',
                json = {'description':'Name atualizado'},
                headers=headerComum
            )
    assert response.status_code == 200

def test_put_TypeArea():
    response = requests.put(
                'http://127.0.0.1:5000/typeAreas/4',
                json = {'description':'Name atualizado'},
                headers=headerAdmin
            )
    assert response.status_code == 200
