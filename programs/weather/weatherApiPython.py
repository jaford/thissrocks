import python_weather
import asyncio
import os
from datetime import datetime

async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
  # async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
    weather = await client.get('Albuquerque')
    dateTime = weather.current.date
    currentDate = dateTime.strftime('%m/%d/%Y')
    currentTime = dateTime.strftime('%I:%M %p')

    print('\nHere is the current stats for Albuquerque\nDate: {}\nTime: {}\n--------'.format(currentDate, currentTime))    
    print('Temperature: {}'.format(weather.current.temperature))
    print('What it feels like: {}'.format(weather.current.feels_like))
    print('Humidity: {}'.format(weather.current.humidity))
    print('Visibility: {}'.format(weather.current.visibility))
    print('Precipitation: {}'.format(weather.current.precipitation))
    print('Wind speed: {}'.format(weather.current.wind_speed))
    print('Wind direction: {}'.format(weather.current.wind_direction))
    print('--------\n')    

    print('Here is the next three days forecast in Albuquerque from {}\n--------'.format(currentDate))    
    # get the weather forecast for a few days
    for forecast, i in weather.forecasts:
      d = forecast.date
      forecastDate = d.strftime(f'%m/%d/%Y')
      print('Date: {}'.format(forecastDate))
      print('Average temperature: {}'.format(forecast.temperature))
      print('Lowest temperature: {}'.format(forecast.lowest_temperature))
      print('Highest temperature: {}\n'.format(forecast.highest_temperature))
      
    #   # hourly forecasts
    #   for hourly in forecast.hourly:
    #     print(f' --> {hourly!r}')
    print('--------\n')    

asyncio.run(getweather())