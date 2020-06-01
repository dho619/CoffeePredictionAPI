from app import app
from flask import jsonify
from ..resources import Profiles

@app.route('/profiles', methods=['GET'])
def get_profiles():
    return Profiles.get_profiles()

@app.route('/profiles/<id>', methods=['GET'])
def get_profile(id):
    return Profiles.get_profile(id)

@app.route('/profiles', methods=['POST'])
def post_profile():
    return Profiles.post_profile()

@app.route('/profiles/<id>', methods=['PUT'])
def update_profile(id):
    return Profiles.update_profile(id)

@app.route('/profiles/<id>', methods=['DELETE'])
def delete_profile(id):
    return Profiles.delete_profile(id)
