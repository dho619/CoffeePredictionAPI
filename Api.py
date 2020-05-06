from flask import Flask, jsonify, request
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from routes import loading_Of_Routes


app = Flask(__name__)#passando a quem pertence a instancia de Flask
app.config.from_object('services.config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)#Criando api

loading_Of_Routes(api)#carregando todas as rotas
from models import Users

#apenas o arquivo principal pode chamar essa funcao
if __name__ == '__main__':
    app.run()
