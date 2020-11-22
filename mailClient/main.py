### ONLY TEXT ###


import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Insert Title...'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Insert Message...')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


### ONLY TEXT END ###



### WITH ATTACHMENTS ###


import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Insert Title...'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Insert Message...')

files = ['img1.jpg', 'img2.png']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image',
                       subtype=file_type, filename=file_name)


### IF PDF FILE ###


files = ['file.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

        msg.add_attachement(file_data, maintype='application',
                            subtype='octet-stream', filename=file_name)


### IF PDF FILE END ###


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


### WITH ATTACHMENTS END ###



### SEND TO MULTIPLE PEOPLE ###


import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['target@gmail.com', 'target2@hotmail.com']

msg = EmailMessage()
msg['Subject'] = 'Insert Title...'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Insert Message...')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


### SEND TO MULTIPLE PEOPLE END ###



### WITH HTML ###

import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Insert Title...'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('This is a plain text email')

msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:#0F0;">This is an HTML Email!</h1>
        </body>
    </html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


### WITH HTML END ###