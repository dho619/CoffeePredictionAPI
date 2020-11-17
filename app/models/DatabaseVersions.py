import datetime
from sqlalchemy.dialects.mysql import DATETIME
from app import db, ma
from ..utils.generalFunctions import create_guid

class DatabaseVersions(db.Model):
    id = db.Column(db.String(37), primary_key=True, default=create_guid, unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    version = db.Column(db.String(20), nullable=False, default='1.0.0')
    description = db.Column(db.String(500))
    created_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())
    updated_at = db.Column(DATETIME(fsp=6), default=datetime.datetime.now())

    def __init__(self, name, version, description):
        self.name = name
        self.version = version
        self.description = description

class DatabaseVersionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'version', 'description')
        include_fk = True

databaseVersion_schema = DatabaseVersionSchema()
databaseVersions_schema = DatabaseVersionSchema( many = True )
