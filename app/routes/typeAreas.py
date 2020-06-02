from app import app
from flask import jsonify
from ..resources import TypeAreas

@app.route('/typeAreas', methods=['GET'])
def get_typeAreas():
    return TypeAreas.get_typeAreas()

@app.route('/typeAreas/<id>', methods=['GET'])
def get_typeArea(id):
    return TypeAreas.get_typeArea(id)

@app.route('/typeAreas', methods=['POST'])
def post_typeArea():
    return TypeAreas.post_typeArea()

@app.route('/typeAreas/<id>', methods=['PUT'])
def update_typeArea(id):
    return TypeAreas.update_typeArea(id)

@app.route('/typeAreas/<id>', methods=['DELETE'])
def delete_typeArea(id):
    return TypeAreas.delete_typeArea(id)
