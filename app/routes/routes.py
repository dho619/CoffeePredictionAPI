from app import app
from flask import jsonify
from ..resources import Users

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Hello Word!!!'})

@app.route('/users', methods=['GET'])
def get_users():
    return Users.get_users()

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return Users.get_user(id)

@app.route('/users', methods=['POST'])
def post_user():
    return Users.post_user()

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    return Users.update_user(id)
