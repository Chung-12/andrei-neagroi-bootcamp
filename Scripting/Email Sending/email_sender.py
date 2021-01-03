import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Ivo Vukman'
email['to'] = 'ivo.vukman@gmx.net'
email['subject'] = 'You won 1 000 000 euro'

email.set_content(html.substitute(name = 'TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() 
    smtp.login('vkmivo@gmail.com', 'speedlink1600')
    smtp.send_message(email)
    print('all good bois')