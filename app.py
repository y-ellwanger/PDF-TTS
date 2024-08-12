from PyPDF2 import PdfReader
import pyttsx3
from multiprocessing import Process
import keyboard
import os

def read_text(text):
    print("\nReading text... \nPress Esc to cancel\n")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def read_pdf():
    path=input("Insert path to the file (e.g.: path\\file.pdf): ")
    if os.path.exists(path):
        reader = PdfReader(path)
        print("\nNumber of pages: ",len(reader.pages))
        interval = input("\nInsert the interval of pages to be read (e.g.: 1-5, to read from page 1 to page 5, or 2-2 to read only page 2): ")
        interval = interval.split("-")
        text = ""
        for page_number in range(int(interval[0])-1,int(interval[1])):
            text+=reader.pages[page_number].extract_text()
        return text
    else:
        return False

def say(text):
    p = Process(target=read_text, args=(text,))
    p.start()
    while p.is_alive():
        if keyboard.is_pressed("esc"):
            p.kill()
        else:
            continue
    p.join()

if __name__=="__main__":
    extracted_text= read_pdf()
    match extracted_text:
        case "":
            print("No text to be read")
        case False:
            print("Path to the file does not exists")
        case _:
            say(extracted_text)