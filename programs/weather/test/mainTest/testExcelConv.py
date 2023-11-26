import unittest
import sys
import os
import pandas as pd
from datetime import date
from unittest.mock import patch
from pandas.testing import assert_frame_equal
from tabulate import tabulate

sys.path.append('..')
from mockTestData.mockWeatherExcelData import mockExcelWeatherData

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
from excelConv import excelConv

class testExcelConv(unittest.TestCase):
    def setUp(self):
        self.mock_to_excel = patch('excelConv.pd.DataFrame.to_excel').start()
        self.mock_exists = patch('excelConv.os.path.exists').start()
        self.mock_exists.return_value = False  # Mock that the file does not exist initially

    def tearDown(self):
        patch.stopall()

    def test_excelConv(self):
        current_date = date.today().strftime('%Y-%m-%d')
        expectedCForcast, expectedDForcast, expectedHForcast, expectedforcastCurrentCel, expectedforcastDayCel, expectedforcastHourCel = mockExcelWeatherData()
        test_city = "New York"
        test_data_list = [
            expectedCForcast, 
            expectedDForcast, 
            expectedHForcast, 
            expectedforcastCurrentCel, 
            expectedforcastDayCel, 
            expectedforcastHourCel
        ]
        excelConv(test_data_list, test_city)

        # Assertions to check if the file creation logic was called
        self.mock_to_excel.assert_called()  # Check if the to_excel method was called
        self.mock_exists.assert_called_with(f'~/Downloads/weatherData_{current_date}_{test_city}.xlsx')  # Check if os.path.exists was called with the expected file path
