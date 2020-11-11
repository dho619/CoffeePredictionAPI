from app import app, executor
from flask import jsonify, request
from ..services.SendEmail import send_email
from ..utils.login import decode_auth_token

def sendFeedback():
    data = request.json
    try:
        subject = data['subject']
        message = data['message']
        returnEmail = data['returnEmail']
    except:
        return jsonify({'message': 'Expected subject, message and returnEmail'}), 400

    user = decode_auth_token(request.headers['Authorization'][7:])

    infoUser = '\n\n\n Enviado por: '
    infoUser = infoUser + '\n Id: ' + user['sub']
    infoUser = infoUser + '\n Nome: ' + user['name']
    infoUser = infoUser + '\n Email: ' + returnEmail

    message = message + infoUser

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

    try:
        #executa em background
        executor.submit(send_email.send, messageInfo, serverInfo)
        return jsonify({'message': 'Feedback encaminhado com sucesso!'}), 201
    except:
        return { 'message': 'Erro ao enviar Feedback' }, 400
