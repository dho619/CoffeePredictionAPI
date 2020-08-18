#TESTE DE DELECAO DE REGISTROS

import requests
from .myToken import token_comum, token_admin, baseURL
headerComum = token_comum
headerAdmin = token_admin

def test_delete_Profiles():
    response = requests.delete(
                baseURL + 'profiles/3',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_delete_Users():
    response = requests.delete(
                baseURL + 'users/3',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_delete_Contacts():
    response = requests.delete(
                baseURL + 'contacts/1',
                headers=headerComum
            )
    assert response.status_code == 200


def test_delete_TypeContacts():
    response = requests.delete(
                baseURL + 'typeContacts/4',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_delete_Classifications():
    response = requests.delete(
                baseURL + 'classifications/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_delete_Areas():
    response = requests.delete(
        baseURL + 'areas/1',
        headers=headerComum
    )
    assert response.status_code == 200

def test_delete_TypeAreas():
    response = requests.delete(
        baseURL + 'typeAreas/4',
        headers=headerAdmin
    )
    assert response.status_code == 200
