from app import app
from flask import jsonify
from ..resources import TypeContacts

@app.route('/typeContacts', methods=['GET'])
def get_typeContacts():
    return TypeContacts.get_typeContacts()

@app.route('/typeContacts/<id>', methods=['GET'])
def get_typeContact(id):
    return TypeContacts.get_typeContact(id)

@app.route('/typeContacts', methods=['POST'])
def post_typeContact():
    return TypeContacts.post_typeContact()

@app.route('/typeContacts/<id>', methods=['PUT'])
def update_typeContact(id):
    return TypeContacts.update_typeContact(id)

@app.route('/typeContacts/<id>', methods=['DELETE'])
def delete_typeContact(id):
    return TypeContacts.delete_typeContact(id)
