from ..models.Users import Users

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
        user = Users.query.filter_by(email=args['email']).first()#busca usuario pelo email

    return result

def isAdmin(user):
    admin = [profile for profile in user.profiles if profile.name == 'admin']#adiciona se for perfil admin
    return len(admin) > 0
