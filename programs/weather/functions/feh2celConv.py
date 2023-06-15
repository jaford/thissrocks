from tabulate import tabulate
import pandas as pd
import re

def feh2celform(tempDegree):
    tempDegreeDec = re.sub('\D', '', tempDegree)
    tempDegree = float(tempDegreeDec)
    try:
        if isinstance(tempDegree, str):
            print('"{}" is not a number!'.format(tempDegree))
        else: 
            fahrenheit = float(tempDegree)
            celsius = ((fahrenheit - 32) * (5 / 9))
            tempDegreeConv = str(round(celsius, 2))
            # Print this for testing if needed!
            # print(u'Fahrenheit: {}\u00b0\nCelsius: {}\u00b0'.format(tempDegree, tempDegreeConv))
    except Exception as err:
        celsiusError = str(tempDegree)
        print('"{}" is not a number!'.format(celsiusError))
        pass

    return tempDegreeConv

def feh2cel(forcastDay, forcastHour, forcastCurrent):
    try:        
        # Making a new dictionary to store the converted numbers
        forcastDayCel = {
            'forcastDate': [],
            'futureTemp': [],
            'highTemp': [],
            'lowTemp': []
        }

        forcastHourCel = {
            'forcastHour': [],
            'temperature': [],
            'description': []
        }

        forcastCurrentCel = {
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

        for keys in forcastDay.keys():
            temps = forcastDay[keys]
            if keys == 'forcastDate':
                dates = forcastDay['forcastDate']
                for date in dates:
                    forcastDayCel['forcastDate'].append(date)
            if keys == 'futureTemp':
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastDayCel['futureTemp'].append(tempDegreeConv)
            if keys == 'highTemp':
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastDayCel['highTemp'].append(tempDegreeConv)
            if keys == 'lowTemp':
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastDayCel['lowTemp'].append(tempDegreeConv)
        for keys in forcastHour.keys():
            temps = forcastHour[keys]
            if keys == 'temperature':
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastHourCel['temperature'].append(tempDegreeConv)
            if keys == 'forcastHour':
                hours = forcastHour['forcastHour']
                for hour in hours:
                    forcastHourCel['forcastHour'].append(hour)
            if keys == 'description':
                details = forcastHour['description']
                for descr in details:
                    forcastHourCel['description'].append(descr)
        for keys in forcastCurrent.keys():
            temps = forcastCurrent[keys]
            if keys == 'cDate':
                date = forcastCurrent['cDate']
                for i in date:
                    forcastCurrentCel['cDate'].append(i)
            if keys == 'cTime':
                time = forcastCurrent['cTime']
                for i in time:
                    forcastCurrentCel['cTime'].append(i)
            if keys == 'cTempOut':
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastCurrentCel['cTempOut'].append(tempDegreeConv)
            if keys == 'cFLOut':
                for tempDegree in temps:
                    tempDegreeConv = feh2celform(tempDegree)
                    forcastCurrentCel['cFLOut'].append(tempDegreeConv)
            if keys == 'cHumOut':
                hum = forcastCurrent['cHumOut']
                for i in hum:
                    forcastCurrentCel['cHumOut'].append(i)
            if keys == 'cVizOut':
                viz = forcastCurrent['cVizOut']
                for i in viz:
                    forcastCurrentCel['cVizOut'].append(i)
            if keys == 'cPrecOut':
                prec = forcastCurrent['cPrecOut']
                for i in prec:
                    forcastCurrentCel['cPrecOut'].append(i)
            if keys == 'cWindSOut':
                windS = forcastCurrent['cWindSOut']
                for i in windS:
                    forcastCurrentCel['cWindSOut'].append(i)
            if keys == 'cWindDOut':
                windD = forcastCurrent['cWindDOut']
                for i in windD:
                    forcastCurrentCel['cWindDOut'].append(i)   

        # Using pandas and tabulate, I can save the pandas boject but I print the tables here.
        # I could poossibly create the tables again since they save as none type when I attempt to make a object for later use. 
        # May need some help with that! 
        headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
        currentHourCel = pd.DataFrame(forcastCurrentCel)
        cForcastConv = tabulate(currentHourCel, headers = headerCurrentHour, tablefmt = 'fancy_grid')

        headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
        dayForcastCel = pd.DataFrame(forcastDayCel)
        fForcastConv = tabulate(dayForcastCel, headers = headerForcastDay, tablefmt = 'fancy_grid')
        
        headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']
        hourForcastCel = pd.DataFrame(forcastHourCel)
        hForcastConv = tabulate(hourForcastCel, headers = headerForcastHour, tablefmt = 'fancy_grid')

        # Can print fo testing
        # print('\n{}\n{}\n{}\n'.format(cForcastConv, hForcastConv, fForcastConv))    
    
    except Exception as err: 
        print('An error has occured: {}'.format(err))

    return dayForcastCel, hourForcastCel, currentHourCel, cForcastConv, fForcastConv, hForcastConv