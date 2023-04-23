import smtplib
import ssl
from email.message import EmailMessage

# Generated password from App Password Gmail 
# qvrewmnqekaqbivl
emailSender = 'hunterpimparatana@gmail.com'
emailPassword = 'qvrewmnqekaqbivl'
# emailPassword = '1966Izzy.'
emailReceiver = 'huntermagicman@live.com'

subject = 'Check out this test :3'
body = 'Hello receiver,\nThis is a email test. I hope this works because this is life or death at this point.\nNothing to serious but anyways, gotta blast\n\nKindly,\nHunter Pimparatana.'

em = EmailMessage()
em['From'] = emailSender
em['To'] = emailReceiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# Will test this at a later time!
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())
