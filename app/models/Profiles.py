import datetime

from app import db, ma
from .UsersProfiles import usersProfiles
from ..utils.guid import create_guid

class Profiles(db.Model):
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())

    users = db.relationship("Users", secondary=usersProfiles, back_populates='profiles')

    def __init__(self, name, description):
        self.name = name
        self.description = description

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class ProfileSchema(ma.Schema):
    # users = ma.Nested('UserSchema', many=True, exclude=('profiles',))

    class Meta:
        fields = ('id', 'name', 'description')

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema( many = True )
