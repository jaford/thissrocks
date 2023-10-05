def weatherDataTest():
    # Simulate API response or generate mock weather data
    forcastCurrent = {
        'cDate': ['06/11/2023'],
        'cTime': ['10:02 AM'],
        'cTempOut': ['69°'],
        'cFLOut': ['69°'],
        'cHumOut': ['18%'],
        'cVizOut': ['9%'],
        'cPrecOut': ['0.0%'],
        'cWindSOut': ['2mph'],
        'cWindDOut': ['North']
    }

    forcastDay = {
        'forcastDate': ['06/11/2023 ', '06/12/2023 ', '06/13/2023 '],
        'futureTemp': ['88', '86', '89'],
        'highTemp': ['90', '88', '92'],
        'lowTemp': ['84', '81', '82']
    }

    forcastHour = {
        'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
        'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
        'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
    }
    

    return forcastDay, forcastHour, forcastCurrent