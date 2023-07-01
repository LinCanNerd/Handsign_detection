
import webbrowser
import urllib.request
import re
import os
import speech_recognition as sr
import playsound
from gtts import gTTS

r = sr.Recognizer() 
def listen(state):
    with sr.Microphone() as source: 
        if state == 'start':
            playsound.playsound('what_music.mp3', False) 
        if state =='repeat':
            playsound.playsound('repeat.mp3', False)  
        r.adjust_for_ambient_noise(source, duration=1.5)  
        audio = r.listen(source)
        action(audio)  
        print('audio saved')
def convert(audio):
    text = r.recognize_google(audio)
    myobj3 = gTTS(text = 'opening {} for you'.format(text), lang='en', slow=False)
    myobj3.save('search.mp3')
    playsound.playsound('search.mp3')
    start(text)
    os.remove('search.mp3')

def action(audio):
    try:
        convert(audio)
    except sr.UnknownValueError:  
        listen('repeat')
        print("I could not understand audio")  
    except sr.RequestError as e:  
        print("error; {0}".format(e))
    except Exception as e:
        print (e)

def start(text):
    search_keyword= '+'.join(text.split())
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    link = "https://www.youtube.com/watch?v=" + video_ids[0]
    webbrowser.open(link,autoraise=False)
#listen('start')