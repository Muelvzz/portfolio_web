import smtplib
import ssl


def send_email(username, message):
    host = "smtp.gmail.com"
    port = 465

    password = "puee ripl zssi hsem"

    receiver = "muelvinlopez25@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
