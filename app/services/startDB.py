from werkzeug.security import generate_password_hash

def starting_DB(db, Users, Profiles, TypeAreas, TypeContacts):
    print('..| Criando banco...')
    db.drop_all()
    db.create_all()
    print('..| Banco Criado!')
    print('..| Populando banco...')
    create_profiles(db, Profiles)
    create_users(db, Users, Profiles)
    create_typeArea(db, TypeAreas)
    create_typeContacts(db, TypeContacts)
    print('..| Banco Pronto para uso!')

def create_profiles(db, Profiles):
    admin = Profiles.Profiles('admin', 'Admnistrador')
    comum = Profiles.Profiles('user', 'Usuario')
    db.session.add_all([admin, comum])
    db.session.commit()

def create_users(db, Users, Profiles):
    admin = Users.Users('admin@admin.com', generate_password_hash('123'), 'admin')
    comum = Users.Users('comum@comum.com', generate_password_hash('123'), 'comum')
    profileAdmin = Profiles.Profiles.query.filter_by(name = 'admin').first()
    profileUser = Profiles.Profiles.query.filter_by(name = 'user').first()
    admin.profile = profileAdmin
    comum.profile = profileUser
    db.session.add_all([admin, comum])
    db.session.commit()

def create_typeArea(db, TypeAreas):
    chacara = TypeAreas.TypeAreas('chacara', 'Chácara')
    fazenda = TypeAreas.TypeAreas('fazenda', 'Fazenda')
    lote = TypeAreas.TypeAreas('lote', 'Lote')
    rancho = TypeAreas.TypeAreas('rancho', 'Rancho')
    sitio = TypeAreas.TypeAreas('sitio', 'Sítio')
    outro = TypeAreas.TypeAreas('outro', 'Outro')
    db.session.add_all([chacara, fazenda, lote, rancho, sitio, outro])
    db.session.commit()

def create_typeContacts(db, TypeContacts):
    celular = TypeContacts.TypeContacts('cel', 'Celular')
    telefone = TypeContacts.TypeContacts('tel', 'Telefone')
    email = TypeContacts.TypeContacts('email', 'Email')
    outro = TypeContacts.TypeContacts('outro', 'Outro')
    db.session.add_all([celular, telefone, outro])
    db.session.commit()
