# -*- coding: utf-8 -*-

from voice2text import speech
from text2mp3 import text_to_sound
from pdf_to_text import pdfReader

def main():
    pdfReader(file_path='temp/text.pdf', language='ru')
    
    #query = speech()    
    #if query=='привет':
    #    text_to_sound('Привет', language='ru')

if __name__ == "__main__":
    main()
