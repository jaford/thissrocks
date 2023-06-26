import smtplib
import time
import logging
from tabulate import tabulate
import pandas as pd
from email.message import EmailMessage
from .lineRemove import deleteLastLine

# def sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel):
def sendMail(hForcast, fForcast, cForcast, cForcastConv, fForcastConv, hForcastConv):
    # Need to put these isinstance into one argument? Last time it gave an error. Unsure why. 
    headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
    headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
    headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']

    body = '\nHere is your data:\n\nTemps in fahrenheit\n{}\n{}\n{}\nTemps in celsius:\n{}\n{}\n{}\n'.format(cForcast, fForcast, hForcast, cForcastConv, fForcastConv, hForcastConv)

    emailSender = input('Enter the senders email: ').lower()
    emailPassword = input('Enter the senders email password: ')
    emailReceiver = input('Enter the receivers email: ').lower()
    lineAmount = len(userInput.splitlines()) + 2
    deleteLastLine(lineAmount)

    # This is hard coded for now! Code above has no use at the moment but is there! 
    emailSender = 'hoonterpymailtest@gmail.com'
    emailPassword = 'cxcvdtzhtnogsust'
    emailReceiver = 'hunterpimparatana@gmail.com'

    subject = 'Check out this test!'
    mailSigniture = '\nKindly,\nHunter Pimparatana.\nEmail: hunterpimparatana@gmail.com\nMobile: (505)-918-4031'
    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)

    # This bellow actually sends the message. The rest contains it into a string and objects to send in email.
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())

    return body