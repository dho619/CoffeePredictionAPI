from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import sys
from .services.startDB import starting_DB

app = Flask(__name__)
app.config.from_object('config_app')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .models import Users, Profiles, TypeContacts, Contacts, TypeAreas, Areas, DatabaseVersions
from .routes import routes

if len(sys.argv) > 1 and sys.argv[1].lower() == 'create_db':
    #passa tudo com paramentro, para evitar import circular
    starting_DB(db, Users, Profiles, TypeAreas, TypeContacts, DatabaseVersions)
    sys.exit()

if __name__ == '__main__':
    app.run()
