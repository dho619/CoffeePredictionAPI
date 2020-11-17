from flask import jsonify, request
from app import db
from ..models import Users, Profiles, TypeAreas, TypeContacts, DatabaseVersions
from ..services.startDB import starting_DB

def create():
    if not ('TCC_test' in str(db.engine)):
        return jsonify({'message': 'Unauthorized, delete non-test database.'}), 401

    try:
        starting_DB(db, Users, Profiles, TypeAreas, TypeContacts, DatabaseVersions)
        return jsonify({'message': 'Created successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Error when creating the database'}), 400
