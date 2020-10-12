# import requests, base64
# from PIL import Image
# from .config_tests import token_comum, token_admin, baseURL
# headerComum = token_comum
# headerAdmin = token_admin
#
# def test_post_Classifications():
#     img = Image.open('./tests/img/teste.jpg')
#     img_base64 = base64.b64encode(img.tobytes())
#     image = base64.b64decode(img_base64)
#     response = requests.post(
#                 baseURL + 'classifications',
#                 json = {"name": "Teste", "description": "Testando", "image": img_base64, 	"user_id": 2, "area_id": 1 },
#                 headers=headerComum
#             )
#     assert response.status_code == 201
#
# def test_put_Classifications():
#     response = requests.put(
#                 baseURL + 'classifications/1',
#                 json = {'name':'Name atualizado'},
#                 headers=headerComum
#             )
#     assert response.status_code == 200
#
# def test_get_Classifications():
#     response = requests.get(
#                 baseURL + 'classifications',
#                 headers=headerAdmin
#             )
#     assert response.status_code == 200
#
# def test_get_Classification():
#     response = requests.get(
#                 baseURL + 'classifications/1',
#                 headers=headerComum
#             )
#     assert response.status_code == 200
