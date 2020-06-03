from app import app
from flask import jsonify
from ..resources import Contacts
from ..services.auth import auth, is_admin

@app.route('/contacts', methods=['GET'])
@auth.login_required#estar logado
@is_admin#ser administrador
def get_contacts():
    return Contacts.get_contacts()

@app.route('/contacts/<id>', methods=['GET'])
@auth.login_required#estar logado
def get_contact(id):
    return Contacts.get_contact(id)

@app.route('/contacts', methods=['POST'])
@auth.login_required#estar logado
def post_contact():
    return Contacts.post_contact()

@app.route('/contacts/<id>', methods=['PUT'])
@auth.login_required#estar logado
def update_contact(id):
    return Contacts.update_contact(id)

@app.route('/contacts/<id>', methods=['DELETE'])
@auth.login_required#estar logado

def delete_contact(id):
    return Contacts.delete_contact(id)
