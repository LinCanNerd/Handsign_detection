from subprocess import call
import playsound
import webbrowser as wb
def open():
    playsound.playsound('clock.mp3')
    wb.open('https://www.google.com/search?q=timer')
#open()