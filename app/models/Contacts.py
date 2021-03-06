import datetime
from sqlalchemy.dialects.mysql import DATETIME
from app import db, ma
from ..utils.generalFunctions import create_guid

class Contacts(db.Model):
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    user_id = db.Column(db.String(37), db.ForeignKey('users.id'))
    type_contact_id = db.Column(db.String(37), db.ForeignKey('type_contacts.id'))
    created_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())
    updated_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())

    user = db.relationship("Users", back_populates="contacts")
    type_contact = db.relationship("TypeContacts", back_populates="contacts")

    def __init__(self, contact, description):
        self.contact = contact
        self.description = description

class ContactSchema(ma.Schema):
    type_contact = ma.Nested('TypeContactSchema')
    class Meta:
        fields = ('id','contact', 'description', 'user_id', 'type_contact')

contact_schema = ContactSchema()
contacts_schema = ContactSchema( many = True )
