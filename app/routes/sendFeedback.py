from app import app
from ..resources import SendFeedback
from ..services.auth import auth

@app.route('/sendFeedback', methods=['POST'])
@auth.login_required
def sendFeedback():
    return SendFeedback.sendFeedback()
