import os
import shutil

old_file_name = '/Users/hunterpimparatana/Desktop/Screenshot 2022-08-15 at 6.06.57 PM.png'
new_file_name = '/Volumes/Workspace/CEDocs/TimeCard/August_15th.png'

# os.rename(old_file_name, new_file_name)
# We can also check whether it the file already exists!
if os.path.isfile(new_file_name):
    print('-----This file already exists!-----')
else:
    # Renames file 
    shutil.move(old_file_name, new_file_name)
    print('-----File has been renamed & moved-----')

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
