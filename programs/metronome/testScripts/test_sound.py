from playsound import playsound
# from pydub import AudioSegment
# from pydub.playback import play

'''
click = AudioSegment.from_mp3('programs/metronome/metronomeSounds/metronome-85688.mp3')
print('Testing to see if sound can actually be played!')
play(click)

I GET THIS STUPID ERROR BELLOW
FileNotFoundError: [Errno 2] No such file or directory: 'programs/metronome/metronomeSounds/metronome-85688.mp3'
'''

# click = 'programs/metronome/metronomeSounds/metronome-85688.mp3'
# playsound(click)
'''
For some reason the absoulte path works rather than relative. This seems unsable for this when other users download this. 
Will look into why this could be the case! 

Using the absolute path seems to work? Why? Who knows rip.png
'''
print('TEST #1\n')
playsound('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/metronome/metronomeSounds/metronome-85688.mp3')
print('Testing to see of sound can actually be played!')




