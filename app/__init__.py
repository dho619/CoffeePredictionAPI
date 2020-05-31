from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

#importando models
from .models import Users, Profiles, TypeContacts, Contacts, TypeAreas, Areas, Classification
#importando resources
from .resources import Users
#importando rotas
from .routes import routes

if __name__ == '__main__':
    app.run()
