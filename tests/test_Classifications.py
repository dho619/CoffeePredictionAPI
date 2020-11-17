import requests, base64
from .config_tests import token_comum, token_admin, baseURL
from .utils.general_functions import decode_token
headerComum = token_comum
headerAdmin = token_admin

user_id = decode_token(headerComum['Authorization'][7:])['sub']
area_id = requests.get(
            baseURL + 'areas',
            headers=headerAdmin
        ).json()['data'][0]['id']

def test_post_Classifications():
    with open('./tests/img/teste.jpg', "rb") as image_file:
        img_base64 = base64.b64encode(image_file.read())
    response = requests.post(
                baseURL + 'classifications',
                json = {"name": "Teste", "description": "Testando", "image": img_base64, "location": "", "user_id": user_id, "area_id": area_id },
                headers=headerComum
            )
    assert response.status_code == 201
