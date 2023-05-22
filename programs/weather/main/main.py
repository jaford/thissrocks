import python_weather
import asyncio
import os
import sys, signal
sys.path.append('..')
from datetime import datetime
from termios import tcflush, TCIFLUSH
from functions.weatherData import getWeather
from functions.dataCompile import dataFormating
from functions.feh2celConv import feh2cel
# from functions.progressBar import loadBar
# from functions.sendEmail import sendMail

# THIS ACTUALLY WORKS! 
# Use this to run main.
cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour, forcastCurrent = asyncio.run(getWeather())
dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour, forcastCurrent)

userInput = input('(Y/N) Would you want to convert from Fahrenheit to Celsius for todays forcast?: ').lower()
if userInput == 'y':
    feh2cel(forcastDay, forcastHour, forcastCurrent)




# TEST THIS LATER 
# cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, forecastDate, currentDate, currentTime = asyncio.run(getweather())
# dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, forecastDate, currentDate, currentTime)