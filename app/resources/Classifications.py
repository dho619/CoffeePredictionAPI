from flask import request, jsonify
from app import db
from ..models.Classifications import Classifications, classification_schema, classifications_schema
from ..models.Users import Users
from ..models.Areas import Areas

def post_classification():
    #pegando os campos da requisicao
    healthy = request.json['healthy']
    disease = request.json['disease']
    user = Users.query.get(request.json['user_id'])
    area = Areas.query.get(request.json['area_id'])

    classification = Classifications(healthy, disease)
    classification.users = user
    classification.areas = area

    try:
        db.session.add(classification)#adiciona
        db.session.commit()# commit no banco
        result = classification_schema.dump(classification)
        return jsonify({'message': 'Sucessfully registered', 'data': result}), 201
    except Exception as e:
            print(e)
            return jsonify({'message': 'We had an error processing your data, please try again in a few moments', 'data': {}}), 400

def get_classifications():
    classifications = Classifications.query.all()#pega todos classifications

    if classifications:
        result = classifications_schema.dump(classifications)
        return jsonify({"message": "Sucessfully fetched", "data": result}), 201
    return jsonify({"message": "nothing found", "data":{}})

def get_classification(id):
    classification = Classifications.query.get(id)#busca classification pelo id

    if classification:#se existir
        result = classification_schema.dump(classification)
        return jsonify({"message": "Sucessfully fetched", "data": result})
    #se nao existir
    return jsonify({'message': "Classification don't exist", 'data': {}}), 404

def delete_classification(id):
    classification = Classifications.query.get(id)#busca classification pelo id

    if not classification:#se nao existir
        return jsonify({'message': "Classification don't exist", 'data': {}}), 404

    try:
        db.session.delete(classification)
        db.session.commit()
        result = classification_schema.dump(classification)
        return jsonify({"message": "Sucessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "Unable to deleted", "data": {}}), 500
