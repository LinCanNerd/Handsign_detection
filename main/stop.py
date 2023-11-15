import playsound
from inspect import getsourcefile
from os.path import abspath
import os
def stop():
    sound_path = os.path.dirname(abspath(getsourcefile(lambda:0)))
    playsound.playsound(sound_path+'\stop.mp3')
    
#stop()