from app import db, ma
from .TypeContacts import TypeContactSchema
from .Users import UserSchema

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    typeContact_id = db.Column(db.Integer, db.ForeignKey('type_contacts.id'))
    users = db.relationship("Users", back_populates="contacts")
    type_contacts = db.relationship("TypeContacts", back_populates="contacts")

    def __init__(self, description):
        self.description = description

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class ContactSchema(ma.Schema):
    type_contacts = ma.Nested(TypeContactSchema)
    users = ma.Nested(UserSchema)
    class Meta:
        fields = ('id', 'name', 'users', 'type_contacts' )

contact_schema = ContactSchema()
contacts_schema = ContactSchema( many = True )
