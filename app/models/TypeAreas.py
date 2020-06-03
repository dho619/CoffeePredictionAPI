import datetime
from app import db, ma

class TypeAreas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())

    areas = db.relationship("Areas", back_populates="type_area")

    def __init__(self, name, description):
        self.name = name
        self.description = description

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class TypeAreaSchema(ma.Schema):
    # areas = ma.Nested('AreaSchema', many=True, exclude=('type_area',))
    class Meta:
        fields = ('id', 'name', 'description')

typeArea_schema = TypeAreaSchema()
typeAreas_schema = TypeAreaSchema( many = True )
