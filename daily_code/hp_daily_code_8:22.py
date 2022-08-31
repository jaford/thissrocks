import os 
import shutil


source_des = '/Users/hunterpimparatana/Desktop'
final_des = '/Volumes/Workspace/CEDocs/TimeCard'

allfiles = os.listdir(source_des)

# Attempt 1 
# for x in allfiles:
#     shutil.move(source_des + x, final_des + x)

# Not as dynamic but allows all files on desktop to move to a directory. 
# we are using the absolute path! 
# THIS DOES NOT WORK SAD
for files in allfiles:
    source = source_des + files
    destination = final_des + files
    if os.path(source):
        shutil.move(source, destination)
        print('---Your file has been moved!----')

# # Next is to make this more dynamic! 

# print('-----File_directory_list-----')
# x = os.listdir(directory_path)
# # print(x)
# for root, dirs, filenames in os.walk(directory_path):
#     print(root)
#     for filename in filenames:
#         file_path = os.path.join(root, filename)
#         print(file_path)
#         if filename == 'Screenshot 2022-08-15 at 6.06.57 PM.png':
#             pass
