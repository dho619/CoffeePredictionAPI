# import requests
# from .config_tests import token_comum, token_admin, baseURL
# headerComum = token_comum
# headerAdmin = token_admin
# def test_get_Profiles():
#     response = requests.get(
#                 baseURL + 'profiles',
#                 headers=headerComum
#             )
#     assert response.status_code == 200
#
# def test_get_Profile():
#     response = requests.get(
#                 baseURL + 'profiles/1',
#                 headers=headerComum
#             )
#     assert response.status_code == 200
#
# def test_get_Users():
#     response = requests.get(
#                 baseURL + 'users',
#                 headers=headerAdmin
#             )
#     assert response.status_code == 200
#
# def test_get_User():
#     response = requests.get(
#                 baseURL + 'users/2',
#                 headers=headerComum
#             )
#     assert response.status_code == 200
#
# def test_get_Contacts():
#     response = requests.get(
#                 baseURL + 'contacts',
#                 headers=headerAdmin
#             )
#     assert response.status_code == 200
#
# def test_get_Contact():
#     response = requests.get(
#                 baseURL + 'contacts/1',
#                 headers=headerComum
#             )
#     assert response.status_code == 200
