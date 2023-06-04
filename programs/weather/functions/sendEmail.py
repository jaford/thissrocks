import smtplib
import time
import logging
from tabulate import tabulate
import pandas as pd
from email.message import EmailMessage
from .lineRemove import deleteLastLine

def sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel):
    # Need to put these isinstance into one argument? Last time it gave an error. Unsure why. 
    try:
        if isinstance(currentHour, pd.DataFrame):
            cForcast = str(tabulate(currentHour, headers = headerCurrentHour, tablefmt = 'fancy_grid'))
            if isinstance(dayForcast, pd.DataFrame):
                fForcast = str(tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid'))
                if isinstance(hourForcast, pd.DataFrame):
                    hForcast = str(tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid'))
                    body = 'Here is your data:\nTemps in fahrenheit\n{}\n{}\n{}\n'.format(cForcast, hForcast, fForcast)
                    print(body)
        if isinstance(currentHourCel, pd.DataFrame):
            cForcastConv = tabulate(currentHourCel, headers = headerCurrentHour, tablefmt = 'fancy_grid')
            if isinstance(dayForcastCel, pd.DataFrame):
                fForcastConv = tabulate(dayForcastCel, headers = headerForcastDay, tablefmt = 'fancy_grid')
                if isinstance(hourForcastCel, pd.DataFrame):
                    hForcastConv = tabulate(hourForcastCel, headers = headerForcastHour, tablefmt = 'fancy_grid')
                    body = 'Here is your data:\nTemps in fahrenheit\n{}\n{}\n{}\nTemps in celsius:\n{}\n{}\n{}\n'.format(cForcast, fForcast, hForcast, cForcastConv, fForcastConv, hForcastConv)
                    print(body)
        elif (dayForcastCel, hourForcastCel, currentHourCel) == None: 
            print('This data has not been added: \n{}\n{}\n{}'.format(dayForcastCel, hourForcastCel, currentHourCel))

        else: 
            print('There was a error:\n')
            pass
    except Exception as err:
        body = 'There was an error: ---> {}'.format(err)    
    
    # This long conditional is for testing purpose. Remove these conditionals once program is ready for launch!
    userInput = input('\nDo you wish to actually send the email? (Y/N): ').lower().strip()
    if isinstance (userInput, str):
        lineAmount = len(userInput.splitlines())
        deleteLastLine(lineAmount)
        userInput = input('Enter the senders email: ').lower()
        if isinstance (userInput, str):
            emailSender = userInput
        userInput = input('Enter the senders email password: ')
        if isinstance (userInput, str):
            emailPassword = userInput
        userInput = input('Enter the receivers email: ').lower()
        if isinstance (userInput, str):
            lineAmount = len(userInput.splitlines()) + 2
            deleteLastLine(lineAmount)
            emailReceiver = userInput

        # This is hard coded for now! Code above has no use at the moment but is there! 
        emailSender = 'hoonterpymailtest@gmail.com'
        emailPassword = 'cxcvdtzhtnogsust'
        emailReceiver = 'hunterpimparatana@gmail.com'

        subject = 'Check out this test!'
        mailSigniture = '\nKindly,\nHunter Pimparatana.\nEmail: hunterpimparatana@gmail.com\nMobile: (505)-918-4031'
        headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
        headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
        headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']
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
    elif userInput == 'n' or userInput == 'q':
        print('You have quit the program.\n')
    else:
        print('User input is not supported: "{}"'.format(userInput))

    return