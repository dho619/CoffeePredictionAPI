from app import db, ma

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    typeContact_id = db.Column(db.Integer, db.ForeignKey('type_contacts.id'))
    type_contacts = db.relationship("TypeContacts", back_populates="contacts")

    def __init__(self, description, user_id, typeContact_id):
        self.description = description
        self.user_id = user_id
        self.typeContact_id = typeContact_id

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class ContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'user_id','typeContact_id')

contact_schema = ContactSchema()
contacts_schema = ContactSchema( many = True )
