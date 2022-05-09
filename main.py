# -*- coding: utf-8 -*-

from voice2text import speech
from text2mp3 import text_to_sound

def main():
    query = speech()
    print(query)
    if query=='привет':
        text_to_sound('Привет', language='ru')

if __name__ == "__main__":
    main()
