from app import app
from ..resources import Profiles
from ..services.auth import auth, is_admin

@app.route('/profiles', methods=['GET'])
@auth.login_required
def get_profiles():
    return Profiles.get_profiles()

@app.route('/profiles/<id>', methods=['GET'])
@auth.login_required
def get_profile(id):
    return Profiles.get_profile(id)

@app.route('/profiles', methods=['POST'])
@auth.login_required
@is_admin
def post_profile():
    return Profiles.post_profile()

@app.route('/profiles/<id>', methods=['PUT'])
@auth.login_required
@is_admin
def update_profile(id):
    return Profiles.update_profile(id)

@app.route('/profiles/<id>', methods=['DELETE'])
@auth.login_required
@is_admin
def delete_profile(id):
    return Profiles.delete_profile(id)
