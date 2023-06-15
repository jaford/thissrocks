# -*- coding: utf-8 -*-
import unittest
import pandas as pd
from tabulate import tabulate
import sys
import os

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directories containing main.py and functions.py to the sys.path
main_dir = os.path.abspath(os.path.join(current_dir, '..', 'main'))
functions_dir = os.path.abspath(os.path.join(current_dir, '..', 'functions'))
sys.path.insert(0, main_dir)
sys.path.insert(0, functions_dir)

from dataCompile import dataFormating
from feh2celConv import feh2cel

def mockWeatherData():
    # Simulate API response or generate mock weather data
    # forcastDay = {
    #     'forcastDay': {
    #         'forcastDate': ['06/11/2023 ', '06/12/2023 ', '06/13/2023 '],
    #         'futureTemp': ['88', '86', '89'],
    #         'highTemp': ['90', '88', '92'],
    #         'lowTemp': ['84', '81', '82']
    #     }
    # }

    # forcastHour = {
    #   'forcastHour': {
    #       'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
    #       'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
    #       'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
    #     }
    # }
    
    # forcastCurrent = {
    #     'forcastCurrent': {
    #         'cDate': ['06/11/2023'],
    #         'cTime': ['10:02 AM'],
    #         'cTempOut': ['69°'],
    #         'cFLOut': ['69°'],
    #         'cHumOut': ['18%'],
    #         'cVizOut': ['9%'],
    #         'cPrecOut': ['0.0%'],
    #         'cWindSOut': ['2mph'],
    #         'cWindDOut': ['North']
    #     }
    # }

    # Remove that this variable that equals a dict. THERE HAS TO BE A WAY
    forcastDay = {
        'forcastDay': {
            'forcastDate': ['06/11/2023 ', '06/12/2023 ', '06/13/2023 '],
            'futureTemp': ['88', '86', '89'],
            'highTemp': ['90', '88', '92'],
            'lowTemp': ['84', '81', '82']
        }
    }

    forcastHour = {
      'forcastHour': {
          'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
          'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
          'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
        }
    }
    
    forcastCurrent = {
        'forcastCurrent': {
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
    }

    return forcastDay, forcastHour, forcastCurrent

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        # Set up the necessary test fixtures
        forcastDay, forcastHour, forcastCurrent = mockWeatherData()
        self.forcastDay = forcastDay  # Assigning value to instance variable
        self.forcastHour = forcastHour  # Assigning value to instance variable
        self.forcastCurrent = forcastCurrent  # Assigning value to instance variable

    def test_dataFormating(self):
        # Calculate or define expected values
        # expectedCForcast =  {
        #     'forcastCurrent': {
        #         'cDate': ['06/11/2023'],
        #         'cTime': ['10:02 AM'],
        #         'cTempOut': ['69°'],
        #         'cFLOut': ['69°'],
        #         'cHumOut': ['18%'],
        #         'cVizOut': ['9%'],
        #         'cPrecOut': ['0.0%'],
        #         'cWindSOut': ['2mph'],
        #         'cWindDOut': ['North']
        #     }
        # }

        # expectedDForcast = {
        #     'forcastDay': {
        #         'forcastDate': ['06/11/2023 ', '06/12/2023 ', '06/13/2023 '],
        #         'futureTemp': ['88', '86', '89'],
        #         'highTemp': ['90', '88', '92'],
        #         'lowTemp': ['84', '81', '82']
        #     }
        # }

        # expectedHForcast = {
        #     'forcastHour': {
        #         'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
        #         'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
        #         'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
        #     } 
        # }

        expectedCForcast =  {
            'forcastCurrent': {
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
        }

        expectedDForcast = {
            'forcastDay': {
                'forcastDate': ['06/11/2023 ', '06/12/2023 ', '06/13/2023 '],
                'futureTemp': ['88', '86', '89'],
                'highTemp': ['90', '88', '92'],
                'lowTemp': ['84', '81', '82']
            }
        }

        expectedHForcast = {
            'forcastHour': {
                'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
                'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
                'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
            } 
        }


        # Assertions (RUN IN PYTHON3)
        # Test data
        self.assertEqual(self.forcastCurrent, expectedCForcast, f"forcastCurrent assertion failed:\nExpected: {expectedCForcast}\nActual: {self.forcastCurrent}")
        self.assertEqual(self.forcastDay, expectedDForcast, f"forcastDay assertion failed:\nExpected: {expectedDForcast}\nActual: {self.forcastDay}")
        self.assertEqual(self.forcastHour, expectedHForcast, f"forcastHour assertion failed:\nExpected: {expectedHForcast}\nActual: {self.forcastHour}")
        
        # Congfigure this later on. Lets Test the pandas formatting later. 
        # I can write a new test for fehr2el later on! 

        # # Test data into pandas objects
        # self.assertEqual(currentHour, expectedCForcast, f"currentHour assertion failed:\nExpected: {expectedCForcast}\nActual: {currentHour}")
        # self.assertEqual(dayForcast, expectedDForcast, f"dayForcast assertion failed:\nExpected: {expectedDForcast}\nActual: {dayForcast}")
        # self.assertEqual(hourForcast, expectedHForcast, f"hourForcast assertion failed:\nExpected: {expectedHForcast}\nActual: {hourForcast}")
        
        # # Test data into tabulate
        # self.assertEqual(cForcast, expectedCForcast, f"cForcast assertion failed:\nExpected: {expectedCForcast}\nActual: {cForcast}")
        # self.assertEqual(fForcast, expectedFForcast, f"fForcast assertion failed:\nExpected: {expectedFForcast}\nActual: {fForcast}")
        # self.assertEqual(hForcast, expectedHForcast, f"hForcast assertion failed:\nExpected: {expectedHForcast}\nActual: {hForcast}")

        # # Test data pandas objects into feh2cel function
        # self.assertEqual(dayForcastCel, expectedCForcastCel, f"dayForcastCel assertion failed:\nExpected: {expectedCForcastCel}\nActual: {dayForcastCel}")
        # self.assertEqual(hourForcastCel, expectedFForcastCel, f"hourForcastCel assertion failed:\nExpected: {expectedFForcastCel}\nActual: {hourForcastCel}")
        # self.assertEqual(currentHourCel, expectedHForcastCel, f"currentHourCel assertion failed:\nExpected: {expectedHForcastCel}\nActual: {currentHourCel}")

        # # Test data pandas objects into feh2cel function
        # self.assertEqual(cForcastConv, expectedCForcastCel, f"cForcastConv assertion failed:\nExpected: {expectedCForcastCel}\nActual: {cForcastConv}")
        # self.assertEqual(fForcastConv, expectedFForcastCel, f"fForcastConv assertion failed:\nExpected: {expectedFForcastCel}\nActual: {fForcastConv}")
        # self.assertEqual(hForcastConv, expectedHForcastCel, f"hForcastConv assertion failed:\nExpected: {expectedHForcastCel}\nActual: {currentHourCel}")
        
        if self._outcome.success:
            headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
            headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
            headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']

            cForcast = str(tabulate(self.forcastCurrent, headers = headerCurrentHour, tablefmt = 'fancy_grid'))   
            fForcast = str(tabulate(self.forcastDay, headers = headerForcastDay, tablefmt = 'fancy_grid'))
            hForcast = str(tabulate(self.forcastHour, headers = headerForcastHour, tablefmt = 'fancy_grid'))
            print('\nYour test have passed!\n')
            print(f'\nHere is the mock weather data:\n\n{cForcast}\n{fForcast}\n{hForcast}\n')

if __name__ == '__main__':
    unittest.main()