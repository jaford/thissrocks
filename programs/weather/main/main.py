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
cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour, forcastCurrent = asyncio.run(getWeather())
loadBar()

currentHour, dayForcast, hourForcast = dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour, forcastCurrent)
print(currentHour)
print(dayForcast)
print(hourForcast)

userInput = input('(Y/N) Would you want to convert from Fahrenheit to Celsius for todays forcast?: ').lower()
if userInput == 'y':
    if isinstance (userInput, str):
        lineAmount = len(userInput.splitlines()) - 1
        deleteLastLine(lineAmount)
    dayForcastCel, hourForcastCel, currentHourCel = feh2cel(forcastDay, forcastHour, forcastCurrent)
    print(currentHourCel)
    print(dayForcastCel)
    print(hourForcastCel)
    print(type(hourForcastCel))

userInput = input('(Y/N) Do you want this information sent to your email?: ').lower()
if userInput == 'y':
    if isinstance (userInput, str):
        lineAmount = len(userInput.splitlines()) - 1
        deleteLastLine(lineAmount)
    if isinstance(currentHourCel, pd.DataFrame):
        if isinstance(dayForcastCel, pd.DataFrame):
            if isinstance(hourForcastCel, pd.DataFrame):
                sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel)
    else:
        print(type(currentHourCel))
        print(type(dayForcastCel))
        print(type(hourForcastCel))
        sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel)
        print('Cel conversion was not done: \n{}\n{}\n{}\n'.format(dayForcastCel, hourForcastCel, currentHourCel))
        
        # DOES NOT WORK :(
        # if hourForcastCel == None and hourForcastCel == None and currentHourCel == None:
        #     sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel)
        # elif isinstance ((currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel), pd.DataFrame):
        #     sendMail(currentHour, dayForcast, hourForcast, dayForcastCel, hourForcastCel, currentHourCel)
        # else:
        #     print('Something broke very badly. #SAD')
else:
    print('User input is not supported: "{}"'.format(userInput))



# TEST THIS LATER 
# cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, forecastDate, currentDate, currentTime = asyncio.run(getweather())
# dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, forecastDate, currentDate, currentTime)