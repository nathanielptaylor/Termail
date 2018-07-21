import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from PIL import Image
import os
import sys

fromAddr = "nathanielptaylor@gmail.com"
toAddr = raw_input('RECIEVER:  ')

msg = MIMEMultipart()

msg['From'] = fromAddr
msg['To'] = toAddr
msg['Subject'] = raw_input('SUBJECT:  ')

body = raw_input('BODY:  ')

filename = raw_input('NAME OF FILE (WITH EXTENSION):  ')

if filename.endswith('.jpg' or '.jpeg' or '.png'):
    openCheck = True
else: 
    openCheck = False

filepath = raw_input('FILEPATH:  ')
attachment = open(filepath, "rb")


"""  
    preview() shows basically a preview of the email. I copied this 
    code from the plainEmail file, but added that it opens the attachement (If it's a photo)
"""

def preview(msg, filepath, openCheck):
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

    #openCheck looks to see if attachment is an image.
    if openCheck == True:
        img = Image.open(filepath)
        img.show()

    confirm = raw_input('Would you like to send? (y/n):  ')
    if confirm == 'y':
        return
    else:
        print('NOT SENT')
        os.system('clear')
        import UI



msg.attach(MIMEText(body, 'plain'))








preview(msg, filepath, openCheck)



part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)




server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

print('SERVER CONNECTION SUCCESSFUL')

server.login(fromAddr, "natcatcher")
print('LOGGED IN')

text = msg.as_string()

server.sendmail(fromAddr, toAddr, text)
print('SENT')

server.quit()
sys.exit()
os.system('clear')

import UI
