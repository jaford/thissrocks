import unittest
import sys
import os
import pandas as pd
from datetime import date
from unittest.mock import patch
from pandas.testing import assert_frame_equal
from tabulate import tabulate

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directories containing main.py and functions.py to the sys.path
main_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'main'))
functions_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'functions'))
sys.path.insert(0, main_dir)
sys.path.insert(0, functions_dir)
from weatherData import getWeather