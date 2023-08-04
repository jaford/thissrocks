from tabulate import tabulate
import pandas as pd
import re

def feh2celform(tempDegree):
    tempDegreeDec = re.sub('\D', '', tempDegree)
    tempDegree = float(tempDegreeDec)
    try:
        fahrenheit = float(tempDegree)
        celsius = ((fahrenheit - 32) * (5 / 9))
        tempDegreeConv = str(round(celsius, 2))
    except (ValueError, TypeError):
        celsiusError = str(tempDegree)
        print('"{}" is not a valid temperature!'.format(tempDegree))

    return tempDegreeConv

def createEmptyDict(originalDict):
    newDict = {}
    for key in originalDict:
        newDict[f'{key}'] = []
    return newDict

def feh2cel(forcastDay, forcastHour, forcastCurrent):
    try:        
        # Making new dictionaries to store the converted numbers
        forcastDayCel = createEmptyDict(forcastDay)
        forcastHourCel = createEmptyDict(forcastHour)
        forcastCurrentCel = createEmptyDict(forcastCurrent)

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

    # return dayForcastCel, hourForcastCel, currentHourCel, cForcastConv, fForcastConv, hForcastConv
    # return dayForcastCel, hourForcastCel, currentHourCel
    return cForcastConv, fForcastConv, hForcastConv, forcastCurrentCel, forcastDayCel, forcastHourCel