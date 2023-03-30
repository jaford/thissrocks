"""
This code was written with James! 

This was the start to help make a program that would easliy rewrite a files name based upon date and time,
then move the file into a spefic directory after the file was re-written! 
"""
from http.client import ImproperConnectionState
import imp
import json
import os
import pprint
import os
import datetime


path = "/Volumes/Workspace/RadarDocs/Postponed_assignment/Radar(97039108)/sysdiagnose_2022.07.12_22-33-04-0700_iPhone-OS_iPhone_20A319a/crashes_and_spins/JetsamEvent-2022-07-12-173059.ips"

os.stat('/Volumes/Workspace/RadarDocs/Postponed_assignment/Radar(97039108)/sysdiagnose_2022.07.12_22-33-04-0700_iPhone-OS_iPhone_20A319a/crashes_and_spins/JetsamEvent-2022-07-12-173059.ips')

stat_result = os.stat(path)
print('-----This is stat result of path-----')
print(stat_result)

file_creation_datetime = datetime.datetime.fromtimestamp(stat_result.st_ctime)
print('-----File creation date time-----')
print(file_creation_datetime)
print('-----The type-----')
print(type(file_creation_datetime))
print('-----The valid attributes of variable-----')
print(dir(file_creation_datetime))


json_file = open(path)
first_line = json_file.readline()
rest_of_file = json_file.read()
json_object = json.loads(rest_of_file)
Active_memory_pages = json_object.get("memory_status")

#Active_memory_pages = json_object["memory_status"]["memoryPages"]["active"]

#pprint.pprint(json_object)

json_file.close()

