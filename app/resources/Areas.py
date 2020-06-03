from flask import request, jsonify
from sqlalchemy import exc
from app import db
from ..models.Areas import Areas, area_schema, areas_schema
from ..models.Users import Users
from ..models.TypeAreas import TypeAreas
from ..services.auth import is_your


def post_area():
    #pegando os campos da requisicao
    try:
        name = request.json['name']
        description = request.json['description']
        location = request.json['location']
        user = Users.query.get(request.json['user_id'])
        type_area = TypeAreas.query.get(request.json['type_area_id'])
    except:
        return jsonify({'message': 'Expected name, description, location, user_id and type_area_id'}), 400

    if not user or not type_area:
        return jsonify({'message': 'type_area_id or user_id does not exist'}), 400

    area = Areas(name, description, location)
    area.type_area = type_area
    area.user = user
    try:
        db.session.add(area)#adiciona
        db.session.commit()# commit no banco
        result = area_schema.dump(area)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400


def update_area(id):
    area = Areas.query.get(id)#procura o area pelo id

    if not area:#se nao existir o area
        return jsonify({'message': "Profile don't exist", 'data': {}}), 404

    if not is_your(area.user_id):
        return jsonify({'message': "Unauthorized action."}), 401

    #substitui ou mantem os campos
    area.name = request.json['name'] if 'name' in request.json else area.name
    area.description = request.json['description'] if 'description' in request.json else area.description
    area.location = request.json['location'] if 'location' in request.json else area.location
    area.type_area = TypeAreas.query.get(request.json['type_area_id']) if 'type_area_id' in request.json else area.type_area

    try:
        db.session.commit()
        result = area_schema.dump(area)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 201
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_areas():
    areas = Areas.query.all()#pega todos areas

    if areas:
        result = areas_schema.dump(areas)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 201
    return jsonify({"message": "nothing found", "data":{}})

def get_area(id):
    area = Areas.query.get(id)#busca area pelo id

    if area:#se existir
        if not is_your(area.user_id):
            return jsonify({'message': "Unauthorized action."}), 401
        result = area_schema.dump(area)
        return jsonify({"message": "Sucessfully fetched", "data": result})
    #se nao existir
    return jsonify({'message': "Profile don't exist", 'data': {}}), 404

def delete_area(id):
    area = Areas.query.get(id)#busca area pelo id

    if not area:#se nao existir
        return jsonify({'message': "Profile don't exist", 'data': {}}), 404

    if not is_your(area.user_id):
        return jsonify({'message': "Unauthorized action."}), 401

    try:
        db.session.delete(area)
        db.session.commit()
        result = area_schema.dump(area)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500