import smtplib
import time
import logging
from tabulate import tabulate
import pandas as pd
from email.message import EmailMessage

def sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel):
    emailSender = 'hoonterpymailtest@gmail.com'
    emailPassword = 'cxcvdtzhtnogsust'
    emailReceiver = 'hunterpimparatana@gmail.com'

    subject = 'Check out this test!'
    mailSigniture = '\nKindly,\nHunter Pimparatana.\nEmail: hunterpimparatana@gmail.com\nMobile: (505)-918-4031'
    headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
    headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
    headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']

    # NEED TO CHECK HOW and WHY THESE isinstance IS NOT WORKING!
    print('CHECK 1')
    if isinstance((currentHour, dayForcast, hourForcast), pd.DataFrame):
        print('CHECK 2')
        fForcast = str(tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid'))
        cForcast = str(tabulate(currentHour, headers = headerCurrentHour, tablefmt = 'fancy_grid'))
        hForcast = str(tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid'))
        body = 'Here is your data:\nTemps in fahrenheit\n{}\n{}\n{}\n'.format(currentHour, dayForcast, hourForcast)
        print(body)
        if (dayForcastCe and hourForcastCel and currentHourCel) == None:
            print('User did not convert data to fahrenheit.\n')
    else:
        print('This data has not been added: \n{}\n{}\n{}'.format(dayForcastCel, hourForcastCel, currentHourCel))
    if isinstance((currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel), pd.DataFrame):
        fForcast = str(tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid'))
        cForcast = str(tabulate(currentHour, headers = headerCurrentHour, tablefmt = 'fancy_grid'))
        hForcast = str(tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid'))
        fForcastConv = tabulate(dayForcastCel, headers = headerForcastDay, tablefmt = 'fancy_grid')
        cForcastConv = tabulate(currentHourCel, headers = headerCurrentHour, tablefmt = 'fancy_grid')
        hForcastConv = tabulate(hourForcastCel, headers = headerForcastHour, tablefmt = 'fancy_grid')
        body = 'Here is your data:\nTemps in fahrenheit\n{}\n{}\n{}\nTemps in celsius:\n{}\n{}\n{}\n'.format(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel)
        print(body)
    else:
        print('Something went very wrong: ')


    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)

    # This bellow actually sends the message. The rest contains it into a string and objects to send in said email.
    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #     smtp.login(emailSender, emailPassword)
    #     smtp.sendmail(emailSender, emailReceiver, em.as_string())

    return