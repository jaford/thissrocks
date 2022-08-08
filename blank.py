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
print(stat_result)

file_creation_datetime = datetime.datetime.fromtimestamp(stat_result.st_ctime)
print(file_creation_datetime)
print(type(file_creation_datetime))
print(dir(file_creation_datetime))


json_file = open(path)
first_line = json_file.readline()
rest_of_file = json_file.read()
json_object = json.loads(rest_of_file)
Active_memory_pages = json_object.get("memory_status")

#Active_memory_pages = json_object["memory_status"]["memoryPages"]["active"]

#pprint.pprint(json_object)

json_file.close()

