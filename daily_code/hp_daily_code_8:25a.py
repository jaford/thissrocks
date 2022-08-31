"""
Python Modules

Consider a python module to be like a code libary. 

A file containing a set of functions you want to include in your application. 

To create a module, make a new file and import the code like so bellow.
"""
# Import sys
# import sys

# # adding directory to the system path
# sys.path.append('/Volumes/Workspace/CEDocs/Test_Source/thissrocks/modules/my_module.py')

# Importing the function from said file
import sys 
from modules.my_module import greating

# calling greeting function 
modules.my_module.greating('Hunter')

# This one is very confusing :( 