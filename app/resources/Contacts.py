from flask import request, jsonify
from app import db
from ..models.Contacts import Contacts, contact_schema, contacts_schema
from ..models.TypeContacts import TypeContacts
from ..models.Users import Users

def post_contact():
    #pegando os campos da requisicao
    description = request.json['description']
    typeContact_id = request.json['typeContact_id']
    user_id = request.json['user_id']
    typeContact = TypeContacts.query.get(request.json['typeContact_id'])
    user = Users.query.get(request.json['user_id'])

    contact = Contacts(description)
    contact.type_contacts = typeContact
    contact.users = user
    try:
        db.session.add(contact)#adiciona
        db.session.commit()# commit no banco
        result = contact_schema.dump(contact)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except Exception as e:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def update_contact(id):
    contact = Contacts.query.get(id)#procura o contact pelo id

    if not contact:#se nao existir o contact
        return jsonify({'message': "Contact don't exist", 'data': {}}), 404

    if 'typeContact_id' in request.json:
        typeContact = TypeContacts.query.get(request.json['typeContact_id'])


    #substitui ou mantem os campos
    contact.description = request.json['description'] if 'description' in request.json else contact.description
    contact.type_contacts = typeContacts.query.get(request.json['typeContact_id']) if 'typeContact_id' in request.json else contact.type_contacts

    try:
        db.session.commit()
        result = contact_schema.dump(contact)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 201
    except Exception as e:
        if ('Duplicate entry' in e.orig.args[1]):#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_contacts():
    contacts = Contacts.query.all()#pega todos contacts

    if contacts:
        result = contacts_schema.dump(contacts)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 201
    return jsonify({"message": "nothing found", "data":{}})

def get_contact(id):
    contact = Contacts.query.get(id)#busca contact pelo id

    if contact:#se existir
        result = contact_schema.dump(contact)
        return jsonify({"message": "Sucessfully fetched", "data": result})
    #se nao existir
    return jsonify({'message': "Contact don't exist", 'data': {}}), 404

def delete_contact(id):
    contact = Contacts.query.get(id)#busca contact pelo id

    if not contact:#se nao existir
        return jsonify({'message': "Contact don't exist", 'data': {}}), 404

    try:
        db.session.delete(contact)
        db.session.commit()
        result = contact_schema.dump(contact)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
