import datetime
from Api import db, ma

class Classifications(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    healthy = db.Column(db.Boolean, nullable=False)
    disease = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))

    def __init__(self, description, user_id, typeArea_id):
        self.description = description
        self.user_id = user_id
        self.typeArea_id = typeArea_id

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class ClassificationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description', 'user_id', 'typeArea_id')

classification_schema = ClassificationSchema()
classifications_schema = ClassificationSchema( many = True )
