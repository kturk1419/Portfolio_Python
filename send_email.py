import smtplib, ssl
import os


def send_email(user_email, user_message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'kturk1419@gmail.com'
    password = 'nsxvivkxizgspwdh'
    receiver = 'kturk1419@gmail.com'
    context = ssl.create_default_context()
    message = f"""\
Subject: From Portfolio App Contact Us
This is the message:
{user_message}

This is the email:
{user_email}
"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


