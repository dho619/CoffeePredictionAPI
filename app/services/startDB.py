from werkzeug.security import generate_password_hash

def starting_DB(db, Users, Profiles, TypeAreas, TypeContacts):
    print('..| Criando banco...')
    db.drop_all()
    db.create_all()
    print('..| Banco Criado!')
    print('..| Populando banco...')
    # create_profiles(db, Profiles)
    # create_users(db, Users, Profiles)
    # create_typeArea(db, TypeAreas)
    # create_typeContacts(db, TypeContacts)
    print('..| Banco Pronto para uso!')

def create_profiles(db, Profiles):
    admin = Profiles.Profiles('admin', 'Admnistrador')
    comum = Profiles.Profiles('comum', 'Comum')
    db.session.add_all([admin, comum])
    db.session.commit()

def create_users(db, Users, Profiles):
    admin = Users.Users('admin@admin.com', generate_password_hash('123'), 'admin')
    comum = Users.Users('comum@comum.com', generate_password_hash('123'), 'comum')
    profile = Profiles.Profiles.query.get(1) #buscando perfil admin
    admin.profiles.append(profile) #adicionando perfil admin
    profile = Profiles.Profiles.query.get(2) #buscando perfil comum
    comum.profiles.append(profile) #adicionando perfil comum
    db.session.add_all([admin, comum])
    db.session.commit()

def create_typeArea(db, TypeAreas):
    chacara = TypeAreas.TypeAreas('chacara', 'Chácara')
    fazenda = TypeAreas.TypeAreas('fazenda', 'Fazenda')
    sitio = TypeAreas.TypeAreas('sitio', 'Sítio')
    db.session.add_all([chacara, fazenda, sitio])
    db.session.commit()

def create_typeContacts(db, TypeContacts):
    celular = TypeContacts.TypeContacts('cel', 'Celular')
    telefone = TypeContacts.TypeContacts('tel', 'Telefone')
    email = TypeContacts.TypeContacts('email', 'Email')
    db.session.add_all([celular, telefone, email])
    db.session.commit()
