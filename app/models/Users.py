import datetime
from app import db, ma

from .UsersProfiles import usersProfiles

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    profiles = db.relationship("Profiles", secondary=usersProfiles, back_populates='users')
    classification = db.relationship("Classifications", back_populates="users")

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'name', 'created_at', 'updated_at')

user_schema = UserSchema()
users_schema = UserSchema( many = True )
