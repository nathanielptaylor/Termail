#!/usr/bin/env python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sys
import os

fromAddr = 'nathanielptaylor@gmail.com'


toAddr = raw_input('RECIEVER: ')



    

msg = MIMEMultipart()
msg['From'] = fromAddr
msg['To'] = toAddr
msg['Subject'] = raw_input('SUBJECT:  ')

body = raw_input('BODY:   ')

msg.attach(MIMEText(body, 'plain'))

def preview(msg):
    print(' ')
    print('         START OF PREVIEW:')
    print('')
    print(toAddr)
    print('')
    print(str(msg['Subject']))
    print(' ')
    print(body)
    print('')
    print('         END OF PREVIEW')
    print('')
    confirm = raw_input('Would you like to send? (y/n):  ')
    if confirm == 'y':
        return
    else:
        print('NOT SENT')
        
        os.system('clear')
        import UI

    
preview(msg)


#   connects to server
server = smtplib.SMTP('smtp.gmail.com', 587)
print('SERVER CONNECTION VERIFIED')

server.starttls()
server.login(fromAddr, 'natcatcher')
print('LOGGED IN')
text = msg.as_string()

server.sendmail(fromAddr, toAddr, text)
print('SENT')
server.quit()
os.system('clear')
import UI

