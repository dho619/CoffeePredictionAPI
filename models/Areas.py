import datetime
from Api import db, ma

class Areas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    location = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    typeArea_id = db.Column(db.Integer, db.ForeignKey('typeAreas.id'))

    def __init__(self, name, description, location, user_id, typeArea_id):
        self.name = name
        self.description = description
        self.location = location
        self.user_id = user_id
        self.typeArea_id = typeArea_id

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class AreaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'location', 'user_id', 'typeArea_id')

area_schema = AreaSchema()
areas_schema = AreaSchema( many = True )
