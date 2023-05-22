from tabulate import tabulate
import pandas as pd

def feh2celform(tempDegree):
    tempDegree = float(tempDegree)
    try:
        if isinstance(tempDegree, str):
            print('"{}" is not a number!'.format(tempDegree))
        else: 
            fahrenheit = float(tempDegree)
            celsius = ((fahrenheit - 32) * (5 / 9))
            tempDegreeConv = str(round(celsius, 2))
            print(u'Fahrenheit: {}\u00b0\nCelsius: {}\u00b0'.format(tempDegree, tempDegreeConv))
    except Exception as err:
        celsiusError = str(tempDegree)
        print('"{}" is not a number!'.format(celsiusError))
        pass

    return tempDegreeConv

def feh2cel(forcastDay, forcastHour, forcastCurrent):
    try:
        print(forcastDay)    
        
        # Making a new dictionary to store the converted numbers
        # NEW THINGS TO DO: Append forcastDay dates into the new dictionary bellow! 
        forcastDayCel = {
        'forcastDate': [],
        'futureTemp': [],
        'highTemp': [],
        'lowTemp': []
        }

        for keys in forcastDay.keys():
            temps = forcastDay[keys]
            if keys == 'futureTemp':
                print(temps)
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastDayCel['futureTemp'].append(tempDegreeConv)
            if keys == 'highTemp':
                print(temps)
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastDayCel['highTemp'].append(tempDegreeConv)
            if keys == 'lowTemp':
                print(temps)
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastDayCel['lowTemp'].append(tempDegreeConv)
        
        print(forcastDayCel)    
            

        # THE WANT: I want to reprint the tables again but with the values converted.
        #  --> So far far to cel for day forcast is done! 
        headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
        dayForcast = pd.DataFrame(forcastDayCel)
        fForcastConv = tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid')
        
        headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']
        hourForcast = pd.DataFrame(forcastHour)
        hForcastConv = tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid')

        headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
        currentHour = pd.DataFrame(forcastCurrent)
        cForcastConv = tabulate(currentHour, headers = headerCurrentHour, tablefmt = 'fancy_grid')

        # print('\n{}\n{}\n{}\n'.format(cForcast, hForcast, fForcast))    
    
    except Exception as err: 
      print('An error has occured: {}'.format(err))

    return 