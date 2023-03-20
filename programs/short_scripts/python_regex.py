# making a tester for regex
import re

string = '            associationLength = "TIME_BUCKET_LT_ONE_HOUR";'
match = re.search(r"\s*associationLength\s=\s\"(.+)\";", string)

if match:
    print('Found', match.group(1))
else:
    print('Did not find')