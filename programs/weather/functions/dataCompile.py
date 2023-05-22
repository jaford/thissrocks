import pandas as pd
from tabulate import tabulate

def dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour, forcastCurrent):
    try:    
        # Current weather data set as strings\
        # Can probably replace this at somepoint!
        cDateTime = ('\nHere is the current stats for Albuquerque\nDate: {}\nTime: {}\n--------'.format(currentDate, currentTime))
        cTempOut = (u'Temperature: {}\u00b0'.format(cTemp))
        cFLOut = (u'What it feels like: {}\u00b0'.format(cFl))
        cHumOut = (u'Humidity:        {}\u0025'.format(cHum))
        cVizOut = (u'Visibility:      {}\u0025'.format(cViz))
        cPrecOut = (u'Precipitation:   {}\u0025'.format(cPrec))
        cWindSOut = ('Wind speed:      {}mph'.format(cWindS))
        cWindDOut = ('Wind direction:  {}\n--------\n'.format(cWindD))

        # Creating tables to display the information to terminal. Later possibly in a email format of some sort. Possibly append the strings together?
        headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
        currentHour = pd.DataFrame(forcastCurrent)
        cForcast = str(tabulate(currentHour, headers = headerCurrentHour, tablefmt = 'fancy_grid'))

        headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
        dayForcast = pd.DataFrame(forcastDay)
        fForcast = str(tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid'))
        
        headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']
        hourForcast = pd.DataFrame(forcastHour)
        hForcast = str(tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid'))

        print('\n{}\n{}\n{}\n'.format(cForcast, hForcast, fForcast))    

    except Exception as err: 
      print('An error has occured: {}'.format(err))

      return 