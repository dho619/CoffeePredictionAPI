from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

def conectarDbMysql(app):
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    return db, ma
