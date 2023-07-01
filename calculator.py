from subprocess import call
import playsound
def open():
    playsound.playsound('calculator.mp3')
    call(["calc.exe"])