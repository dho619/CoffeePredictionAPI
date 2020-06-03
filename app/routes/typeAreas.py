from app import app
from flask import jsonify
from ..resources import TypeAreas
from ..services.auth import auth, is_admin

@app.route('/typeAreas', methods=['GET'])
@auth.login_required#estar logado
def get_typeAreas():
    return TypeAreas.get_typeAreas()

@app.route('/typeAreas/<id>', methods=['GET'])
@auth.login_required#estar logado
def get_typeArea(id):
    return TypeAreas.get_typeArea(id)

@app.route('/typeAreas', methods=['POST'])
@auth.login_required#estar logado
@is_admin #ser administrador
def post_typeArea():
    return TypeAreas.post_typeArea()

@app.route('/typeAreas/<id>', methods=['PUT'])
@auth.login_required#estar logado
@is_admin #ser administrador
def update_typeArea(id):
    return TypeAreas.update_typeArea(id)

@app.route('/typeAreas/<id>', methods=['DELETE'])
@auth.login_required#estar logado
@is_admin #ser administrador
def delete_typeArea(id):
    return TypeAreas.delete_typeArea(id)
