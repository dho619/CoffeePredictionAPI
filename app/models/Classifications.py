import datetime
from app import db, ma

class Classifications(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000))
    image = db.Column(db.LargeBinary)
    healthy = db.Column(db.Boolean, nullable=False)
    disease = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))

    user = db.relationship("Users", back_populates="classifications")
    area = db.relationship("Areas", back_populates="classifications")

    def __init__(self, name, description, image, healthy, disease):
        self.name = name
        self.description = description
        self.image = image
        self.healthy = healthy
        self.disease = disease

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class ClassificationSchema(ma.Schema):
    # user = ma.Nested('UserSchema', many=False, exclude=('classifications',))
    area = ma.Nested('AreaSchema', many=False, exclude=('classifications',))

    class Meta:
        fields = ( 'area', 'id', 'name', 'description', 'healthy', 'disease', 'created_at')

classification_schema = ClassificationSchema()
classifications_schema = ClassificationSchema( many = True )
