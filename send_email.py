import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "koolknight.ie@gmail.com"
password = "akkivvkprhtqxhyj"

receiver = "koolknight.ie@gamil.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)