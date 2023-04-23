import smtplib
import ssl
from email.message import EmailMessage

# THIS HAS NOT BEEN TESTED!
# THIS MAY SEND MULTPLE EMAILS?? 
# HOW CAN I GENERATE NEW STRINGS TO PUT INTO ONE BDDY??
def emailSender(result):
    emailSender = 'hunterpimparatana@gmail.com'
    emailPassword = 'qvrewmnqekaqbivl'
    emailReceiver = 'huntermagicman@live.com'

    subject = 'Check out this test!'
    body = 'Here is the result of your numbers: {}'.format(result)

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

def addition(x, y):
    result = x + y 

    return result

def subtraction(x, y):
    result = x - y 

    return result

x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))

result = addition(x, y)
emailSender(result)

result = subtraction(x, y)
emailSender(result)


