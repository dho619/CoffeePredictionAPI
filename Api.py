from flask import Flask, jsonify, request
from flask_restful import Api
from routes import loading_Of_Routes


app = Flask(__name__)#passando a quem pertence a instancia de Flask
app.config.from_object('services.config')
api = Api(app)#Criando api

loading_Of_Routes(api)#carregando todas as rotas

#apenas o arquivo principal pode chamar essa funcao
if __name__ == '__main__':
    app.run()
