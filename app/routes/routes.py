from app import app
from flask import jsonify
from ..resources import Users

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Hello Word!!!'})

@app.route('/users', methods=['POST'])
def post_user():
    return Users.post_user()
