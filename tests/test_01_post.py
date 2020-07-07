import requests
from .token import token_comum, token_admin
headerComum = token_comum
headerAdmin = token_admin

def test_post_Profile():
    response = requests.post(
                'http://127.0.0.1:5000/profiles',
                json = {'name':'teste', 'description':'Teste'},
                headers=headerAdmin
            )
    assert response.status_code == 201

def test_post_Users():
    response = requests.post(
                'http://127.0.0.1:5000/users',
                json = {'name':'teste', 'email':'teste@teste.com', 'password': '123'}
            )
    assert response.status_code == 201

def test_post_TypeContacts():
    response = requests.post(
                'http://127.0.0.1:5000/typeContacts',
                json = {'name':'teste', 'description':'Teste'},
                headers=headerAdmin
            )
    assert response.status_code == 201


def test_post_TypeAreas():
    response = requests.post(
                'http://127.0.0.1:5000/typeAreas',
                json = {'name':'teste', 'description':'Teste'},
                headers=headerAdmin
            )
    assert response.status_code == 201

def test_post_Contacts():
    response = requests.post(
                'http://127.0.0.1:5000/contacts',
                json = {"contact": "35998398509","description": "Meu Xiaomi Redmi", "type_contact_id": 1, "user_id": 2},
                headers=headerComum
            )
    assert response.status_code == 201

def test_post_Area():
    response = requests.post(
                'http://127.0.0.1:5000/areas',
                json = {"name": "Minha Chacara 2", 	"description": "Essa é minha chacara que eu comprei com meu money", "location": "12349994499", 	"user_id": 2, "type_area_id": 1 },
                headers=headerComum
            )
    assert response.status_code == 201

def test_post_Classifications():
    response = requests.post(
                'http://127.0.0.1:5000/classifications',
                json = {"name": "Teste", "description": "Testando", "healthy": False, "disease": "Doença X", 	"user_id": 2, "area_id": 1 },
                headers=headerComum
            )
    assert response.status_code == 201
