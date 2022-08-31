"""
Python Datetime 

A date in python is not a data type but we can import a module named 
datetime to work with dates as date objects
"""
import datetime

x = datetime.datetime.now()
print(x)

# You can print and show different variations of the time as well.
print(x.year)
print(x.strftime('%A'))
