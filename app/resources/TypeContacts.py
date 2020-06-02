from flask import request, jsonify
from app import db
from ..models.TypeContacts import TypeContacts, typeContact_schema, typeContacts_schema

def post_typeContact():
    #pegando os campos da requisicao
    name = request.json['name']
    nickname = request.json['nickname']
    typeContact = TypeContacts(name, nickname)
    try:
        db.session.add(typeContact)#adiciona
        db.session.commit()# commit no banco
        result = typeContact_schema.dump(typeContact)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except Exception as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def update_typeContact(id):
    typeContact = TypeContacts.query.get(id)#procura o typeContact pelo id

    if not typeContact:#se nao existir o typeContact
        return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

    #substitui ou mantem os campos
    typeContact.name = request.json['name'] if 'name' in request.json else typeContact.name
    typeContact.nickname = request.json['nickname'] if 'nickname' in request.json else typeContact.nickname

    try:
        db.session.commit()
        result = typeContact_schema.dump(typeContact)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 201
    except Exception as e:
        if ('Duplicate entry' in e.orig.args[1]):#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_typeContacts():
    typeContacts = TypeContacts.query.all()#pega todos typeContacts

    if typeContacts:
        result = typeContacts_schema.dump(typeContacts)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 201
    return jsonify({"message": "nothing found", "data":{}})

def get_typeContact(id):
    typeContact = TypeContacts.query.get(id)#busca typeContact pelo id

    if typeContact:#se existir
        result = typeContact_schema.dump(typeContact)
        return jsonify({"message": "Sucessfully fetched", "data": result})
    #se nao existir
    return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

def delete_typeContact(id):
    typeContact = TypeContacts.query.get(id)#busca typeContact pelo id

    if not typeContact:#se nao existir
        return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

    try:
        db.session.delete(typeContact)
        db.session.commit()
        result = typeContact_schema.dump(typeContact)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
