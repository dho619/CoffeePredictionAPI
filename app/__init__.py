from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from flask_executor import Executor
import sys
from .services.startDB import starting_DB

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
seeder = FlaskSeeder()
seeder.init_app(app, db)

runsInTheBackground = Executor(app) #trabalhar background em processos demorados

from .models import Users, Profiles, TypeContacts, Contacts, TypeAreas, Areas, Classifications
from .resources import Users
from .routes import routes

if len(sys.argv) > 1 and sys.argv[1].lower() == 'create_db':
    #passa tudo com paramentro, para evitar import circular
    starting_DB(db, Users, Profiles, TypeAreas, TypeContacts)
    sys.exit()

if __name__ == '__main__':
    app.run()
