import os 
import weather
import search_in_google
import translator
import calculator
import open_music
import screenshot, create_txt
import stop,restart
import clock
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
