import smtplib, ssl

host = 'smtp.gmail.com'
port = 465

username = 'kturk1419@gmail.com'
password = 'nsxvivkxizgspwdh'

receiver = 'kturk1419@gmail.com'
context = ssl.create_default_context()

message = """\
Subject: Helloooooooooo
How are you everyone ??????

Goodbye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)