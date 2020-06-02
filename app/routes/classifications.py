from app import app
from flask import jsonify
from ..resources import Classifications

@app.route('/classifications', methods=['GET'])
def get_classifications():
    return Classifications.get_classifications()

@app.route('/classifications/<id>', methods=['GET'])
def get_classification(id):
    return Classifications.get_classification(id)

@app.route('/classifications', methods=['POST'])
def post_classification():
    return Classifications.post_classification()

@app.route('/classifications/<id>', methods=['DELETE'])
def delete_classification(id):
    return Classifications.delete_classification(id)
