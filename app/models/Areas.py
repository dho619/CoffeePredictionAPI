from app import db, ma

class Areas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(100))
    location = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    typeArea_id = db.Column(db.Integer, db.ForeignKey('type_areas.id'))
    type_areas = db.relationship("TypeAreas", back_populates="areas")
    users = db.relationship("Users", back_populates="areas")
    classification = db.relationship("Classifications", back_populates="areas")

    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location


#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class AreaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'location', 'user_id', 'typeArea_id')

area_schema = AreaSchema()
areas_schema = AreaSchema( many = True )
