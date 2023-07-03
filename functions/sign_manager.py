import os 
from actions import weather
from actions import search_in_google
from actions import translator
from actions import calculator, open_music, screenshot, create_txt, stop, restart, clock
def sign_manager(key):
    if key =='A':
        create_txt.open()
    if key == 'B':
        stop.stop()
    if key == 'C':
        calculator.open()
    if key == 'D':
        clock.open()
    if key =='I':
        restart.start()
    if key == 'L':
        screenshot.grab()
    if key =='V':
        open_music.listen('start')
    if key =='T':
        translator.open()
    if key == 'G':
        search_in_google.record_audio('start')
    if key == 'W':
        weather.record_audio('start')
        
    else:
        print('no function for this sign yet')
