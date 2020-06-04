import requests
from .token import token_comum, token_admin
headerComum = token_comum
headerAdmin = token_admin
def test_get_Profiles():
    response = requests.get(
                'http://127.0.0.1:5000/profiles',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Profile():
    response = requests.get(
                'http://127.0.0.1:5000/profiles/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Users():
    response = requests.get(
                'http://127.0.0.1:5000/users',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_get_User():
    response = requests.get(
                'http://127.0.0.1:5000/users/2',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Contacts():
    response = requests.get(
                'http://127.0.0.1:5000/contacts',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_get_Contact():
    response = requests.get(
                'http://127.0.0.1:5000/contacts/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_TypeContacts():
    response = requests.get(
                'http://127.0.0.1:5000/typeContacts',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_TypeContact():
    response = requests.get(
                'http://127.0.0.1:5000/typeContacts/4',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_TypeAreas():
    response = requests.get(
                'http://127.0.0.1:5000/typeAreas',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_TypeAreas():
    response = requests.get(
                'http://127.0.0.1:5000/typeAreas/4',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Areas():
    response = requests.get(
                'http://127.0.0.1:5000/areas',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_get_Areas():
    response = requests.get(
                'http://127.0.0.1:5000/areas/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Classification():
    response = requests.get(
                'http://127.0.0.1:5000/classifications',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_get_Classification():
    response = requests.get(
                'http://127.0.0.1:5000/classifications/1',
                headers=headerComum
            )
    assert response.status_code == 200
