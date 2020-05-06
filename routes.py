#importar os Resources
from Resources.Login import Login
from Resources.User import User


def loading_Of_Routes(api):
    api.add_resource(Login, '/login')
    api.add_resource(User, '/users')
