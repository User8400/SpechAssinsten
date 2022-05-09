from cgitb import text
from gtts import gTTS
import pyttsx3
from playsound import playsound

def text_to_sound(Text=text, language='ru', GTTS_API=False):
    if GTTS_API:        
        my_audio = gTTS(Text,lang=language, slow=False)
        my_audio.save("tmpsound.mp3")
        playsound("tmpsound.mp3")        
        #удалить __tmpsound.mp3
    else:
        engine = pyttsx3.init()
        engine.say(Text)
        engine.runAndWait()
