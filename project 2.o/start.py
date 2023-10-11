import os
import speech_recognition as oo

def takecommand():
    r = oo.Recognizer()
    with oo.Microphone() as source:
        print("Listening you sir...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
        try:
            print("Recognising plz wait a moment...")
            question = r.recognize_google(audio,language='en-in')
            print(f"You: {question}")
        except Exception as e:
            print("Say that again please...")
            return "none"
        return question
    
while True:
    wake = takecommand().lower()
    if "wake up jarvis" in wake:
        os.startfile("jarvis.py")
    else:
        print("ok")