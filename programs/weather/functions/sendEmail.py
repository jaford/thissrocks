import smtplib
import time
import logging
from email.message import EmailMessage

def sendMail(dataList):
    emailSender = 'hoonterpymailtest@gmail.com'
    emailPassword = 'cxcvdtzhtnogsust'
    emailReceiver = 'hunterpimparatana@gmail.com'

    subject = 'Check out this test!'
    mailSigniture = '\nKindly,\nHunter Pimparatana.\nEmail: hunterpimparatana@gmail.com\nMobile: (505)-918-4031'
    body ='\nHere is a example on how to display data onto a string. Here is test to put into this string.\nThis is one way I can fomat data into a email so I can send it to user & myself!\nCompiled data:\t{}\n{}\n'.format(dataList, mailSigniture)

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())

    return