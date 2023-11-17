import asyncio
import python_weather
import time

async def getWeather(city):
  # Noticed program will disconnect. Re-run program until a connection is sucure?
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    # I can loop through the entire program so user can pick the city. Something like the line bellow this one.    

    # Easy fix to enure I can get weather data from any city
    # weather = await client.get(city)
    weather = await client.get('Albuquerque')
    dateTime = weather.current.date
    currentDate = dateTime.strftime('%m-%d-%Y')
    currentTime = dateTime.strftime('%I:%M %p')

    # Creating list to append to for data that is being made bellow.
    forcastDay = {
      'forcastDate': [],
      'futureTemp': [],
      'highTemp': [],
      'lowTemp': []
    }

    forcastHour = {
      'forcastHour': [],
      'temperature': [],
      'description': []
    }
    
    forcastCurrent = {
        'cDate': [],
        'cTime': [],
        'cTempOut': [],
        'cFLOut': [],
        'cHumOut': [],
        'cVizOut': [],
        'cPrecOut': [],
        'cWindSOut': [],
        'cWindDOut': []
    }

    # Attempt to save the methods into callable objects from this function
    cTemp = str(weather.current.temperature)
    cFl   = str(weather.current.feels_like)
    cHum  = str(weather.current.humidity)
    cViz  = str(weather.current.visibility)
    cPrec = str(weather.current.precipitation)
    cWindS = str(weather.current.wind_speed)
    cWindD = str(weather.current.wind_direction)

    cTempOut = (u'{}\u00b0'.format(cTemp))
    cFLOut = (u'{}\u00b0'.format(cFl))
    cHumOut = (u'{}\u0025'.format(cHum))
    cVizOut = (u'{}\u0025'.format(cViz))
    cPrecOut = (u'{}\u0025'.format(cPrec))
    cWindSOut = ('{}mph'.format(cWindS))
    cWindDOut = ('{}'.format(cWindD))

    # Append the Current Forcast to the new list above
    forcastCurrent['cDate'].append(currentDate)
    forcastCurrent['cTime'].append(currentTime)
    forcastCurrent['cTempOut'].append(cTempOut)
    forcastCurrent['cFLOut'].append(cFLOut)  
    forcastCurrent['cHumOut'].append(cHumOut)
    forcastCurrent['cVizOut'].append(cVizOut)
    forcastCurrent['cPrecOut'].append(cPrecOut)
    forcastCurrent['cWindSOut'].append(cWindSOut)  
    forcastCurrent['cWindDOut'].append(cWindDOut)  

    for forecast in weather.forecasts:
      d = forecast.date
      forecastDate = d.strftime(f'%m-%d-%Y')
      fTemp = str(forecast.temperature)
      fHighTemp = str(forecast.highest_temperature)
      fLowTemp = str(forecast.lowest_temperature)
      forcastDay['forcastDate'].append(forecastDate)
      forcastDay['futureTemp'].append(fTemp)
      forcastDay['highTemp'].append(fHighTemp)
      forcastDay['lowTemp'].append(fLowTemp)  

    for hourly in forecast.hourly:
      d = hourly.time
      forecastHourly = d.strftime(f'%I:%M %p')
      hTemp = str(hourly.temperature)
      hDescr = str(hourly.description)
      forcastHour['forcastHour'].append(forecastHourly)
      forcastHour['temperature'].append(hTemp)
      forcastHour['description'].append(hDescr)

    return forcastDay, forcastHour, forcastCurrent
