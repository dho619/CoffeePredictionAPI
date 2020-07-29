import requests
from .token import token_comum, token_admin, baseURL
headerComum = token_comum
headerAdmin = token_admin
def test_get_Profiles():
    response = requests.get(
                baseURL + 'profiles',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Profile():
    response = requests.get(
                baseURL + 'profiles/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Users():
    response = requests.get(
                baseURL + 'users',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_get_User():
    response = requests.get(
                baseURL + 'users/2',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Contacts():
    response = requests.get(
                baseURL + 'contacts',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_get_Contact():
    response = requests.get(
                baseURL + 'contacts/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_TypeContacts():
    response = requests.get(
                baseURL + 'typeContacts',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_TypeContact():
    response = requests.get(
                baseURL + 'typeContacts/4',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_TypeAreas():
    response = requests.get(
                baseURL + 'typeAreas',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_TypeArea():
    response = requests.get(
                baseURL + 'typeAreas/4',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Areas():
    response = requests.get(
                baseURL + 'areas',
                headers=headerAdmin
            )
    assert response.status_code == 201

def test_get_Area():
    response = requests.get(
                baseURL + 'areas/1',
                headers=headerComum
            )
    assert response.status_code == 200

def test_get_Classifications():
    response = requests.get(
                baseURL + 'classifications',
                headers=headerAdmin
            )
    assert response.status_code == 200

def test_get_Classification():
    response = requests.get(
                baseURL + 'classifications/1',
                headers=headerComum
            )
    assert response.status_code == 200
