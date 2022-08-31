import os
import shutil

<<<<<<< HEAD
old_file_name = '/Users/hunterpimparatana/Desktop/Screenshot 2022-08-30 at 6.18.23 PM.png'
new_file_name = '/Volumes/Workspace/CEDocs/TimeCard/August_30th.png'
=======
old_file_name = '/Users/hunterpimparatana/Desktop/Screenshot 2022-08-22 at 6.39.26 PM.png'
new_file_name = '/Volumes/Workspace/CEDocs/TimeCard/August_22nd.png'
>>>>>>> d6924eb82824dff59ad7c5b511667fae590ea484

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
