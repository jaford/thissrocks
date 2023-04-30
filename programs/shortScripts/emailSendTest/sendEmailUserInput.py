import smtplib
import ssl
from email.message import EmailMessage

def sendMail(dataList):
    emailSender = 'hunterpimparatana@gmail.com'
    emailPassword = 'qvrewmnqekaqbivl'
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

def stringResultBody(restultDict):
    if isinstance(restultDict, dict):
        keyList = list(restultDict.keys())
        valueList = list(restultDict.values())
        dataList = []
        for i, v in restultDict.items():
            dataList.append((i, v))

    return dataList

def math(x, y):
    resultAdd = x + y 
    resultSub = x - y 
    resultMulti = x * y 
    resultDiv = x / y 

    return resultAdd, resultSub, resultMulti, resultDiv


x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))
resultAdd, resultSub, resultMulti, resultDiv = math(x, y)

restultDict = {}
restultDict['Addition']         = str(resultAdd)
restultDict['Subtraction']      = str(resultSub)
restultDict['Multiplcation']    = str(resultMulti)
restultDict['Division']         = str(resultDiv)

dataList = stringResultBody(restultDict)
sendMail(dataList)