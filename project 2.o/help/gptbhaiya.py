import openai
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',195)
engine.setProperty('voice',voices[0].id)

openai.api_key = "Openai_api"

def speak(audio):
        engine.say(audio)
        print(f"Jarvis: {audio}")
        engine.runAndWait()


def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening you sir...")
            r.pause_threshold=1
            audio = r.listen(source,timeout=1,phrase_time_limit=5)
        try:
            print("Recognising plz wait a moment...")
            question = r.recognize_google(audio,language='en-in')
            print(f"You: {question}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return question

def ai_response(query):
    response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": query
    }
  ],
  temperature=1,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    reply = response.choices[0].message.content
    return reply

while True:
    query = takecommand().lower()
    if 'quit' in query:
       break
    elif query == "none":
        print("Continue")
    else:
       reply = ai_response(query)
       speak(reply)