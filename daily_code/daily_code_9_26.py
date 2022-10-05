"""
Experimenting with some counters. Might makea a program similar to Jims where it counts down the days till 
my last day! 

This might be a couple of variations
"""
import datetime
import time

from datetime import datetime
from datetime import date
from datetime import timedelta

print('----Practice 1----')
start = time.time()
print('Hello')
end = time.time()
print(end - start)

print('\n')
print('----Practice 2----')

# Datetime string
datetime_str = '26SEP2022101010'

# Call datetime.strptime to convert it into datetime datatype 
datetime_obj = datetime.strptime(datetime_str, '%d%b%Y%H%M%S')

# Printing object
print(datetime_obj)

# Extract the time from datetime_obj
time = datetime_obj.time()
# Printing out that we have exctracted from datetime obj
print(time) 

print('\n')
print('----Practice 3----')
datetime_str = '26SEP2022101010'
datetime_obj = datetime.strptime(datetime_str, '%d%b%Y%H%M%S')
print('date time: {}'.format(datetime_obj))

time = datetime_obj.time()
print('Time: {}'.format(time))

hour = time.hour
print('Hour: {}'.format(hour))

print('\n')
print('----Practice 4----')
# Using now() to get current time
current_time = datetime.now()

# Printing value of now. 
print('Time now at ABQ, New Mexico: {}'.format(current_time))

print('\n')
print('----Practice 5----')
current_time = datetime.now()

# Printing attributes of now()
current_year = current_time.year
print('Year: {}'.format(current_year))

current_month = current_time.month
print('Month: {}'.format(current_month))

current_day = current_time.day
print('Day: {}'.format(current_day))

current_hour = current_time.hour
print('Hour: {}'.format(current_hour))

print('\n')
print('----Practice 6----')

today = date.today()
print('Today date is: {}'.format(today))

print('\n')
print('----Practice 7----')

time = datetime.now().time()
print('Current Time: {}'.format(time))

print('\n')
print('----Practice 7----')

# No formatting time
now = datetime.now()
print('No formatting: {}'.format(now))

# String formatting
s = now.strftime('%a %m %y')
print('Format 1: {}'.format(s))

s = now.strftime('%A %-m %Y')
print('Format 2: {}'.format(s))

s = now.strftime('%-I %p %S')
print('Format 3: {}'.format(s))

s = now.strftime('%-j')
print('Format 4: {}'.format(s))

print('\n')
print('----Practice 8----')

# Creates timedelta object with differance of 1 weeks
d1 = timedelta(weeks=1)
# Same applies to this as well but in days.
d2 = timedelta(days=30)

print(d1)
print(d2)

print('\n')
print('----Practice 9----')

current_time = datetime.now()

# Printing intial date
print('Current date and time: {}'.format(current_time))

# Calculating future dates
# One for 2 years!
future_date_1 = current_time + timedelta(days = 730)
future_date_2 = current_time + timedelta(days = 15)

print('Future date 1: {}'.format(future_date_1))
print('Future date 2: {}'.format(future_date_2))

print('\n')
print('----Practice 10----')

d1 = date(2021, 3, 16)
d2 = date(2022, 3, 31)

diff = d2 - d1
print('Differance: {} Days'.format(diff.days))
