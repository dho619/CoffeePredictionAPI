import datetime
from app import db, ma

class Areas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    location = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type_area_id = db.Column(db.Integer, db.ForeignKey('type_areas.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())

    type_area = db.relationship("TypeAreas", back_populates="areas")
    user = db.relationship("Users", back_populates="areas")
    classifications = db.relationship("Classifications", back_populates="area")

    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location


#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class AreaSchema(ma.Schema):
    type_area = ma.Nested('TypeAreaSchema', many=False)
    classifications = ma.Nested('ClassificationSchema', many=True)
    # user = ma.Nested('UserSchema', many=False, exclude=('areas',))

    class Meta:
        fields = ('id', 'name', 'description', 'location', 'typeArea', 'classifications')

area_schema = AreaSchema()
areas_schema = AreaSchema( many = True )
