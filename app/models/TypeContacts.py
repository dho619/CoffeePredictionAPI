import datetime
from sqlalchemy.dialects.mysql import DATETIME
from app import db, ma
from ..utils.generalFunctions import create_guid

class TypeContacts(db.Model):
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())
    updated_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())

    contacts = db.relationship("Contacts", back_populates="type_contact")

    def __init__(self, name, description):
        self.name = name
        self.description = description

class TypeContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
        include_fk = True

typeContact_schema = TypeContactSchema()
typeContacts_schema = TypeContactSchema( many = True )
