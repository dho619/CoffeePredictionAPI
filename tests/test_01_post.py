#TESTE DE CRIACAO DE REGISTROS NAS TABELAS
#menos de classifications

import requests, base64
from PIL import Image
from .myToken import token_comum, token_admin, baseURL
headerComum = token_comum
headerAdmin = token_admin

def test_post_Profile():
    response = requests.post(
                baseURL + 'profiles',
                json = {'name':'teste', 'description':'Teste'},
                headers=headerAdmin
            )
    assert response.status_code == 201

def test_post_Users():
    response = requests.post(
                baseURL + 'users',
                json = {'name':'teste', 'email':'teste@teste.com', 'password': '123'}
            )
    assert response.status_code == 201

def test_post_TypeContacts():
    response = requests.post(
                baseURL + 'typeContacts',
                json = {'name':'teste', 'description':'Teste'},
                headers=headerAdmin
            )
    assert response.status_code == 201


def test_post_TypeAreas():
    response = requests.post(
                baseURL + 'typeAreas',
                json = {'name':'teste', 'description':'Teste'},
                headers=headerAdmin
            )
    assert response.status_code == 201

def test_post_Contacts():
    response = requests.post(
                baseURL + 'contacts',
                json = {"contact": "35998398509","description": "Meu Xiaomi Redmi", "type_contact_id": 1, "user_id": 2},
                headers=headerComum
            )
    assert response.status_code == 201

def test_post_Area():
    response = requests.post(
                baseURL + 'areas',
                json = {"name": "Minha Chacara 2", 	"description": "Essa é minha chacara que eu comprei com meu money", "location": "12349994499", 	"user_id": 2, "type_area_id": 1 },
                headers=headerComum
            )
    assert response.status_code == 201
