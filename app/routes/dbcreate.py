from app import app
from ..services.auth import auth, is_admin
from ..resources import DbCreate

@app.route('/create_database', methods=['POST'])
@auth.login_required
@is_admin
def post_creates():
    return DbCreate.create()
