import json
from app import db

def getUsuario(args):
    if not('id' in args or 'email' in args):
        return None

    result = []

    #filtrando de acordo se for id ou email
    if 'id' in args:
        try:
            id = int(args['id'])
        except:
            return None
        result = Users.query.get(id)#busca usuario pelo id
    elif 'email' in args:
        result = Users.query.get(id)#busca usuario pelo email

    return result

def getPerfis(args):
    usuario = getUsuario(args)
    return usuario['perfil']
