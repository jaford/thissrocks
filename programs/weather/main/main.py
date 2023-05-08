import python_weather
import asyncio
import os
import sys, signal
sys.path.append('..')
from datetime import datetime
from termios import tcflush, TCIFLUSH
# from functions.dataCompile import dataFormating
# from functions.feh2celConv import feh2cel
# from functions.progressBar import loadBar
# from functions.sendEmail import sendMail
from functions.weatherData import getWeather


# THIS IS COMMENTED OUT JUST IN CASE
# async def getWeather():
#   # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
#   async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
#   # async with python_weather.Client(unit=python_weather.METRIC) as client:

#     # fetch a weather forecast from a city
#     weather = await client.get('Albuquerque')
#     dateTime = weather.current.date
#     currentDate = dateTime.strftime('%m/%d/%Y')
#     currentTime = dateTime.strftime('%I:%M %p')


#     # Noticed program will disconnect. Re-run program until a connection is sucure?
#     # Attempt to save the methods into callable objects from this function
#     cTemp = str(weather.current.temperature)
#     cFl   = str(weather.current.feels_like)
#     cHum  = str(weather.current.humidity)
#     cViz  = str(weather.current.visibility)
#     cPrec = str(weather.current.precipitation)
#     cWindS = str(weather.current.wind_speed)
#     cWindD = str(weather.current.wind_direction)

#     # print('Here is the next three days forecast in Albuquerque from {}\n--------'.format(currentDate))    
#     # get the weather forecast for a few days
#     forcastDay = {
#       'forcastDate': [],
#       'futureTemp': [],
#       'highTemp': [],
#       'lowTemp': []
#     }

#     forcastHour = {
#       'forcastHour': [],
#       'temperature': [],
#       'description': []
#     }

#     for forecast in weather.forecasts:
#       d = forecast.date
#       forecastDate = d.strftime(f'%m/%d/%Y')
#       fTemp = str(forecast.temperature)
#       fLowTemp = str(forecast.lowest_temperature)
#       fHighTemp = str(forecast.highest_temperature)
#       forcastDay['forcastDate'].append(forecastDate)
#       forcastDay['futureTemp'].append(fTemp)
#       forcastDay['highTemp'].append(fLowTemp)
#       forcastDay['lowTemp'].append(fHighTemp)  

#     for hourly in forecast.hourly:
#       d = hourly.time
#       forecastDate = d.strftime(f'%I:%M %p')
#       hTemp = str(hourly.temperature)
#       hDescr = str(hourly.description)
#       forcastHour['forcastHour'].append(forecastDate)
#       forcastHour['temperature'].append(hTemp)
#       forcastHour['description'].append(hDescr)
#       print(f' --> {hourly!r}')

#     return cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, currentDate, currentTime, forcastDay, forcastHour

# # Use this to run main.
cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, currentDate, currentTime, forcastDay, forcastHour = asyncio.run(getWeather())

# TEST THIS LATER 
# cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, forecastDate, currentDate, currentTime = asyncio.run(getweather())
# dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, forecastDate, currentDate, currentTime)