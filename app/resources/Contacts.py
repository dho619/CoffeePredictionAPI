from flask import request, jsonify
from sqlalchemy import exc
from app import db
from ..models.Contacts import Contacts, contact_schema, contacts_schema
from ..models.TypeContacts import TypeContacts
from ..models.Users import Users
from ..services.auth import is_your

def post_contact():
    try:
        contact = request.json['contact']
        description = request.json['description']
        type_contact_id = request.json['type_contact_id']
        user_id = request.json['user_id']
        typeContact = TypeContacts.query.get(request.json['type_contact_id'])
        user = Users.query.get(request.json['user_id'])
    except Exception as e:
        return jsonify({'message': 'Expected contact, description, type_contact_id and user_id'}), 400

    if not user or not typeContact:
        return jsonify({'message': 'type_contact_id or user_id does not exist'}), 400

    if not is_your(user.id):
        return jsonify({'message': "Unauthorized action."}), 401

    contact = Contacts(contact, description)
    contact.type_contact = typeContact
    contact.user = user
    try:
        db.session.add(contact)
        db.session.commit()
        result = contact_schema.dump(contact)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:
            return jsonify({'message': 'This contact is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def update_contact(id):
    contact = Contacts.query.get(id)

    if not contact:
        return jsonify({'message': "Contact don't exist", 'data': {}}), 404

    if not is_your(contact.user_id):
        return jsonify({'message': "Unauthorized action."}), 401

    if 'type_contact_id' in request.json:
        typeContact = TypeContacts.query.get(request.json['type_contact_id'])


    contact.description = request.json['description'] if 'description' in request.json else contact.description
    contact.type_contact = typeContacts.query.get(request.json['type_contact_id']) if 'type_contact_id' in request.json else contact.type_contact

    try:
        db.session.commit()
        result = contact_schema.dump(contact)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 200
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:
            return jsonify({'message': 'This contact is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400



def get_contacts():
    contacts = Contacts.query.all()

    if contacts:
        result = contacts_schema.dump(contacts)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 200
    return jsonify({"message": "nothing found", "data":{}})

def get_contact(id):
    contact = Contacts.query.get(id)

    if contact:
        if not is_your(contact.user_id):
            return jsonify({'message': "Unauthorized action."}), 401
        result = contact_schema.dump(contact)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 200
    #se nao existir
    return jsonify({'message': "Contact don't exist", 'data': {}}), 404

def delete_contact(id):
    contact = Contacts.query.get(id)
    '''
    resgata o typeContact, pois estava gerando bug que um fk (o typeContact) tava
    desatualizado(o que estava em cache) com o do banco, apenas tras para ele atualizar
    '''
    typeContact = TypeContacts.query.get(contact.type_contact_id)

    if not contact:
        return jsonify({'message': "Contact don't exist", 'data': {}}), 404

    if not is_your(contact.user_id):
        return jsonify({'message': "Unauthorized action."}), 401

    try:
        db.session.delete(contact)
        db.session.commit()
        result = contact_schema.dump(contact)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
