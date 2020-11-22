import smtplib

server = smtplib.SMTP('smtp-relay.gmail.com', 25)

server.ehlo()

server.login('')
