from tabulate import tabulate
import pandas as pd

def feh2celform(tempDegree):
    tempDegree = float(tempDegree)
    try:
        if isinstance(tempDegree, str):
            print('"{}" is not a number!'.format(tempDegree))
        else: 
            fahrenheit = float(tempDegree)
            tempDegreeConv = ((fahrenheit - 32) * (5 / 9))
            print(u'Fahrenheit: {}\u00b0\nCelsius: {}\u00b0'.format(tempDegree, tempDegreeConv))
    except Exception as err:
        celsiusError = str(tempDegree)
        print('"{}" is not a number!'.format(celsiusError))
        pass

    return tempDegreeConv

def feh2cel(forcastDay, forcastHour, forcastCurrent):
    
    print(forcastDay)    

    for keys in forcastDay.keys():
        temps = forcastDay[keys]
        if keys == 'futureTemp':
            print(temps)
            for tempDegree in temps:
                tempDegreeConv = feh2celform(tempDegree)
        if keys == 'highTemp':
            print(temps)
            for tempDegree in temps:
                tempDegreeConv = feh2celform(tempDegree)
        if keys == 'lowTemp':
            print(temps)
            for tempDegree in temps:
                tempDegreeConv = feh2celform(tempDegree)

    # THE WANT: I want to reprint the tables again but with the values converted.
    headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
    dayForcast = pd.DataFrame(forcastDay)
    fForcastConv = tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid')
    
    headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']
    hourForcast = pd.DataFrame(forcastHour)
    hForcastConv = tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid')

    headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
    currentHour = pd.DataFrame(forcastCurrent)
    cForcastConv = tabulate(currentHour, headers = headerCurrentHour, tablefmt = 'fancy_grid')

    return fForcastConv, hForcastConv, cForcastConv