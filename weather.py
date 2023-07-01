import requests
from gtts import gTTS
import playsound
import speech_recognition as sr
import os
from tkinter import *
from tkinter.ttk import *
import webbrowser as wb


r = sr.Recognizer() 

def record_audio(state):
    
    with sr.Microphone() as source: 
        if state == 'start':
            playsound.playsound('Name_city.mp3', False) 
        if state =='repeat':
            playsound.playsound('repeat.mp3', False) 

    # listen for 2.5 seconds and create the ambient noise energy level  
        r.adjust_for_ambient_noise(source, duration=2.5)  
        print('starting audio')
        audio = r.listen(source)  
        print('audio is done')
    action(audio)

def convert(audio):
    text = r.recognize_google(audio)
    print(text)
    url = 'https://wttr.in/{}'.format(text)
    res = requests.get(url)
    
    #print(res.text[0:len(res.text)-54])
    wb.open('https://wttr.in/{}'.format(text),new=1)

# recognize speech 
def action(audio):
    try:
        convert(audio)
    except sr.UnknownValueError:  
        record_audio('repeat')
        print("I could not understand audio")  
    except sr.RequestError as e:  
        print("error; {0}".format(e))
    except Exception as e:
        print (e)
#record_audio('start')



  
