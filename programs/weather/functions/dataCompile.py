def dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, fTemp, fLowTemp, fHighTemp, forecastDate, currentDate, currentTime):
    try:    
        # Current weather data set as strings
        print('\nHere is the current stats for Albuquerque\nDate: {}\nTime: {}\n--------'.format(currentDate, currentTime))    
        print(u'Temperature: {}\u00b0'.format(cTemp))
        print(u'What it feels like: {}\u00b0'.format(cFl))
        print(u'Humidity:        {}\u0025'.format(cHum))
        print(u'Visibility:      {}\u0025'.format(cViz))
        print(u'Precipitation:   {}\u0025'.format(cPrec))
        print('Wind speed:      {}mph'.format(cWindS))
        print('Wind direction:  {}'.format(cWindS))
        print('--------\n')   

        # print('Here is the next three days forecast in Albuquerque from {}\n--------'.format(currentDate))    
        # get the weather forecast for a few days
        print('Date: {}'.format(forecastDate))
        print(u'Average temperature: {}\u00b0'.format(fTemp))
        print(u'Lowest temperature:  {}\u00b0'.format(fLowTemp))
        print(u'Highest temperature: {}\u00b0\n'.format(fHighTemp))
        print('--------\n')  

    except Exception as err: 
      print('An error has occured: {}'.format(err))

      return