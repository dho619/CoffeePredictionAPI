from app import app
from flask import jsonify
from ..resources import TypeContacts
from ..services.auth import auth, is_admin

@app.route('/typeContacts', methods=['GET'])
@auth.login_required#estar logado
def get_typeContacts():
    return TypeContacts.get_typeContacts()

@app.route('/typeContacts/<id>', methods=['GET'])
@auth.login_required#estar logado
def get_typeContact(id):
    return TypeContacts.get_typeContact(id)

@app.route('/typeContacts', methods=['POST'])
@auth.login_required#estar logado
@is_admin #ser administrador
def post_typeContact():
    return TypeContacts.post_typeContact()

@app.route('/typeContacts/<id>', methods=['PUT'])
@auth.login_required#estar logado
@is_admin #ser administrador
def update_typeContact(id):
    return TypeContacts.update_typeContact(id)

@app.route('/typeContacts/<id>', methods=['DELETE'])
@auth.login_required#estar logado
@is_admin #ser administrador
def delete_typeContact(id):
    return TypeContacts.delete_typeContact(id)