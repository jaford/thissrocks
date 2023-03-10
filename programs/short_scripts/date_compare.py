import datetime

current_date = datetime.date.today()
print('Current date: {}\n'.format(current_date))

future_date = datetime.date(2022, 11, 4)
print('Last day of CE: {}\n'.format(future_date))

dif = future_date - current_date
# print(dif, '\n')
print('Days left of CE: {}'.format(dif))

