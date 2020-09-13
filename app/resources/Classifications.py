from flask import request, jsonify
from os import urandom, fork
from app import db, runsInTheBackground
from ..models.Classifications import Classifications, classification_schema, classifications_schema
from ..models.Users import Users
from ..models.Areas import Areas
from ..services.auth import is_your
from ..utils.classifications import classificationImage

def post_classification():
    #pegando os campos da requisicao
    try:
        name = request.json['name']
        description = request.json['description']
        imageBase64 = request.json['image']
        user = Users.query.get(request.json['user_id'])
        area = Areas.query.get(request.json['area_id'])
    except:
        return jsonify({'message': 'Expected name, description, image, user_id and area_id'}), 400

    if not user or not area:
        return jsonify({'message': 'area_id or user_id does not exist'}), 400

    if not is_your(user.id):
        return jsonify({'message': "Unauthorized action."}), 401

    image = urandom(1)#imageBase64
    healthy = 0
    disease = 'Análise'
    classification = Classifications(name, description, image, healthy, disease)
    classification.user = user
    classification.area = area

    try:
        db.session.add(classification)
        db.session.commit()
        result = classification_schema.dump(classification)
        runsInTheBackground.submit(classificationImage, imageBase64, result['id'])
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except Exception as e:
            print(e)
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400


def put_classification(id):
    classification = Classifications.query.get(id)

    if not classification:
        return jsonify({'message': "Classification don't exist", 'data': {}}), 404

    classification.name = request.json['name'] if 'name' in request.json else classification.name
    classification.description = prequest.json['description'] if 'description' in request.json else classification.description

    if not is_your(classification.user_id):
        return jsonify({'message': "Unauthorized action."}), 401

    try:
        db.session.commit()
        result = classification_schema.dump(classification)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 200
    except:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400


def get_classifications():
    classifications = Classifications.query.all()

    if classifications:
        result = classifications_schema.dump(classifications)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 200
    return jsonify({"message": "nothing found", "data":{}})

def get_classification(id):
    classification = Classifications.query.get(id)
    if classification:
        if not is_your(classification.user_id):
            return jsonify({'message': "Unauthorized action."}), 401

        result = classification_schema.dump(classification)
        return jsonify({"message": "Sucessfully fetched", "data": result}),200

    return jsonify({'message': "Classification don't exist", 'data': {}}), 404

def delete_classification(id):
    classification = Classifications.query.get(id)

    if not classification:
        return jsonify({'message': "Classification don't exist", 'data': {}}), 404

    if not is_your(classification.user_id):
        return jsonify({'message': "Unauthorized action."}), 401

    try:
        db.session.delete(classification)
        db.session.commit()
        result = classification_schema.dump(classification)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
