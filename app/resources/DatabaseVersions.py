from flask import jsonify, request
from ..models.DatabaseVersions import DatabaseVersions, databaseVersion_schema, databaseVersions_schema

def get_versions():
    try:
        versions = DatabaseVersions.query.all()

        if versions:
            result = databaseVersions_schema.dump(versions)
            return jsonify({"message": "Sucessfully fetched", "data": result}), 200
        return jsonify({"message": "nothing found", "data":{}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_version(name):
    try:
        version = DatabaseVersions.query.filter_by(name=name).first()

        if version:
            result = databaseVersion_schema.dump(version)
            return jsonify({"message": "Sucessfully fetched", "data": result}), 200
        return jsonify({"message": "nothing found", "data":{}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
