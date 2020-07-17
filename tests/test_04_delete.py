import requests
from .token import token_comum, token_admin
headerComum = token_comum
headerAdmin = token_admin

def test_delete_Profiles():
    response = requests.delete(
                'http://127.0.0.1:5000/profiles/3',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_delete_Users():
    response = requests.delete(
                'http://127.0.0.1:5000/users/3',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_delete_Contacts():
    response = requests.delete(
                'http://127.0.0.1:5000/contacts/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_delete_Areas():
    response = requests.delete(
                'http://127.0.0.1:5000/areas/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_delete_TypeAreas():
    response = requests.delete(
                'http://127.0.0.1:5000/typeAreas/4',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_delete_TypeContacts():
    response = requests.delete(
                'http://127.0.0.1:5000/typeContacts/4',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_delete_Classifications():
    response = requests.delete(
                'http://127.0.0.1:5000/classifications/1',
                headers=headerComum
            )
    assert response.status_code == 200
