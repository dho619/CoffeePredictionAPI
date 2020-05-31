from app import db, ma
from .UsersProfiles import usersProfiles

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    users = db.relationship("Users", secondary=usersProfiles, back_populates='profiles')

    def __init__(self, name, description):
        self.name = name
        self.description = description

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema( many = True )
