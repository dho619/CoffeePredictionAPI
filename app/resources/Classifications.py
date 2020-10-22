from flask import request, jsonify
from os import urandom
from app import db
from ..models.Classifications import Classifications, classification_schema, classifications_schema
from ..models.Users import Users
from ..models.Areas import Areas
from ..services.auth import is_your, token_user
from ..utils.generalFunctions import save_image

def post_classification():
    id = ""
    try:
        name = request.json['name']
        description = request.json['description']
        imageBase64 = request.json['image']
        user = Users.query.get(request.json['user_id'])
        area = Areas.query.get(request.json['area_id'])

        if 'id' in request.json:
            id = request.json['id']
    except:
        return jsonify({'message': 'Expected name, description, image, user_id and area_id'}), 400

    if not user or not area:
        return jsonify({'message': 'area_id or user_id does not exist'}), 400

    if not is_your(user.id):
        return jsonify({'message': "Unauthorized action."}), 401

    image_path, error = save_image(imageBase64, user.id)

    if error:
        return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

    classification = Classifications(name, description, image_path)
    classification.user = user
    classification.area = area

    if id != "":
        classification.id = id

    classification.is_processed = False
    classification.is_sended = True

    try:
        db.session.add(classification)
        db.session.commit()
        result = classification_schema.dump(classification)
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
    loggedUser = token_user()
    classifications = Classifications.query.filter_by(user_id=loggedUser['id']).order_by(Classifications.created_at.desc())
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
