# program intended to countdown how many days until vacation
import datetime
from datetime import date

def vaca_countdown():
    print('----------This program is a countdown that will tell us how many days until your vacation----------')

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date1 = datetime.date(year, month, day)
date2 = date.today()

print(f"Today's date is {date2}. You leave for vacation on {date1}")
days_remaining = date1 - date2
print(f'There are {days_remaining} until you leave!  Pack your bags!')

vaca_countdown()