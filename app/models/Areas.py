import datetime

from app import db, ma
from ..utils.generalFunctions import create_guid

class Areas(db.Model):
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    user_id = db.Column(db.String(37), db.ForeignKey('users.id'))
    type_area_id = db.Column(db.String(37), db.ForeignKey('type_areas.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())

    type_area = db.relationship("TypeAreas", back_populates="areas")
    user = db.relationship("Users", back_populates="areas")
    classifications = db.relationship("Classifications", back_populates="area")

    def __init__(self, name, description):
        self.name = name
        self.description = description


class AreaSchema(ma.Schema):
    type_area = ma.Nested('TypeAreaSchema', many=False)
    class Meta:
        fields = ('id', 'name', 'description', 'type_area', 'user_id')

area_schema = AreaSchema()
areas_schema = AreaSchema( many = True )
