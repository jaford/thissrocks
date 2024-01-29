import unittest
from unittest.mock import patch
import sys
import os

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directories containing main.py and functions.py to the sys.path
main_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'main'))
functions_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'functions'))
sys.path.insert(0, main_dir)
sys.path.insert(0, functions_dir)
from locationData import get_location_ip  # Replace 'your_module' with your module name

class TestGetLocationIP(unittest.TestCase):
    @patch('requests.get')  # Mock the requests.get function
    def test_get_location_ip(self, mock_get):
        mock_data = {
            'ip': '123.45.67.89',
            'city': 'TestCity',
            'region': 'TestRegion',
            'loc': '123.4567,-89.0123'
        }
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        expected_output = {
            'ip_address': '123.45.67.89',
            'city': 'testcity',  # Lowercased city
            'state': 'testregion',
            'gps_loc': '123.4567,-89.0123'
        }

        result = get_location_ip()
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
