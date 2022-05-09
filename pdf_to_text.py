from cgitb import text
from pathlib import Path
import pdfplumber

def pdfReader(file_path = '', language = 'ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text()  for page in pdf.pages]
        text = ''.join(pages)

        with open('temp/textfrompdf.txt', 'w') as file:
            file.write(text)
