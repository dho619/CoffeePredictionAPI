from flask import request, jsonify
from app import db
from ..models.Areas import Areas, area_schema, areas_schema
from ..models.Users import Users
from ..models.TypeAreas import TypeAreas

def post_area():
    #pegando os campos da requisicao
    name = request.json['name']
    description = request.json['description']
    location = request.json['location']
    user = Users.query.get(request.json['user_id'])
    type_area = TypeAreas.query.get(request.json['typeArea_id'])

    area = Areas(name, description, location)
    area.type_areas = type_area
    area.users = user
    try:
        db.session.add(area)#adiciona
        db.session.commit()# commit no banco
        result = area_schema.dump(area)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except Exception as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def update_area(id):
    area = Areas.query.get(id)#procura o area pelo id

    if not area:#se nao existir o area
        return jsonify({'message': "Profile don't exist", 'data': {}}), 404

    #substitui ou mantem os campos
    area.name = request.json['name'] if 'name' in request.json else area.name
    area.description = request.json['description'] if 'description' in request.json else area.description
    area.location = request.json['location'] if 'location' in request.json else area.location
    area.type_areas = TypeAreas.query.get(request.json['typeArea_id']) if 'typeArea_id' in request.json else area.type_areas

    try:
        db.session.commit()
        result = area_schema.dump(area)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 201
    except Exception as e:
        if ('orig' in e) and ('Duplicate entry' in e.orig.args[1]):#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
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
        result = area_schema.dump(area)
        return jsonify({"message": "Sucessfully fetched", "data": result})
    #se nao existir
    return jsonify({'message': "Profile don't exist", 'data': {}}), 404

def delete_area(id):
    area = Areas.query.get(id)#busca area pelo id

    if not area:#se nao existir
        return jsonify({'message': "Profile don't exist", 'data': {}}), 404

    try:
        db.session.delete(area)
        db.session.commit()
        result = area_schema.dump(area)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
