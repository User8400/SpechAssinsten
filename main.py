# -*- coding: utf-8 -*-

from email.mime import audio
import speech_recognition
from config import lang, pause_threshold

def speech():
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = pause_threshold

    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language=lang).lower()
        return query

def main():
    query = speech()
    print(query)

if __name__ == "__main__":
    main()
