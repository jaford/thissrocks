import smtplib
import ssl
from email.message import EmailMessage

def stringResult(restultDict):
    emailSender = 'hoonterpymailtest@gmail.com'
    emailPassword = 'cxcvdtzhtnogsust'
    emailReceiver = 'hunterpimparatana@gmail.com'

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


    if isinstance(restultDict, dict):
        print('\nHere is the results of your calculations bellow:\n')
        for i, v in restultDict.items():
            print(i + '\t', v)

    body ='\nHere is a example on how to display data onto a string. Here is test to put into this string.\nThis is one way I can fomat data into a email so I can send it to user & myself!\n'
    print(body)
    
    return

def math(x, y):
    resultAdd = x + y 
    resultSub = x - y 
    resultMulti = x * y 
    resultDiv = x / y 

    return resultAdd, resultSub, resultMulti, resultDiv


x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))
resultAdd, resultSub, resultMulti, resultDiv = math(x, y)

restultList = []
restultDict = {}
restultDict['Addition']         = resultAdd
restultDict['Subtraction']      = resultSub
restultDict['Multiplcation']    = resultMulti
restultDict['Division']         = resultDiv