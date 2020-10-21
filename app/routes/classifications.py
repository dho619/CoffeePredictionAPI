from app import app
from ..resources import Classifications
from ..services.auth import auth, is_admin

@app.route('/classifications', methods=['GET'])
@auth.login_required
def get_classifications():
    return Classifications.get_classifications()

@app.route('/classifications/<id>', methods=['GET'])
@auth.login_required
def get_classification(id):
    return Classifications.get_classification(id)

@app.route('/classifications', methods=['POST'])
@auth.login_required
def post_classification():
    return Classifications.post_classification()

@app.route('/classifications/<id>', methods=['PUT'])
@auth.login_required
def put_classification(id):
    return Classifications.put_classification(id)

@app.route('/classifications/<id>', methods=['DELETE'])
@auth.login_required
def delete_classification(id):
    return Classifications.delete_classification(id)
