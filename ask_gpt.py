import openai
import playsound
import speech_recognition as sr
import webbrowser as wb
import playsound
from gtts import gTTS
import os

openai.api_key = "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"


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

    question = r.recognize_google(audio)
    print(question)
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "user", "content": "question"}],
    max_tokens = 1024,
    temperature = 0.8)

    myobj3 = gTTS(text = response.choices[0].message.content, lang='en', slow=False)
    myobj3.save('search.mp3')
    playsound.playsound('search.mp3')
    os.remove('search.mp3')



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
record_audio('start')




