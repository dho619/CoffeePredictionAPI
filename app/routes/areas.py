from app import app
from flask import jsonify
from ..resources import Areas

@app.route('/areas', methods=['GET'])
def get_areas():
    return Areas.get_areas()

@app.route('/areas/<id>', methods=['GET'])
def get_area(id):
    return Areas.get_area(id)

@app.route('/areas', methods=['POST'])
def post_area():
    return Areas.post_area()

@app.route('/areas/<id>', methods=['PUT'])
def update_area(id):
    return Areas.update_area(id)

@app.route('/areas/<id>', methods=['DELETE'])
def delete_area(id):
    return Areas.delete_area(id)
