import datetime
from sqlalchemy.dialects.mysql import DATETIME
from app import db, ma
from ..utils.generalFunctions import create_guid

class Profiles(db.Model):
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())
    updated_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())

    users = db.relationship("Users", back_populates='profile')

    def __init__(self, name, description):
        self.name = name
        self.description = description

class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema( many = True )
