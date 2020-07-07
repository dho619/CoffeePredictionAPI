from app import app
from flask import jsonify
from ..resources import Classifications
from ..services.auth import auth, is_admin

@app.route('/classifications', methods=['GET'])
@auth.login_required#estar logado
@is_admin#ser administrador
def get_classifications():
    return Classifications.get_classifications()

@app.route('/classifications/<id>', methods=['GET'])
@auth.login_required#estar logado
def get_classification(id):
    return Classifications.get_classification(id)

@app.route('/classifications', methods=['POST'])
@auth.login_required#estar logado
def post_classification():
    return Classifications.post_classification()

@app.route('/classifications/<id>', methods=['PUT'])
@auth.login_required#estar logado
def put_classification(id):
    return Classifications.put_classification(id)

@app.route('/classifications/<id>', methods=['DELETE'])
@auth.login_required#estar logado
def delete_classification(id):
    return Classifications.delete_classification(id)
