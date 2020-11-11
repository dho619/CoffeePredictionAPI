from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send(messageInfo, serverInfo):

    if (not messageInfo) or (not serverInfo):
        return False

    try:
        message = MIMEMultipart()

        host = serverInfo['host']
        port = serverInfo['port']
        password = messageInfo['password']
        message['from'] = messageInfo['from']
        message['to'] = messageInfo['to']
        message['subject'] = messageInfo['subject']

        message.attach(MIMEText(messageInfo['message'], 'plain'))

        server = smtplib.SMTP(host, port)

        server.starttls()

        server.login(messageInfo['from'], password)

        server.sendmail(message['from'], message['to'], message.as_string())

        server.quit()

    except Exception as err:
        return False
