'''
This is finally the workable version that prints line by line 
in seconds the quarter notes in BPM! A lot easier than I thought! 

Task --> Make text error a red color to stand out!
'''
import time
import datetime

try:

    user_bpm = float(input("Enter BPM: "))
    quarter_seconds = (60/user_bpm)
    '''
    This above will covert the users BPM to quarter notes.
    This is also to convert BPM to how many seconds a quater last in the desired BPM.
      
    '''

    tstep = datetime.timedelta(seconds=quarter_seconds)
    tnext = datetime.datetime.now() + tstep

    while True: 
        tdiff = tnext - datetime.datetime.now()
        time.sleep(tdiff.total_seconds())
        tnext = tnext + tstep
        print('Boop')

except Exception as err: 
    print("An error occured --> : {}".format(err))