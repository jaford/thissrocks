import time
import sys

def deleteLastLine(lineAmount):
    for x in range(lineAmount):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')