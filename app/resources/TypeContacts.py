from flask import request, jsonify
from sqlalchemy import exc
from app import db
from ..models.TypeContacts import TypeContacts, typeContact_schema, typeContacts_schema

def post_typeContact():
    try:
        name = request.json['name']
        description = request.json['description']
    except:
        return jsonify({'message': 'Expected name and description'}), 400
    typeContact = TypeContacts(name, description)
    try:
        db.session.add(typeContact)
        db.session.commit()
        result = typeContact_schema.dump(typeContact)
        return jsonify({'message': 'Sucessfully registered', 'data': result.decode('utf-8')}), 201
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def update_typeContact(id):
    typeContact = TypeContacts.query.get(id)

    if not typeContact:
        return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

    typeContact.name = request.json['name'] if 'name' in request.json else typeContact.name
    typeContact.description = request.json['description'] if 'description' in request.json else typeContact.description

    try:
        db.session.commit()
        result = typeContact_schema.dump(typeContact)
        return jsonify({'message': 'Sucessfully updated', 'data': result.decode('utf-8')}), 200
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_typeContacts():
    typeContacts = TypeContacts.query.all()

    if typeContacts:
        result = typeContacts_schema.dump(typeContacts)
        return jsonify({"message": "Sucessfully fetched", "data": result.decode('utf-8')}), 200
    return jsonify({"message": "nothing found", "data":{}})

def get_typeContact(id):
    typeContact = TypeContacts.query.get(id)

    if typeContact:
        result = typeContact_schema.dump(typeContact)
        return jsonify({"message": "Sucessfully fetched", "data": result.decode('utf-8')})

    return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

def delete_typeContact(id):
    typeContact = TypeContacts.query.get(id)

    if not typeContact:
        return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

    try:
        db.session.delete(typeContact)
        db.session.commit()
        result = typeContact_schema.dump(typeContact)
        return jsonify({"message": "Sucessfully deleted", "data": result.decode('utf-8')}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
