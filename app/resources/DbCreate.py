from flask import jsonify, request
from app import db
from ..models import Users, Profiles, TypeAreas, TypeContacts
from ..services.startDB import starting_DB

def create():
    try:
        if not ('TCC_test' in str(db.engine)):
            return jsonify({'message': 'Unauthorized, delete non-test database.'}), 401
        user = request.json['user']
        password = request.json['password']

        if not (user == 'dho619' and password == '619dho'):
            return jsonify({'message': 'Unauthorized, admin-only access.'}), 401
    except:
        return jsonify({'message': 'Unauthorized, admin-only access.'}), 401

    try:
        starting_DB(db, Users, Profiles, TypeAreas, TypeContacts)
        return jsonify({'message': 'Created successfully'}), 201
    except:
        return jsonify({'message': 'Error when creating the database'}), 400
