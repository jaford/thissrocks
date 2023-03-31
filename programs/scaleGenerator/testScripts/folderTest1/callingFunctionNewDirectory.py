# from folderTest2 import subtration, printTest # pylint: disable=import-error
import sys

# sys.path.append(0, '/thissrocks/programs/scale_generator/testScripts/folderTest2')
# sys.path.instert(0, '')

# sys.path.append('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/scale_generator/testScripts/folderTest1')
# sys.path.insert(1, '/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/scale_generator/testScripts/folderTest1')
# sys.path.append('/scale_generator/testScripts/folderTest2')
sys.path.append('..')

from folderTest2.folderFunctions import subtration, printTest
result = subtration(20, 5)
printTest()
print('Here is your result: "{}"'.format(result))
