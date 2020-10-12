import datetime

from app import db, ma
from ..utils.generalFunctions import create_guid

class Users(db.Model):
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)
    profile_id = db.Column(db.String(37), db.ForeignKey('profiles.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())

    profile = db.relationship("Profiles", back_populates='users')
    classifications = db.relationship("Classifications", back_populates="user")
    areas = db.relationship("Areas", back_populates="user")
    contacts = db.relationship("Contacts", back_populates="user")

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

class UserSchema(ma.Schema):
    profile = ma.Nested('ProfileSchema')
    areas = ma.Nested('AreaSchema', many=True)
    contacts = ma.Nested('ContactSchema', many=True)
    class Meta:
        fields = ('id', 'email', 'name', 'created_at', 'updated_at', 'profile', 'areas', 'contacts')

user_schema = UserSchema()
users_schema = UserSchema( many = True )
