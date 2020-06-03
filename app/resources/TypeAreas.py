from flask import request, jsonify
from sqlalchemy import exc
from app import db
from ..models.TypeAreas import TypeAreas, typeArea_schema, typeAreas_schema

def post_typeArea():
    #pegando os campos da requisicao
    try:
        name = request.json['name']
        description = request.json['description']
    except:
        return jsonify({'message': 'Expected name and description'}), 400

    typeArea = TypeAreas(name, description)
    try:
        db.session.add(typeArea)#adiciona
        db.session.commit()# commit no banco
        result = typeArea_schema.dump(typeArea)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def update_typeArea(id):
    typeArea = TypeAreas.query.get(id)#procura o typeArea pelo id

    if not typeArea:#se nao existir o typeArea
        return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

    #substitui ou mantem os campos
    typeArea.name = request.json['name'] if 'name' in request.json else typeArea.name
    typeArea.description = request.json['description'] if 'description' in request.json else typeArea.description

    try:
        db.session.commit()
        result = typeArea_schema.dump(typeArea)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 201
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_typeAreas():
    typeAreas = TypeAreas.query.all()#pega todos typeAreas

    if typeAreas:
        result = typeAreas_schema.dump(typeAreas)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 201
    return jsonify({"message": "nothing found", "data":{}})

def get_typeArea(id):
    typeArea = TypeAreas.query.get(id)#busca typeArea pelo id

    if typeArea:#se existir
        result = typeArea_schema.dump(typeArea)
        return jsonify({"message": "Sucessfully fetched", "data": result})
    #se nao existir
    return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

def delete_typeArea(id):
    typeArea = TypeAreas.query.get(id)#busca typeArea pelo id

    if not typeArea:#se nao existir
        return jsonify({'message': "TypeArea don't exist", 'data': {}}), 404

    try:
        db.session.delete(typeArea)
        db.session.commit()
        result = typeArea_schema.dump(typeArea)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
