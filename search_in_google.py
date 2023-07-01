import speech_recognition as sr
import webbrowser as wb
import playsound
from gtts import gTTS
import os

url = 'https://www.google.co.in/search?q='

r = sr.Recognizer() 
def record_audio(state):
    
    with sr.Microphone() as source: 
        if state == 'start':
            playsound.playsound('voice_signal.mp3', False) 
        if state =='repeat':
            playsound.playsound('repeat.mp3', False)  
        r.adjust_for_ambient_noise(source, duration=1.5)  
        audio = r.listen(source)
        action(audio)  
        print('audio saved')

def convert(audio):

    text = r.recognize_google(audio)
    myobj3 = gTTS(text = 'searching {} for you'.format(text), lang='en', slow=False)
    myobj3.save('search.mp3')
    playsound.playsound('search.mp3')
    os.remove('search.mp3')
    wb.open(url+text)


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