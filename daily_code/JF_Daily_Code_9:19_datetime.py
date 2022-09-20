# program intended to countdown how many days until vacation
import datetime
from datetime import date

def vaca_countdown():
    print('----------This program is a countdown that will tell us how many days until your vacation----------')
date1 = datetime.date(2022, 12, 13)
date2 = date.today()

print(f"Today's date is {date2}. You leave for vacation on {date1}")
days_remaining = date1 - date2
print(f'There are {days_remaining} until you leave!  Pack your bags!')