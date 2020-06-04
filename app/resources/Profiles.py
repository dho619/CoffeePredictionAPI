from flask import request, jsonify
from sqlalchemy import exc
from app import db
from ..models.Profiles import Profiles, profile_schema, profiles_schema

def post_profile():
    #pegando os campos da requisicao
    try:
        name = request.json['name']
        description = request.json['description']
    except:
        return jsonify({'message': 'Expected name and description'}), 400


    profile = Profiles(name, description)
    try:
        db.session.add(profile)#adiciona
        db.session.commit()# commit no banco
        result = profile_schema.dump(profile)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def update_profile(id):
    profile = Profiles.query.get(id)#procura o profile pelo id

    if not profile:#se nao existir o profile
        return jsonify({'message': "Profile don't exist", 'data': {}}), 404

    #substitui ou mantem os campos
    profile.name = request.json['name'] if 'name' in request.json else profile.name
    profile.description = request.json['description'] if 'description' in request.json else profile.description

    try:
        db.session.commit()
        result = profile_schema.dump(profile)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 200
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e.orig.args[1]:#se isso for true, significa que teve duplicida e nesse caso so pode ser o name
            return jsonify({'message': 'This name is already in use', 'data': {}}), 406
        else:
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_profiles():
    profiles = Profiles.query.all()#pega todos profiles

    if profiles:
        result = profiles_schema.dump(profiles)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 200
    return jsonify({"message": "nothing found", "data":{}})

def get_profile(id):
    profile = Profiles.query.get(id)#busca profile pelo id

    if profile:#se existir
        result = profile_schema.dump(profile)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 200
    #se nao existir
    return jsonify({'message': "Profile don't exist", 'data': {}}), 404

def delete_profile(id):
    profile = Profiles.query.get(id)#busca profile pelo id

    if not profile:#se nao existir
        return jsonify({'message': "Profile don't exist", 'data': {}}), 404

    try:
        db.session.delete(profile)
        db.session.commit()
        result = profile_schema.dump(profile)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
