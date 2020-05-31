from Api import db, ma

class TypeContacts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    nickname = db.Column(db.String(100), nullable=False)
    contacts = db.relationship("Contacts", back_populates="type_contacts")

    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class TypeContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'nickname')

typeContact_schema = TypeContactSchema()
typeContacts_schema = TypeContactSchema( many = True )
