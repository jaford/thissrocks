def mockExcelWeatherData():
    # Calculate or define expected values
    expectedCForcast =  {
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

    expectedDForcast = {
        'forcastDate': ['06/11/2023 ', '06/12/2023 ', '06/13/2023 '],
        'futureTemp': ['88', '86', '89'],
        'highTemp': ['90', '88', '92'],
        'lowTemp': ['84', '81', '82']
    }

    expectedHForcast = {
        'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
        'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
        'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
    }

    expectedforcastCurrentCel = {
        'cDate': ['06/11/2023'],
        'cTime': ['10:02 AM'],
        'cTempOut': ['20.56'],
        'cFLOut': ['20.56'],
        'cHumOut': ['18%'],
        'cVizOut': ['9%'],
        'cPrecOut': ['0.0%'],
        'cWindSOut': ['2mph'],
        'cWindDOut': ['North']
    }

    expectedforcastDayCel = {
        'forcastDate': ['06/11/2023 ', '06/12/2023 ', '06/13/2023 '],
        'futureTemp': ['31.11', '30.0', '31.67'],
        'highTemp': ['32.22', '31.11', '33.33'],
        'lowTemp': ['28.89', '27.22', '27.78']
    }

    expectedforcastHourCel = {
        'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
        'temperature': ['31.11', '30.0', '31.67', '32.22', '31.11', '33.33', '28.89', '27.22'],
        'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
    }
    
    return expectedCForcast, expectedDForcast, expectedHForcast, expectedforcastCurrentCel, expectedforcastDayCel, expectedforcastHourCel