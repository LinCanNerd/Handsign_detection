from subprocess import call
import playsound
def open():
    playsound.playsound('notepad.mp3')
    call(["notepad.exe"])
#open()