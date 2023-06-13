import python_weather
import asyncio
import os
import sys, signal
import pandas as pd
sys.path.append('..')
from datetime import datetime
from termios import tcflush, TCIFLUSH
from functions.weatherData import getWeather
from functions.dataCompile import dataFormating
from functions.feh2celConv import feh2cel
from functions.progressBar import loadBar
from functions.sendEmail import sendMail
from functions.lineRemove  import deleteLastLine

currentHour = None
dayForcast  = None
hourForcas  = None
currentHourCel  = None
dayForcastCel   = None
hourForcastCel  = None
# THIS ACTUALLY WORKS! 
# Use this to run main.

while True:
    introText = '\n---- Welcome to my Weather Program! ----\n\n----How to use----\n'\
        'Step 1: Enter the city in which you want to see the weather in.\n'\
        'Step 2: Convert the tempatures into celsius if you want to see both displayed.\n'\
        'Step 3: Select to see if you want to information to display on your terminal or sent as email to yourself. (AKA ME AS OF NOW)\n'\
        '\n---- Current issues/upcoming features ----\n'\
        'Add to where you can enter the cities name\nCreate unit test to for my program to better run testing. (Create random values for the lists/dictionaries)\n'\
        'Have a enterable email (Sender & reciver)\nAdd color logging at a later point!\n'\
    
    print(introText)
    userInput = input('Are you ready to start? (Y/N)\n').lower().strip()
    lineAmount = len(userInput.splitlines() + introText.splitlines())
    deleteLastLine(lineAmount)
    if userInput == 'y':
        while True: 
                try:
                    city = input('Enter the city you want to see the weather for. Needs to be spelling accurate: ').lower().capitalize()
                    lineAmount = len(userInput.splitlines())
                    deleteLastLine(lineAmount)
                    cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour, forcastCurrent = asyncio.run(getWeather(city))
                    currentHour, dayForcast, hourForcast, hForcast, fForcast, cForcast = dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour, forcastCurrent)
                    print('Here is your weather data:\n\nTemps in fahrenheit\n{}\n{}\n{}\n'.format(cForcast, hForcast, fForcast))

                    userInput = input('(Y/N) Would you want to convert from Fahrenheit to Celsius for todays forcast?: ').lower()
                    if userInput == 'y':
                        lineAmount = len(userInput.splitlines()) - 1
                        deleteLastLine(lineAmount)
                        dayForcastCel, hourForcastCel, currentHourCel, cForcastConv, fForcastConv, hForcastConv= feh2cel(forcastDay, forcastHour, forcastCurrent)
                        print('Here is your weather data:\n\nTemps in celsius:\n{}\n{}\n{}\n').format(cForcastConv, fForcastConv, hForcastConv)
                    elif userInput == 'n':
                        print('CODE THIS SHIZZ NEXT\n')
                    elif userInput == 'q':
                        print('You have quit the program!\n')
                        exit()
                    
                    userInput = input('(Y/N) Do you want this information sent to your email?: ').lower()
                    if userInput == 'y':
                        lineAmount = len(userInput.splitlines()) - 1
                        deleteLastLine(lineAmount)
                        if isinstance(currentHourCel, pd.DataFrame) and isinstance(dayForcastCel, pd.DataFrame) and isinstance(hourForcastCel, pd.DataFrame):
                            sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel)
                        else:
                            print('Cel conversion was not done (These should be None): \n{}\n{}\n{}\n'.format(dayForcastCel, hourForcastCel, currentHourCel))
                            sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel)
                    elif userInput == 'n':
                        # New condition to print objects to terminal! 
                        print('CODE THIS SHIZZ NEXT\n')
                    elif userInput == 'q':
                        print('You have quit the program!\n')
                        exit()
                    else:
                        print('User input is not supported: "{}"'.format(userInput))
                        exit()
                except Exception as err: 
                    print('\nA error occured --> : "{}"\n'.format(err))
                    pass
                    
    elif userInput == 'n' or userInput == 'q':
        print('You have quit the program.\n')
    else:
        print('You have entered a incorrect value: {}\nQuiting the program...'.format(userStart))
        exit()
