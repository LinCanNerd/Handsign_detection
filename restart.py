from inspect import getsourcefile
from os.path import abspath
import os
import playsound
def start():
    sound_path = os.path.dirname(abspath(getsourcefile(lambda:0)))
    playsound.playsound(sound_path+ '\start.wav')
#start()