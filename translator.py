import webbrowser as wb
import playsound
def open():
    url = 'https://translate.google.com/?sl=auto&tl=en&op=translate'
    playsound.playsound('translator.mp3')
    wb.open(url)
