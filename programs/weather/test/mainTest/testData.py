# -*- coding: utf-8 -*-
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from tabulate import tabulate
import sys
import os

sys.path.append('..')
from mockTestData.mockWeatherData import weatherDataTest

# Remove the parent directory from sys.path
if '..' in sys.path:
    sys.path.remove('..')

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directories containing main.py and functions.py to the sys.path
main_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'main'))
functions_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'functions'))
sys.path.insert(0, main_dir)
sys.path.insert(0, functions_dir)
from dataCompile import dataFormating
from feh2celConv import feh2cel


# def mockWeatherData():
#     # Simulate API response or generate mock weather data
#     forcastCurrent = {
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

#     forcastDay = {
#         'forcastDate': ['06/11/2023 ', '06/12/2023 ', '06/13/2023 '],
#         'futureTemp': ['88', '86', '89'],
#         'highTemp': ['90', '88', '92'],
#         'lowTemp': ['84', '81', '82']
#     }

#     forcastHour = {
#         'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
#         'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
#         'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
#     }
    

#     return forcastDay, forcastHour, forcastCurrent

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        # Set up the necessary test fixtures
        forcastDay, forcastHour, forcastCurrent = weatherDataTest()
        self.forcastDay = forcastDay  # Assigning value to instance variable
        self.forcastHour = forcastHour  # Assigning value to instance variable
        self.forcastCurrent = forcastCurrent  # Assigning value to instance variable
        
        hForcast, fForcast, cForcast = dataFormating(self.forcastDay, self.forcastHour, self.forcastCurrent)
        # tabulate objects (AKA strings)
        # Can be used to test the printing format!
        self.hForcast = hForcast
        self.fForcast = fForcast
        self.cForcast = cForcast

        dayForcastCel, hourForcastCel, currentHourCel, cForcastConv, fForcastConv, hForcastConv = feh2cel(self.forcastDay, self.forcastHour, self.forcastCurrent)
        # pandas objects
        self.dayForcastCel = dayForcastCel
        self.hourForcastCel = hourForcastCel
        self.currentHourCel = currentHourCel
        
        self.cForcastConv = cForcastConv
        self.fForcastConv = fForcastConv
        self.hForcastConv = hForcastConv

    def test_dataFormating(self):
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

        expectedConvCForcast = pd.DataFrame(expectedforcastCurrentCel)
        expectedConvDForcast = pd.DataFrame(expectedforcastDayCel)
        expectedConvHForcast = pd.DataFrame(expectedforcastHourCel)

        # Assertions (RUN IN PYTHON3)
        # Test data
        self.assertEqual(self.forcastCurrent, expectedCForcast, f"forcastCurrent assertion failed:\nExpected: {expectedCForcast}\nActual: {self.forcastCurrent}")
        self.assertEqual(self.forcastDay, expectedDForcast, f"forcastDay assertion failed:\nExpected: {expectedDForcast}\nActual: {self.forcastDay}")
        self.assertEqual(self.forcastHour, expectedHForcast, f"forcastHour assertion failed:\nExpected: {expectedHForcast}\nActual: {self.forcastHour}")

        # Test data converted to cel
        self.assertEqual(self.cForcastConv, expectedforcastCurrentCel, f"cForcastConv assertion failed:\nExpected: {expectedforcastCurrentCel}\nActual: {self.cForcastConv}")
        self.assertEqual(self.fForcastConv, expectedforcastDayCel, f"fForcastConv assertion failed:\nExpected: {expectedforcastDayCel}\nActual: {self.fForcastConv}")
        self.assertEqual(self.hForcastConv, expectedforcastHourCel, f"hForcastConv assertion failed:\nExpected: {expectedforcastHourCel}\nActual: {self.hForcastConv}")

        # self.assertEqual(self.dayForcastCel, expectedConvDForcast, f'hForcast assertion failed:\nExpected: {expectedConvDForcast}\nActual: {self.dayForcastCel}')
        # assert_frame_equal(self.dayForcastCel, expectedConvDForcast, check_dtype=False)

        # self.assertEqual(self.currentHourCel, expectedConvCForcast, f'cForcast assertion failed:\nExpected: {expectedConvCForcast}\nActual: {self.currentHourCel}')
        # assert_frame_equal(self.currentHourCel, expectedConvCForcast, check_dtype=False)

        # self.assertEqual(self.hourForcastCel, expectedConvHForcast, f'hForcast assertion failed:\nExpected: {expectedConvHForcast}\nActual: {self.hourForcastCel}')
        # assert_frame_equal(self.hourForcastCel, expectedConvHForcast, check_dtype=False)


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
        # self.assertEqual(self.cForcastConv, expectedCForcastCel, f"cForcastConv assertion failed:\nExpected: {expectedCForcastCel}\nActual: {cForcastConv}")
        # self.assertEqual(self.fForcastConv, expectedFForcastCel, f"fForcastConv assertion failed:\nExpected: {expectedFForcastCel}\nActual: {fForcastConv}")
        # self.assertEqual(self.hForcastConv, expectedHForcastCel, f"hForcastConv assertion failed:\nExpected: {expectedHForcastCel}\nActual: {currentHourCel}")
        
        if self._outcome.success:
            headerForcastDay = ['Forcast Date', 'Tempature', 'Highest Tempature', 'Lowest Tempature']
            headerCurrentHour = ['Current Date', 'Current Time', 'Current Tempature', 'What it feels like', 'Humidity', 'Visibility', 'Precipitation', 'Wind speed', 'Wind direction']
            headerForcastHour = ['Forcast Hour', 'Tempature', 'Description']
            cForcastConv = tabulate(expectedConvCForcast, headers = headerCurrentHour, tablefmt = 'fancy_grid')
            fForcastConv = tabulate(expectedConvDForcast, headers = headerForcastDay, tablefmt = 'fancy_grid')            
            hForcastConv = tabulate(expectedConvHForcast, headers = headerForcastHour, tablefmt = 'fancy_grid')
            self.cForcastConv = cForcastConv
            self.fForcastConv = fForcastConv
            self.hForcastConv = hForcastConv

            print('\nYour intial data test have passed!\n')
            print(f'\nHere is the mock weather data:\n\n{self.cForcast}\n{self.fForcast}\n{self.hForcast}\n')
            print(f'\nHere is the mock weather data (in Cel):\n\n{self.cForcastConv}\n{self.fForcastConv}\n{self.hForcastConv}\n')

if __name__ == '__main__':
    unittest.main()