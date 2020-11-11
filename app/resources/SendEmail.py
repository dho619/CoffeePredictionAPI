from app import app
from flask import jsonify, request
from ..services.SendEmail import send_email

def sendEmail():
    data = request.json
    try:
        subject = data['subject']
        message = data['message']
        returnEmail = data['returnEmail']
    except:
        return jsonify({'message': 'Expected subject, message and returnEmail'}), 400

    message = message + '\n\n\nEnviado por: ' + returnEmail

    messageInfo = {
        'subject': subject,
        'message': message,
        'password': app.config['EMAIL_PASS'],
        'from': app.config['EMAIL_FROM'],
        'to': app.config['EMAIL_TO']
    }

    serverInfo = {
        'host': app.config['EMAIL_HOST'],
        'port': app.config['EMAIL_PORT']
    }

    sucess, message = send_email.send(messageInfo,serverInfo)

    if sucess:
        return jsonify({'message': 'Email enviado com sucesso!'}), 201

    else:
        return { 'message': str(message) }, 400
