from app import app
from flask import jsonify
from ..resources import Areas
from ..services.auth import auth, is_admin

@app.route('/areas', methods=['GET'])
@auth.login_required#estar logado
def get_areas():
    return Areas.get_areas()

@app.route('/areas/<id>', methods=['GET'])
@auth.login_required#estar logado
def get_area(id):
    return Areas.get_area(id)

@app.route('/areas', methods=['POST'])
@auth.login_required#estar logado
def post_area():
    return Areas.post_area()

@app.route('/areas/<id>', methods=['PUT'])
@auth.login_required#estar logado
def update_area(id):
    return Areas.update_area(id)

@app.route('/areas/<id>', methods=['DELETE'])
@auth.login_required#estar logado
def delete_area(id):
    return Areas.delete_area(id)
