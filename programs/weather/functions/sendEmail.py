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

    try:
        # NEED TO CHECK HOW and WHY THESE isinstance IS NOT WORKING!
        print('CHECK 1')
        if isinstance(currentHour, pd.DataFrame):
            print('CHECK 4')
            cForcast = str(tabulate(currentHour, headers = headerCurrentHour, tablefmt = 'fancy_grid'))
            if isinstance(dayForcast, pd.DataFrame):
                print('CHECK 3')
                fForcast = str(tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid'))
                if isinstance(hourForcast, pd.DataFrame):
                    print('CHECK 2')
                    hForcast = str(tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid'))
                    body = 'Here is your data:\nTemps in fahrenheit\n{}\n{}\n{}\n'.format(cForcast, hForcast, fForcast)
                    # For Testing
                    print(body)
        if isinstance(currentHourCel, pd.DataFrame):
            cForcastConv = tabulate(currentHourCel, headers = headerCurrentHour, tablefmt = 'fancy_grid')
            print('CHECK 1 FOR CEL')
            if isinstance(dayForcastCel, pd.DataFrame):
                fForcastConv = tabulate(dayForcastCel, headers = headerForcastDay, tablefmt = 'fancy_grid')
                print('CHECK 2 FOR CEL')
                if isinstance(hourForcastCel, pd.DataFrame):
                    hForcastConv = tabulate(hourForcastCel, headers = headerForcastHour, tablefmt = 'fancy_grid')
                    print('CHECK 3 FOR CEL')
                    body = 'Here is your data:\nTemps in fahrenheit\n{}\n{}\n{}\nTemps in celsius:\n{}\n{}\n{}\n'.format(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel)
                    # For Testing
                    print(body)
        elif (dayForcastCel, hourForcastCel, currentHourCel) == None: 
            print('This data has not been added: \n{}\n{}\n{}'.format(dayForcastCel, hourForcastCel, currentHourCel))
    except Exception as err:
        body = 'There was some sort of error within the program ---> {}'.format(err)

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)

    # This bellow actually sends the message. The rest contains it into a string and objects to send in email.
    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #     smtp.login(emailSender, emailPassword)
    #     smtp.sendmail(emailSender, emailReceiver, em.as_string())

    return