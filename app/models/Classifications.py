import datetime
from flask_marshmallow import fields
from sqlalchemy.dialects.mysql import DATETIME
from app import db, ma
from ..utils.generalFunctions import create_guid
import base64

class Classifications(db.Model):
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000))
    image_path = db.Column(db.String(10000))
    location = db.Column(db.String(1000))
    healthy = db.Column(db.Boolean)
    disease = db.Column(db.String(50))
    tokenPush = db.Column(db.String(100))
    is_processed = db.Column(db.Boolean, nullable=False, default=False)
    is_sended = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())
    updated_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())
    user_id = db.Column(db.String(37), db.ForeignKey('users.id'))
    area_id = db.Column(db.String(37), db.ForeignKey('areas.id'))

    user = db.relationship("Users", back_populates="classifications")
    area = db.relationship("Areas", back_populates="classifications")

    def __init__(self, name, description, image_path, location, tokenPush):
        self.name = name
        self.description = description
        self.image_path = image_path
        self.location = location
        self.tokenPush = tokenPush

class ClassificationSchema(ma.Schema):
    def get_imageBase64(self, obj):
        try:
            with open(obj.image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
        except:
            encoded_string = ""
        return encoded_string

    area = ma.Nested('AreaSchema', many=False)
    image_base64 = fields.fields.Method('get_imageBase64')

    class Meta:
        fields = ( 'id', 'name', 'description', 'image_path','image_base64', 'location', 'healthy', 'disease', 'tokenPush', 'area', 'created_at', 'updated_at', 'is_processed', 'is_sended')


classification_schema = ClassificationSchema()
classifications_schema = ClassificationSchema( many = True )
