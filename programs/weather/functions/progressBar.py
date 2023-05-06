import time
import sys

def loadBar():
    print('\nLoading your information...')

    # IM A THEIF AND STOLE THIS CODE
    toolbarWidth = 40

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbarWidth))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbarWidth+1)) # return to start of line, after '['

    for i in range(toolbarWidth):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar

    return