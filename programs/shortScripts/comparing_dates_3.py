import datetime
from datetime import date, datetime

# current_date = date.today()
current_date = datetime.combine(date.today(), datetime.min.time())  # Convert date to datetime
print('Todays date: {}\n'.format(current_date))

# date and time
current_date_time = datetime.now()
print('Todays date and time: {}\n'.format(current_date_time))

# format dd/mm/yy H:M:S
format_datetime = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
print('Date and time: {}\n'.format(format_datetime))

future_date = datetime(2024, 11, 4)  # Correction here
date_difference = future_date - current_date
print('Days until the last day: {}\n'.format(date_difference.days))

date_differance = future_date - current_date
print('Days until last day: {}\n'.format(date_differance))

# Big failed one. Dont know why this does not work 
# BIG SAD