import os
from dotenv import load_dotenv
import smtplib
import ssl

load_dotenv()


def send(message):
    username = os.environ['SENDER']
    password = os.environ['PASSCODE']

    host = 'smtp.gmail.com'
    port = 465

    receiver = os.environ['RECEIVER']

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user=username, password=password)
        server.sendmail(username, receiver, message)



