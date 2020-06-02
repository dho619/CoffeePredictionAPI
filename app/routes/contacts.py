from app import app
from flask import jsonify
from ..resources import Contacts

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return Contacts.get_contacts()

@app.route('/contacts/<id>', methods=['GET'])
def get_contact(id):
    return Contacts.get_contact(id)

@app.route('/contacts', methods=['POST'])
def post_contact():
    return Contacts.post_contact()

@app.route('/contacts/<id>', methods=['PUT'])
def update_contact(id):
    return Contacts.update_contact(id)

@app.route('/contacts/<id>', methods=['DELETE'])
def delete_contact(id):
    return Contacts.delete_contact(id)
