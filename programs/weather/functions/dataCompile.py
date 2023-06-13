import pandas as pd
from tabulate import tabulate

def dataFormating(cTemp, cFl, cHum, cViz, cPrec, cWindS, cWindD, currentDate, currentTime, forcastDay, forcastHour, forcastCurrent):
    try:    

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
        
    except Exception as err: 
      print('An error has occured: {}'.format(err))

    return currentHour, dayForcast, hourForcast, hForcast, fForcast, cForcast