from app import db, ma

class TypeAreas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100))
    areas = db.relationship("Areas", back_populates="type_areas")

    def __init__(self, name, description):
        self.name = name
        self.description = description

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class TypeAreaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')

typeArea_schema = TypeAreaSchema()
typeAreas_schema = TypeAreaSchema( many = True )
