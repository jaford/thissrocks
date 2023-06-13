# -*- coding: utf-8 -*-

import unittest
import pandas as pd
from tabulate import tabulate
import sys
import os
from functions import dataCompile
# Add the directory containing main.py to the sys.path
mainDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main'))
sys.path.insert(0, mainDir)

def mockWeatherData():
    # Simulate API response or generate mock weather data
    # Return the mock weather data
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

    return forcastDay, forcastHour, forcastCurrent

    class testWeatherAPI(unittest.TestCase):
        def setUp(self):
            # Set up the necessary test fixtures
            self.weatherData = mockWeatherData()

        def dataFormatingTest(self):
            forcastDay, forcastHour, forcastCurrent = mockWeatherData()
            currentHour, dayForcast, hourForcast, hForcast, fForcast, cForcast = dataFormating(forcastDay, forcastHour, forcastCurrent)

            # Assertions (RUN IN PYTHON3)
            self.assertEqual(currentHour, expectedCForcast, f"currentHour assertion failed:\nExpected: {expectedCForcast}\nActual: {currentHour}")
            self.assertEqual(dayForcast, expectedFForcast, f"dayForcast assertion failed:\nExpected: {expectedFForcast}\nActual: {dayForcast}")
            self.assertEqual(hourForcast, expectedHForcast, f"hourForcast assertion failed:\nExpected: {expectedHForcast}\nActual: {hourForcast}")
            self.assertEqual(cForcast, expectedCForcast, f"cForcast assertion failed:\nExpected: {expectedCForcast}\nActual: {cForcast}")
            self.assertEqual(fForcast, expectedFForcast, f"fForcast assertion failed:\nExpected: {expectedFForcast}\nActual: {fForcast}")
            self.assertEqual(hForcast, expectedHForcast, f"hForcast assertion failed:\nExpected: {expectedHForcast}\nActual: {hForcast}")

        # def dataFormatingTest(self):
        #     headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
        #     headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
        #     headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']
            
        #     dayForcast = pd.DataFrame(self.weatherData[0])
        #     fForcast = str(tabulate(dayForcast, headers = headerForcastDay, tablefmt = 'fancy_grid'))

        #     hourForcast = pd.DataFrame(self.weatherData[1])
        #     hForcast = str(tabulate(hourForcast, headers = headerForcastHour, tablefmt = 'fancy_grid'))

        #     currentHour = pd.DataFrame(self.weatherData[2])
        #     cForcast = str(tabulate(currentHour, headers = headerCurrentHour, tablefmt = 'fancy_grid'))

        #     # Assertions (RUN IN PYTHON3)
        #     self.assertEqual(cForcast, expectedCForcast, f"cForcast assertion failed:\nExpected: {expectedCForcast}\nActual: {cForcast}")
        #     self.assertEqual(fForcast, expectedFForcast, f"fForcast assertion failed:\nExpected: {expectedFForcast}\nActual: {fForcast}")
        #     self.assertEqual(hForcast, expectedHForcast, f"hForcast assertion failed:\nExpected: {expectedHForcast}\nActual: {hForcast}")

if __name__ == '__main__':
    unittest.main()