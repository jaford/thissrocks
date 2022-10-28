#This is a python script that will countdown how much time you have left until your shift ends

from datetime import datetime
from datetime import date

#now = date.today()
now = datetime.now()
# print(now)
# print(type(now))

end = input("What time does your shift end? Enter time in: YYYY-MM-DD-HH-MM: ")
end_formatted = datetime.strptime(end, '%Y-%m-%d-%H-%M')

# print(end_formatted)
# print(type(end_formatted))

time_delta = end_formatted - now
print(f'YOUR SHIFT ENDS IN: {time_delta}')
