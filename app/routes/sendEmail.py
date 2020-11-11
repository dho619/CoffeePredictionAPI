from app import app
from ..resources import SendEmail
from ..services.auth import auth

@app.route('/sendEmail', methods=['POST'])
@auth.login_required
def sendEmail():
    return SendEmail.sendEmail()
