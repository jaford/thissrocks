"""
Experimenting with some counters. Might makea a program similar to Jims where it counts down the days till 
my last day! 

This might be a couple of variations
"""
from datetime import *

# Enter dates and store into date class object
d1, m1, y1 = [int(x) for x in input('Enter first date (DD/MM/YYYY) : ').split('/')]

b1 = date(y1, m1, d1)

d2, m2, y2 = [int(x) for x in input('Enter second date (DD/MM/YYYY) : ').split('/')]

b2 = date(y2, m2, d2)

# Checking the dates 
if b1 == b2: 
    print('These dates are the same!')
elif b1 > b2:
    print('The first date is greater')
else: 
    print('The second date is greater')