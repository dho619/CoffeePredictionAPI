from app import app
from ..resources import DbCreate

@app.route('/create_database', methods=['POST'])
def post_creates():
    return DbCreate.create()
