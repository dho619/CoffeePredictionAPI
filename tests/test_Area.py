import requests
from .config_tests import token_comum, token_admin, baseURL
from .utils.general_functions import decode_token
headerComum = token_comum
headerAdmin = token_admin

area_id = ''
user_id = decode_token(headerComum['Authorization'][7:])['sub']
type_area_id = requests.get(
            baseURL + 'typeAreas',
            headers=headerAdmin
        ).json()['data'][0]['id']

def test_post_Area_01():
    response = requests.post(
                baseURL + 'areas',
                json = {"name": "Minha Chacara", 	"description": "Essa é minha chacara que eu comprei com meu money", "location": "12349994499", 	"user_id": user_id, "type_area_id": type_area_id },
                headers=headerComum
            )
    area_id = response.json()['data']
    assert response.status_code == 201

def test_post_Area_02():
    response = requests.post(
                baseURL + 'areas',
                json = {"name": "Minha Chacara", 	"description": "Essa é minha chacara que eu comprei com meu money", "location": "12349994499" },
                headers=headerComum
            )

    assert response.status_code == 400

def test_post_Area_03():
    response = requests.post(
                baseURL + 'areas',
                json = {"name": "Minha Chacara", 	"description": "Essa é minha chacara que eu comprei com meu money", "location": "12349994499", 	"user_id": user_id, "type_area_id": type_area_id },
                headers={"Authorization": "asdsa"}
            )
    assert response.status_code == 401

# def test_put_Area_01():
#     response = requests.put(
#                 baseURL + 'areas/'+area_id,
#                 json = {'description':'Name atualizado'},
#                 headers=headerComum
#             )
#     print(response.text)
#     print(area_id)
#     assert response.status_code == 200

# def test_put_Area_02():
#     response = requests.put(
#                 baseURL + 'areas/'+area_id,
#                 json = {'description':'Name atualizado'},
#                 headers=headerComum
#             )
#     assert response.status_code == 200
#
# def test_put_Area_03():
#     response = requests.put(
#                 baseURL + 'areas/'+area_id,
#                 json = {'description':'Name atualizado'},
#                 headers={"Authorization": "asdsa"}
#             )
#     assert response.status_code == 401


# def test_get_Areas_01():
#     response = requests.get(
#                 baseURL + 'areas',
#                 headers=headerAdmin
#             )
#     assert response.status_code == 201
#
# def test_get_Area_01():
#     response = requests.get(
#                 baseURL + 'areas/1',
#                 headers=headerComum
#             )
#     assert response.status_code == 200
#
# def test_get_Areas_02():
#     response = requests.get(
#                 baseURL + 'areas',
#                 headers=headerComum
#             )
#     assert response.status_code == 401
#
# def test_get_Area_02():
#     response = requests.get(
#                 baseURL + 'areas/1',
#                 headers='sdasdas'
#             )
#     assert response.status_code == 401
#
# def test_delete_Areas_01():
#     response = requests.delete(
#     baseURL + 'areas/1',
#     headers='sadasdas'
#     )
#     assert response.status_code == 401
#
# def test_delete_Areas_02():
#     response = requests.delete(
#         baseURL + 'areas/1',
#         headers=headerComum
#     )
#     assert response.status_code == 200
