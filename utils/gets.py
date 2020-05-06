import json
with open('db/db.json') as arq:
    usuarios = json.load(arq)

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
        result = [usuario for usuario in usuarios if usuario['id'] == id]
    elif 'email' in args:
        result = [usuario for usuario in usuarios if usuario['email'] == args['email'].lower()]

    usuario = result[0] if len(result) > 0 else None

    return usuario

def getPerfil(args):
    usuario = getUsuario(args)
    return usuario['perfil']
