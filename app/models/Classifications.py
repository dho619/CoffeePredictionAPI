import datetime
from app import db, ma
from ..utils.generalFunctions import create_guid

class Classifications(db.Model):
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000))
    image_path = db.Column(db.String(10000))
    location = db.Column(db.String(1000))
    healthy = db.Column(db.Boolean)
    disease = db.Column(db.String(50))
    is_processed = db.Column(db.Boolean, nullable=False, default=False)
    is_sended = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.String(37), db.ForeignKey('users.id'))
    area_id = db.Column(db.String(37), db.ForeignKey('areas.id'))

    user = db.relationship("Users", back_populates="classifications")
    area = db.relationship("Areas", back_populates="classifications")

    def __init__(self, name, description, image_path, location):
        self.name = name
        self.description = description
        self.image_path = image_path
        self.location = location

class ClassificationSchema(ma.Schema):
    area = ma.Nested('AreaSchema', many=False)

    class Meta:
        fields = ( 'id', 'name', 'description', 'image_path', 'location', 'healthy', 'disease', 'area', 'created_at', 'updated_at')

classification_schema = ClassificationSchema()
classifications_schema = ClassificationSchema( many = True )
