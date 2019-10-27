import os
import secrets
from flask import url_for
from flask_mail import Message
from cat import mail


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(subject='Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''Reset your password by clicking this link:
{url_for('users.reset_token', token=token, _external=True)}

Cyber Awareness Trivia
'''
    mail.send(msg)