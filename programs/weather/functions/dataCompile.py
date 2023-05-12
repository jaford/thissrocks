from tabulate import tabulate
import pandas as pd

def dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour):
    try:    
        # Current weather data set as strings
        cDateTime = ('\nHere is the current stats for Albuquerque\nDate: {}\nTime: {}\n--------'.format(currentDate, currentTime))
        cTempOut = (u'Temperature: {}\u00b0'.format(cTemp))
        cFLOut = (u'What it feels like: {}\u00b0'.format(cFl))
        cHumOut = (u'Humidity:        {}\u0025'.format(cHum))
        cVizOut = (u'Visibility:      {}\u0025'.format(cViz))
        cPrecOut = (u'Precipitation:   {}\u0025'.format(cPrec))
        cWindSOut = ('Wind speed:      {}mph'.format(cWindS))
        cWindDOut = ('Wind direction:  {}\n--------\n'.format(cWindD))

        # print('Here is the next three days forecast in Albuquerque from {}\n--------'.format(currentDate))    
        # get the weather forecast for a few days

        print(forcastDay)
        print(type(forcastDay))

        dayForcast = pd.DataFrame(forcastDay)
        headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
        fForcast = tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid')
        # print(fForcast)
        
        headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']
        hourForcast = pd.DataFrame(forcastHour)
        hForcast = tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid')
        # print(hForcast)

        
        '''
        # Since these are coming from a dictionary, I may have to append these to a new list that holds each of these lines to a string in the new list. 
        # Once I do that, I can append all the string values in that list to a single string varible so I can call one item to display my items 
        forcastDate = ('Date: {}'.format(forecastDate))
        fTempOut = (u'Average temperature: {}\u00b0'.format(fTemp))
        fLowTemp = (u'Lowest temperature:  {}\u00b0'.format(fLowTemp))
        fHighTempOut = (u'Highest temperature: {}\u00b0\n--------\n'.format(fHighTemp))

        forcastDate = ('Date: {}'.format(forecastDate))
        fTempOut = (u'Average temperature: {}\u00b0'.format(fTemp))
        fLowTemp = (u'Lowest temperature:  {}\u00b0'.format(fLowTemp))
        fHighTempOut = (u'Highest temperature: {}\u00b0\n--------\n'.format(fHighTemp))
        ''' 
    except Exception as err: 
      print('An error has occured: {}'.format(err))

      return