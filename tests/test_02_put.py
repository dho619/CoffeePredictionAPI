import requests
from .token import token_comum, token_admin, baseURL
headerComum = token_comum
headerAdmin = token_admin

def test_put_Profile():
    response = requests.put(
                baseURL + 'profiles/3',
                json = {'description':'Teste atualizado'},
                headers=headerAdmin
            )
    assert response.status_code == 200


def test_put_Users():
    response = requests.put(
                baseURL + 'users/2',
                json = {'name':'Name atualizado'},
                headers=headerComum
            )
    assert response.status_code == 200

def test_put_Contacts():
    response = requests.put(
                baseURL + 'contacts/1',
                json = {'description':'Name atualizado'},
                headers=headerComum
            )
    assert response.status_code == 200

def test_put_TypeContacts():
    response = requests.put(
                baseURL + 'typeContacts/4',
                json = {'description':'Name atualizado'},
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_put_Area():
    response = requests.put(
                baseURL + 'areas/1',
                json = {'description':'Name atualizado'},
                headers=headerComum
            )
    assert response.status_code == 200

def test_put_TypeArea():
    response = requests.put(
                baseURL + 'typeAreas/4',
                json = {'description':'Name atualizado'},
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_put_Classifications():
    response = requests.put(
                baseURL + 'classifications/1',
                json = {'name':'Name atualizado'},
                headers=headerComum
            )
    assert response.status_code == 200
