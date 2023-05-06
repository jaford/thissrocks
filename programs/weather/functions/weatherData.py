import python_weather
import asyncio
async def getWeather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
  # async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
    weather = await client.get('Albuquerque')
    dateTime = weather.current.date
    currentDate = dateTime.strftime('%m/%d/%Y')
    currentTime = dateTime.strftime('%I:%M %p')

    try:  
      print('\nHere is the current stats for Albuquerque\nDate: {}\nTime: {}\n--------'.format(currentDate, currentTime))    
      print(u'Temperature: {}\u00b0'.format(weather.current.temperature))
      print(u'What it feels like: {}\u00b0'.format(weather.current.feels_like))
      print(u'Humidity:        {}\u0025'.format(weather.current.humidity))
      print(u'Visibility:      {}\u0025'.format(weather.current.visibility))
      print(u'Precipitation:   {}\u0025'.format(weather.current.precipitation))
      print('Wind speed:      {}mph'.format(weather.current.wind_speed))
      print('Wind direction:  {}'.format(weather.current.wind_direction))
      print('--------\n')    

      #  Noticed it disconnects. Re-run program until a connection is sucure?
      # Attempt to save the methods into callable objects from this function
      cTemp = str(weather.current.temperature)
      cFl   = str(weather.current.feels_like)
      cHum  = str(weather.current.humidity)
      cViz  = str(weather.current.visibility)
      cPrec = str(weather.current.precipitation)
      cWindS = str(weather.current.wind_speed)
      cWindD = str(weather.current.wind_direction)

      print('Here is the next three days forecast in Albuquerque from {}\n--------'.format(currentDate))    
      # get the weather forecast for a few days
      for forecast in weather.forecasts:
        d = forecast.date
        fTemp = str(forecast.temperature)
        fLowTemp = str(forecast.lowest_temperature)
        fHighTemp = str(forecast.highest_temperature)
        forecastDate = d.strftime(f'%m/%d/%Y')
        print('Date: {}'.format(forecastDate))
        print(u'Average temperature: {}\u00b0'.format(forecast.temperature))
        print(u'Lowest temperature:  {}\u00b0'.format(forecast.lowest_temperature))
        print(u'Highest temperature: {}\u00b0\n'.format(forecast.highest_temperature))
      print('--------\n')  
      # hourly forecasts
      for hourly in forecast.hourly:
        print(f' --> {hourly!r}')

    except Exception as err: 
      print('An error has occured: {}'.format(err))

asyncio.run(getWeather())