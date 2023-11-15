from gtts import gTTS

language = 'en'
stop = gTTS(text='detection stopped', lang = language, slow = False)
stop.save('stop.mp3')
try:
    myobj7 = gTTS(text = 'opening timer',lang = language, slow = False )
    myobj7.save('clock.mp3')
except:
    pass
try:
    myobj7 = gTTS(text ='opening notepad', lang = language, slow = False)
    myobj7.save('notepad.mp3')
except:
    pass
try:
    myobj7 = gTTS(text='Saved to the folder on your desktop')
    myobj7.save('saved_im.mp3')
except:
    pass
try:
    myobj6 = gTTS(text = 'what you wanna listen to?',lang = language, slow = False)
    myobj6.save('what_music.mp3')
except:
    pass
try:
    myobj5 = gTTS(text = 'opening calculator',lang = language,slow = False)
    myobj5.save('calculator.mp3')
except:
    pass
try:
    myobj4 = gTTS(text = 'opening google translate',lang = language, slow = False)
    myobj4.save('translator.mp3')
except:
    pass
try:
    myobj3 = gTTS(text = 'Please, say again', lang=language, slow=False)
    myobj3.save('repeat.mp3')
except:
    pass
try:
    myobj2 = gTTS(text = 'name your inquiry', lang=language, slow=False)
    myobj2.save('voice_signal.mp3')
except:
    pass
try:
    myobj = gTTS(text= 'Which city you want a forecast for?', lang=language, slow=False)
    myobj.save("Name_city.mp3")
except:
    pass
try:
    myobj = gTTS(text= 'detection start', lang=language, slow=False)
    myobj.save("start.mp3")
except:
    pass

