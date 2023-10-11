import pyttsx3 
from bardapi import BardCookies
import datetime
import pyttsx3
import sys
import os

cookie_dict ={
    "__Secure-1PSID":"agiOITuMm8p_TNYzxbAAcTuq-vglkC_c0e3fs_klfyRQquenT3yEXKIQZSBM6ng2GIzKPA.",
    "__Secure-1PSIDTS":"sidts-CjIBSAxbGez0a9jKyN5r7JkhRlZK0P8zwfnt7Qv9TbcJVK7KqRdvittayqgkwU-CfREfHRAA",
    "__Secudr-1PSIDCC":"APoG2W-ZgD7D7G9BAu9IVWMgZ-J3gIdi5throos3k2-NhqL151t9aWJJ-0b5ry4tJ5osIUerdg"
    

}

bard = BardCookies(cookie_dict=cookie_dict)

samay_g = datetime.datetime.now().hour
samay_m = datetime.datetime.now().minute

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',195)
engine.setProperty('voice',voices[0].id)



def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak(f"Good morning,it's {samay_g}:{samay_m} A.M.")
    elif hour>12 and hour<18:
        speak(f"Good afternoon,it's {samay_g}:{samay_m} P.M.")
    else:
        speak(f"Good evening,it's {samay_g}:{samay_m} P.M.")
    speak("I am Jarvis. Plz tell me sir how can i help you")

def speak(audio):
    engine.say(audio)
    print(f"Jarvis: {audio}")
    engine.runAndWait()


def Taskexecution():
    while True:

        query = input("Enter your query:")

        if "start voicebot" in query:
            os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\project 2.o\\jarvis.py")
        elif "sleep" in query:
            sys.exit()
        elif "exit" in query:
            sys.exit()       
        elif "your name" in query:
            speak("My name is jarvis and i am a virtual ai assistant")
        else:
            reply = bard.get_answer(query)['content']
            print(reply)
        

Taskexecution()
