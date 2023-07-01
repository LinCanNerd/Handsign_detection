import PIL.ImageGrab
import os
from datetime import datetime
import pathlib
import playsound

def grab():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    im = PIL.ImageGrab.grab()
    desktop = pathlib.Path.home()
    desktop = str(desktop)+'\Desktop\Screenshots'
    try:
        os.mkdir(desktop)
    except:
        pass
    path =os.getcwd()
    os.chdir(desktop)
    im.save(dt_string +'.jpg','JPEG')
    os.chdir(path)
    playsound.playsound('saved_im.mp3')

