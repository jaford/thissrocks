from genericpath import isfile
from hashlib import new
import os
import datetime 
from datetime import date 
import shutil # This is can simply call os.rename but since this file is on a different partition, this copies the file over

source_file = '/Users/hunterpimparatana/Desktop/Screenshot 2022-08-11 at 3.23.01 PM.png' # Path to screenshots
print(type(source_file))

print('-----Stat_result-----')
stat_result = os.stat(source_file)
print(type(stat_result))
print(stat_result)

print('-----File_Creation_time-----')
# I am using this long methon from a class called datetime to get ctime from stat result to print out 
# the local file creatation time
file_creation_datetime = datetime.datetime.fromtimestamp(stat_result.st_ctime)
print(type(file_creation_datetime))
print('This file was created on:', file_creation_datetime)

print('-----File_Readable_Dates-----')
today = date.today()
print(f'This file was created on {today}')
# more ways to print out date
readable_date = today.strftime("%B %d, %Y")
print(readable_date)
