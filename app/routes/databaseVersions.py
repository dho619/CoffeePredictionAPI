from app import app
from ..resources import DatabaseVersions

@app.route('/versions', methods=['GET'])
def get_versions():
    return DatabaseVersions.get_versions()

@app.route('/version/<name>', methods=['GET'])
def get_version(name):
    return DatabaseVersions.get_version(name)
