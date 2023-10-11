import typing
from PyQt5.QtWidgets import QWidget
import pyttsx3
import speech_recognition as sr
import sys
import datetime
import os
import cv2
from playsound import playsound as play
from requests import get
import ctypes
import wikipedia 
import webbrowser
import pywhatkit as kit
from pyautogui import click
from keyboard import press,press_and_release
from keyboard import write
from time import sleep,localtime
import time
import smtplib
import openai
import pyjokes
import pyautogui
import requests
import json
from PyQt5 import QtGui , QtCore , QtWidgets
import instaloader
import operator
from PyQt5.QtCore import QTimer , QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindow
from bardapi import BardCookies
from tkinter import *
import random
from tkvideo import tkvideo
import psutil
import speedtest
from bs4 import BeautifulSoup
import winsound
from Try.texttoimage import textimage 


openai.api_key = "Openai_Api"

cookie_dict ={
    "__Secure-1PSID":"bwiOIWZDIEJdI-ZwEOYst3h-a3vicnQiWbN5g9PrGSh5UP_iCxtfcnp-pMkEOFG0GokVLw.",
    "__Secure-1PSIDTS":"sidts-CjIB3e41hdWnF5OHTIJCHGCSYbI_5YfJ0FL9iOTBVJoeHhTmJMy8eAxye0o_NkQrs2bz8xAA",
    "__Secudr-1PSIDCC":"ACA-OxOJAnhIL9kleDyRh02GbgPq3j5BZHDXGX7CXo_05BwAsjLZ5p9S42oj3W4FsCy88QfTVg"

}

Api_key2 = "4d9a0d5440d58623d1884bc7d82b091a"

bard = BardCookies(cookie_dict=cookie_dict)

samay_g = datetime.datetime.now().hour
samay_m = datetime.datetime.now().minute

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',195)
engine.setProperty('voice',voices[0].id)

# def dateeee():
#     date = input("Enter the date here:")
#     return date

def game(computerturn,pturn):
    if computerturn == pturn:
        return None
    elif(computerturn == 'r'):
        if(pturn == 'p'):
            return True
        elif(pturn == 's'):
            return False
    elif(computerturn == 'p'):
        if(pturn == 'r'):
            return False
        elif(pturn == 's'):
            return True
    elif(computerturn == 's'):
        if(pturn == 'r'):
            return True
        elif(pturn == 'p'):
            return False

def move_mouse(direction, distance):
  if direction == "up":
    pyautogui.moveRel(0, -distance)
  elif direction == "down":
    pyautogui.moveRel(0, distance)
  elif direction == "left":
    pyautogui.moveRel(-distance, 0)
  elif direction == "right":
    pyautogui.moveRel(distance, 0)

def whatsappmsg(name,message):
    wpath = "C:\\Users\\bhavy\\OneDrive\\Desktop\\WhatsApp.lnk"
    os.startfile( wpath )
    sleep(7)
    click(x=258, y=130)
    sleep(2)
    write(name)
    sleep(2)
    click(x=281, y=205)
    sleep(2)
    click(x=783, y=692)
    sleep(2)
    write(message)
    press("Enter")

def whatscall(name):
    wpath = "C:\\Users\\bhavy\\OneDrive\\Desktop\\WhatsApp.lnk"
    os.startfile( wpath )
    sleep(7)
    click(x=258, y=130)
    sleep(1)
    write(name)
    sleep(1)
    click(x=281, y=205)
    sleep(1)
    click(x=1263, y=72)

def whatsvcall(name):
    wpath = "C:\\Users\\bhavy\\OneDrive\\Desktop\\WhatsApp.lnk"
    os.startfile( wpath )
    sleep(7)
    click(x=258, y=130)
    sleep(1)
    write(name)
    sleep(1)
    click(x=281, y=205)
    sleep(1)
    click(x=1214, y=74) 



def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('bdisop1234@gmail.com','Bhavya4343@43431')
    server.sendmail('bdisop1234@gmail.com',to,content)
    server.close()





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

Api_key = "KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK"

class Main(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("images\\7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("images\\Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("images\\Mr3W.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("images\\O1SC.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("images\\Nv2.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100000)
        self.showTime()
        self.TaskExecution()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = now.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_date)
        self.ui.textBrowser_3.setText(label_time)
    
    def termi(self,text):
        self.ui.terminalOutput.appendPlainText(text)

    def news(self):
        main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=381230afe00f4ea292c59a338263ff23"
        main_page = requests.get(main_url).json()
        article=main_page["articles"]
        head=[]
        day=["first","second","third","fourth",'fifth',"sixth",'seventh','eighth','ninth','tenth']
        for ar in article:
            head.append(ar["title"])
        for i in range(len(day)):
            self.speak(f"Today's {day[i]} news is:{head[i]}")

    def wish(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<=12:
            self.speak(f"Good morning,it's {samay_g}:{samay_m} A.M.")
        elif hour>12 and hour<18:
            self.speak(f"Good afternoon,it's {samay_g}:{samay_m} P.M.")
        else:
            self.speak(f"Good evening,it's {samay_g}:{samay_m} P.M.")
        self.speak("I am Jarvis. Plz tell me sir how can i help you")

    def speak(self,audio):
        engine.say(audio)
        self.termi(f"Jarvis: {audio}")
        engine.runAndWait()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.termi("Listening you sir...")
            r.pause_threshold=1
            audio = r.listen(source,timeout=1,phrase_time_limit=5)
        try:
            self.termi("Recognising plz wait a moment...")
            question = r.recognize_google(audio,language='en-in')
            self.termi(f"You: {question}")

        except Exception as e:
            self.speak("Say that again please...")
            return "none"
        return question
    


    def youtubeauto(self):
        self.speak("The control is in my hand...")
        while True:
            quer = self.takecommand().lower()
            if "pause" in quer:
                press("space bar")
            elif "resume" in quer:
                press("space bar")
            elif "full screen" in quer:
                press("t")
            elif "forward" in quer:
                press("l")
            elif "backward" in quer:
                press("j")
            elif "increase speed" in quer:
                press_and_release("shift + .")
            elif "decrease speed" in quer:
                press_and_release("shift + ,")
            elif "small screen" in quer:
                press("escape")
            elif "previous video" in quer:
                press_and_release("shift + p")
            elif "next video" in quer:
                press_and_release("shift + n")
            elif "previous frame" in quer:
                press("space bar")
                sleep(1)
                press(",")
            elif "next frame" in quer:
                press("space bar")
                sleep(1)
                press(".")
            elif 'mute' in quer:
                press("m")
            elif "search" in quer:
                click(x=464, y=93)
                sleep(1)
                self.speak("What to search sir?")
                sear = self.takecommand()
                write(sear)
                sleep(1)
                press("enter")
            elif "close youtube" in quer:
                self.speak("Giving you controls...")
                press_and_release("ctrl + w")
                break
            elif "give me controls" in quer:
                self.speak("Giving you controls...")
                break
            elif "up" in quer:
                move_mouse("up", 100)
                self.speak("Moved...")
            elif "down" in quer:
                move_mouse("down", 100)
                self.speak("Moved...")
            elif "left" in quer:
                move_mouse("left", 100)
                self.speak("Moved...")
            elif "right" in quer:
                move_mouse("right", 100)
                self.speak("Moved...")
            elif "click" in quer:
                mouse_position = pyautogui.position()
                pyautogui.click(mouse_position)
                self.speak("Clicked")
            elif "double" and "click" in quer:
                mouse_position = pyautogui.position()
                pyautogui.click(mouse_position)
                pyautogui.click(mouse_position)
                self.speak("clicked")

    def printboard(self,xstate,zstate):
        zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
        one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
        two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
        three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
        four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
        five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
        six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
        seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
        eight = 'X' if xstate[8] else ('O' if zstate[8] else 8)
        self.termi(f" {zero} | {one} | {two}")
        self.termi("---|---|---") 
        self.termi(f" {three} | {four} | {five}")
        self.termi("---|---|---")
        self.termi(f" {six} | {seven} | {eight}")

    def checkwin(self,xstate,zstate,name2):
        wins = [[0,1,2],[3,4,5],[6,7,8],[1,4,7],[0,3,6],[2,5,8],[0,4,8],[2,4,6]]
        for win in wins:
            if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
                self.speak(f"{name2} won the match")
                return 1
            if sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:
                self.speak(f"Jarvis won the match")
                return 0
        return -1

    def Nasanews(self,date):
        url1 = "https://api.nasa.gov/planetary/apod?api_key="+Api_key
        Params = {'date' : str(date)}
        r = requests.get(url1,params=Params)
        # data = r.json()
        # self.termi(data)
        Data = r.json()
        Info = Data['explanation']
        title = Data['title']
        Image_url = Data['url']
        Image_r = requests.get(Image_url)
        Filename = r"C:\\Users\\bhavy\\OneDrive\\Documents\\Nasa\\{}.jpg".format(date)
        filename = r"C:\\Users\\bhavy\\OneDrive\\Documents\\Nasa\\{}.txt".format(date)
        with open(Filename,'wb') as f:
            f.write(Image_r.content)
        with open(filename,'w') as f:
            f.write(Info)
        os.startfile(Filename)
        os.startfile(filename)
        self.speak("Sir may i speak the news or you will read by yourself...")
        readornot = self.takecommand().lower()
        if readornot == "yes":
            self.speak(f"Title : {title}")
            self.speak(f"According to nasa : {Info}")
        else:
            self.speak("Ok sir working as per you decision")

    def TaskExecution(self):
        play("sounds\\Jarvisstart.mp3")
        sleep(1)
        play("sounds\\Startup Sound.mp3")
        self.wish()
        while True:

            sleep(1)
            self.query = self.takecommand().lower()

            if "open notepad" in self.query:
                self.speak("Ok sir opening Notepad...")
                npath = "apps\\Notepad.lnk"
                os.startfile(npath)
            elif self.query == "none":
                self.termi("Continuing")
            elif "None" in self.query:
                self.speak("date")
            elif "open command prompt" in self.query:
                cpath = "apps\\cmd.lnk"
                self.speak("Ok sir Opening Command prompt...")
                os.startfile(cpath)
            # elif "open camera" in self.query:
            #     self.speak("Ok sir opening Camera...")
            #     cap = cv2.VideoCapture(0)
            #     while True:
            #         ret, img = cap.read()
            #         cv2.imshow('webcam',img)
            #         k = cv2.waitKey(10)
            #         if k==5 :
            #             break
            #     cap.release()
            #     cv2.destroyAllWindows()
            elif "how are you jarvis" in self.query:
                self.speak("I am all date sir. How can i assist you today?")       
            elif"play music" in self.query:
                self.speak("Playing music...")
                music_dir="C:\\Users\\bhavy\Music"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir,song)) 

            elif "up" in self.query:
                move_mouse("up", 100)
                self.speak("Moved...")
            elif "down" in self.query:
                move_mouse("down", 100)
                self.speak("Moved...")
            elif "left" in self.query:
                move_mouse("left", 100)
                self.speak("Moved...")
            elif "right" in self.query:
                move_mouse("right", 100)
                self.speak("Moved...")
            elif "single" and "click" in self.query:
                mouse_position = pyautogui.position()
                pyautogui.click(mouse_position)
                self.speak("Clicked")
            elif "double" and "click" in self.query:
                mouse_position = pyautogui.position()
                pyautogui.click(mouse_position)
                pyautogui.click(mouse_position)
                self.speak("clicked")

            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                self.speak(f"Your ip address is {ip}")
            elif "close tab" in self.query:
                self.speak("closing tab sir...")
                press_and_release("ctrl + w")
            elif "wikipedia" in self.query:
                self.speak("Searching on wikipedia...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                self.speak("According to wikipedia")
                self.speak(results)
                self.termi(results)

            elif "write" and "essay" in self.query:
                que = self.query.replace("write","")
                que = que.replace("a","")
                que = que.replace("an","")
                que = que.replace("on","")
                que = que.replace("the","")
                que = que.replace("topic","")
                que = que.replace("jarvis","")
                que = que.replace("about","")
                # self.speak("By whom you want to renerate response...")
                # self.termi("Bard or Chatgpt?")
                # q1 = self.takecommand().lower()

                # if "chatgpt" in q1:
                #     reply = ai_response(self.query)
                # else:
                reply = bard.get_answer(self.query)['content']

                self.speak("Sir where do you want to wite in ternimal output or notepad")
                ss = self.takecommand().lower()
                if "terminal" in ss:
                    self.termi(f"Topic: {que}")
                    self.termi(reply)
                    self.speak("Written sir...")
                elif "notepad" in ss:
                    self.speak("Sir tell the file name by which you want to save the essay:")
                    namee = self.takecommand().lower()
                    # namee = "C:\\Users\\bhavy\\OneDrive\\note\\"+namee+".txt"
                    namee = namee+".txt"

                    with open("notes\\"+namee,"w") as file:
                        file.write(reply)

                    os.startfile("notes\\"+namee)
                    
                    self.speak(f"A essay on {que} is written...")

            elif "tell me battery" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                self.speak(f"Sir we have {percentage} percent battery") 

            elif("open youtube") in self.query:
                self.speak("Ok sir opening youtube...")
                webbrowser.open("https://www.youtube.com/")

            elif "open telegram" in self.query:
                self.speak("Opening telegram sir...")
                webbrowser.open("https://web.telegram.org/k/")

            elif("open facebook") in self.query:
                self.speak("Ok sir pening facebook...")
                webbrowser.open("https://www.facebook.com/")
    
            # elif("open instagram") in self.query:
            #     self.speak('Ok sir opening instagram...')
            #     webbrowser.open("https://www.instagram.com/")

            elif("open github") in self.query:
                self.speak("Ok sir opening github...")
                webbrowser.open("https://github.com/")

            elif("open google") in self.query:
                self.speak("Sir, what should i search on google")
                cm = self.takecommand().lower()
                self.speak("Searching in process...")
                sleep(1)
                self.speak("Opening google...")
                webbrowser.open(f"{cm}")

            elif "open whatsapp" in self.query:
                os.startfile("apps\\WhatsApp.lnk")
                self.speak("Opening whatsapp sir...")

            elif "send message" in self.query:
                self.speak("Tell the whatsapp name to whom you have to send message:")
                name = self.takecommand().lower()
                self.speak("Speak out the message you what to send:")
                msgwhat = self.takecommand().lower()
                whatsappmsg(name,msgwhat)

            elif "open instagram" in self.query:
                self.speak("Opening instagram sir...")
                os.startfile("apps\\Instagram.lnk")
            
            elif "open calculator" in self.query:
                self.speak("Opening calculator sir...")
                os.startfile("apps\\Calculator.lnk")

            elif "call" and "on whatsapp" in self.query:
                self.speak("How you want to call Voice or video:")
                hint = self.takecommand().lower()
                while True:
                    if "voice" in hint:
                        self.speak("Whom you have to call:")
                        someone = self.takecommand().lower()
                        whatscall(someone)
                        break
                    elif "video" in hint:
                        self.speak("Whom you have to call:")
                        some = self.takecommand().lower()
                        whatsvcall(some)
                        break
                    else :
                        self.speak("Invalid command do you want to try again yes or no:")
                        take_command = self.takecommand().lower()
                        if "yes" in take_command:
                            pass
                        elif "no" in take_command:
                            break
            elif "on youtube" in self.query:
                self.speak("Name the video or song you want to play on youtube:")
                song = self.takecommand().lower()
                kit.playonyt(song)

            elif "need" and "blood" in self.query:
                self.speak("Fill the information here and click search:")
                webbrowser.open("https://www.friends2support.org/")
            elif "email" and "send" in self.query:
                try:
                    self.speak("Tell the email address at which you want to send mail")
                    to = self.takecommand().lower()
                    to2 = to.replace(" ","")
                    self.termi(f"Target:{to2}")
                    self.speak("Tell me the subject of the email:")
                    sub = self.takecommand().lower()
                    self.speak("What should i say?")
                    content = self.takecommand().lower()
                    webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
                    sleep(5)
                    click(x=103, y=183)
                    sleep(4)
                    click(x=890, y=307)
                    sleep(1)
                    write(to2)
                    press("enter")
                    sleep(2)
                    click(x=871, y=408)
                    sleep(2)
                    click(x=895, y=344)
                    sleep(2)
                    write(sub)
                    sleep(2)
                    click(x=871, y=408)
                    click(x=871, y=408)
                    sleep(2)
                    write(content)
                    sleep(2)
                    click(x=841, y=699)
                    self.speak(f"Your Email has been sent...")
                except Exception as e:
                    self.termi(e)
                    self.speak("Sorry sir i am not able to send mail...")
            elif "sleep for now" in self.query:
                self.speak("Thanks sir for using me \n Exiting program...")
                sleep(2)
                self.speak("Exited successfully...")
                play("sounds\\jarvishutdown.mp3")
                # pyautogui.click(x=580, y=481)
                sys.exit()
                break
            elif "close notepad" in self.query:
                self.speak('Ok sir closing notepad...')
                os.system("taskkill /f /im Notepad.exe")
            # elif "close camera" in self.query:
            #     self.speak('Ok sir closing Camera...')
            #     cv2.destroyAllWindows()

            elif "start calculating" in self.query:
                while True:
                    self.speak("Sir tell me the first number:")
                    num1 = str(self.takecommand())
                    num1 = num1.lower()
                    num1 = num1.replace("one","1")
                    num1 = num1.replace("two","2")
                    num1 = num1.replace("three","3")
                    num1 = num1.replace("four","4")
                    num1 = num1.replace("five","5")
                    num1 = num1.replace("six","6")
                    num1 = num1.replace("seven","7")
                    num1 = num1.replace("eight","8")
                    num1 = num1.replace("nine","9")
                    num1 = num1.replace("zero","0")
                    num1 = num1.replace(" ","")
                    num1 = int(num1)
                    self.speak("Sir tell me the second number:")
                    num2 = str(self.takecommand())
                    num2 = num2.lower()
                    num2 = num2.replace("one","1")
                    num2 = num2.replace("two","2")
                    num2 = num2.replace("three","3")
                    num2 = num2.replace("four","4")
                    num2 = num2.replace("five","5")
                    num2 = num2.replace("six","6")
                    num2 = num2.replace("seven","7")
                    num2 = num2.replace("eight","8")
                    num2 = num2.replace("nine","9")
                    num2 = num2.replace("zero","0")
                    num2 = num2.replace(" ","")
                    num2 = int(num2)
                    self.speak("Sir tell me the operation")
                    opp = self.takecommand().lower()
                    ans = 0
                    if opp == "add":
                        ans = num1+num2
                        self.speak(f"Your ans is {str(ans)}")
                    elif opp == "substract":
                        ans = num1-num2
                        self.speak(f"Your ans is {str(ans)}")
                    elif opp == "multiply":
                        ans = num1*num2
                        self.speak(f"Your ans is {str(ans)}")
                    elif opp == "divide":
                        ans = num1/num2 
                        self.speak(f"Your ans is {str(ans)}")

                    self.speak("sir do you want to continue:")
                    yesorno = self.takecommand().lower()
                    if yesorno == "yes":
                        self.speak("Continuing sir...")
                    else:
                        self.speak("Ready for your next command sir")
                        break

            elif "close command prompt" in self.query:
                self.speak('Ok sir closing Command prompt...')
                os.system("taskkill /f /im cmd.exe")
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                self.speak(joke)
            elif "shut down the system" in self.query:
                self.speak("Ok sir shuting down...")
                os.system("shutdown /s /t")
            elif "restart the system" in self.query :
                self.speak("Ok sir restarting the system...")
                os.system("shutdown /r /t 5")

            elif "take photo" in self.query:
                os.startfile("apps\\Camera.lnk")
                sleep(2)
                self.speak("3")
                self.speak("2")
                self.speak("1")
                self.speak("Say cheesee")
                pyautogui.click(x=1319, y=392)
            
            elif "sleep the system" in self.query:
                self.speak("Going to sleep...")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            # elif "set alarm" in self.query:
            #     nn = int(datetime.datetime.now().hour)
            #     if nn == 22:
            #         music_dir = "C:\\Users\\bhavy\Music"
            #     songs = os.listdir("C:\\Users\\bhavy\Music")
            #     for song in songs:
            #         os.startfile(os.path.join("C:\\Users\\bhavy\Music",song))
            elif "switch the window" in self.query:
                pyautogui.keydown("alt")
                pyautogui.press("tab")
                sleep(1)
                pyautogui.keyup("alt")

            elif "tell" and "nasa" in self.query:
                self.speak("Sir tell me the date in year month and day format")
                date = self.takecommand().lower()
                date = date.replace("january","1")
                date = date.replace("february","2")
                date = date.replace("march","3")
                date = date.replace("april","4")
                date = date.replace("may","5")
                date = date.replace("june","6")
                date = date.replace("july","7")
                date = date.replace("august","8")
                date = date.replace("september","9")
                date = date.replace("october","10")
                date = date.replace("november","11")
                date = date.replace("december","12")
                date = date.replace(" ","-")
                # date = self.ui.terminalOutput.toPlainText()
                # date = dateee()
                # date = input("Enter date here:")
                # day = datetime.datetime.now().day
                # mon = datetime.datetime.now().month
                # yea = datetime.datetime.now().year
                # date = str(yea)+'-'+str(mon)+'-'+str(day)
                # url1 = "https://api.nasa.gov/planetary/apod?api_key="+Api_key
                # Params = {'date' : str(date)}
                # r = requests.get(url1,params=Params)
                # # data = r.json()
                # # self.termi(data)
                # Data = r.json()
                # Info = Data['explanation']
                # title = Data['title']
                # Image_url = Data['url']
                # Image_r = requests.get(Image_url)
                # Filename = r"C:\\Users\\bhavy\\OneDrive\\Documents\\Nasa\\{}.jpg".format(date)
                # filename = r"C:\\Users\\bhavy\\OneDrive\\Documents\\Nasa\\{}.txt".format(date)
                # with open(Filename,'wb') as f:
                #     f.write(Image_r.content)
                # with open(filename,'w') as f:
                #     f.write(Info)
                # os.startfile(Filename)
                # os.startfile(filename)
                # self.speak("Sir may i speak the news or you will read by yourself...")
                # readornot = self.takecommand().lower()
                # if readornot == "yes":
                #     self.speak(f"Title : {title}")
                #     self.speak(f"According to nasa : {Info}")
                # else:
                #     self.speak("Ok sir working as per you decision")
                self.Nasanews(date)

            elif "close gallery" in self.query:
                self.speak("Closing gallery sir")
                press_and_release("Alt + F4")

            elif "tell " and "daily news" in self.query:
                self.speak("Wait sir, Fetching the best recent news...")
                self.news()
            elif  "location" in self.query:
                self.speak("Wait sir, let me check...")
                try:
                    ipadd= requests.get("https://api.ipify.org").text
                    self.termi(ipadd)
                    url= "https://get.geojs.io/v1/ip/geo/"+ipadd+".json"
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    self.speak(f"Sir we are in city named {city} in the country {country}")
                except Exception as e:
                    self.speak("Sorry sir, due to network issue i am not able to find where we are.")
            elif "screenshot" in self.query:
                self.speak("Tell me the name for the screenshot file")
                sname= self.takecommand().lower()
                self.speak("Taking screenshot...")
                sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{sname}.png")
                self.speak("I am done sir, I have take the screenshot and i am ready for the next command")
            elif "control youtube" in self.query:
                self.youtubeauto()
            elif "hide all files" in self.query or "visible all files" in self.query:
                self.speak("Sir plz tell me do you want to hide files or visible for everyone")
                condi = self.takecommand().lower()
                if "hide" in condi:
                    os.system("attrib +h /s /d")
                    self.speak("sir, all files in the folder are hidden")
                elif "visible" in condi:
                    os.system("attrib -h /s /d")
                    self.speak('All the files of this folder are visbile now')
            elif "internet speed" in self.query:
                self.speak("Starting test sir...")
                dl = speedtest.Speedtest().download()
                ul = speedtest.Speedtest().upload()
                self.speak(f"Sir our downloading speed is {dl} and uploading speed is {ul}")

            elif"set" and "alarm" in self.query:
                self.speak("Sir tell me the hour:")
                hourrr = str(self.takecommand())
                hourrr = hourrr.lower()
                hourrr = hourrr.replace("one","1")
                hourrr = hourrr.replace("two","2")
                hourrr = hourrr.replace("three","3")
                hourrr = hourrr.replace("four","4")
                hourrr = hourrr.replace("five","5")
                hourrr = hourrr.replace("six","6")
                hourrr = hourrr.replace("seven","7")
                hourrr = hourrr.replace("eight","8")
                hourrr = hourrr.replace("nine","9")
                hourrr = hourrr.replace("zero","0")
                hourrr = hourrr.replace(" ","")
                hourrr = int(hourrr)

                self.speak("Sir tell me the minute:")
                minu = str(self.takecommand())
                minu = minu.lower()
                minu = minu.replace("one","1")
                minu = minu.replace("two","2")
                minu = minu.replace("three","3")
                minu = minu.replace("four","4")
                minu = minu.replace("five","5")
                minu = minu.replace("six","6")
                minu = minu.replace("seven","7")
                minu = minu.replace("eight","8")
                minu = minu.replace("nine","9")
                minu = minu.replace("zero","0")
                minu = minu.replace(" ","")
                minu = int(minu)

                self.speak("Starting process")

                # hourr = datetime.datetime.now().hour
                # minut = datetime.datetime.now().minute

                if hourrr >= 7:
                    hourrrr = int(hourrr) - 7
                    minutee = int(minu) - 0

                    os.startfile("apps\\Clock.lnk")
                    # pyautogui.click(x=851, y=749)

                    sleep(2)

                    pyautogui.click(x=105, y=126)

                    sleep(2)

                    pyautogui.click(x=1320, y=684)
                    
                    sleep(2)

                    i = 0
                    while i < hourrrr:
                        pyautogui.click(x=625, y=165)
                        i=i+1
                        sleep(0.5)
                    j=0
                    while j < minutee:
                        pyautogui.click(x=744, y=156)
                        j=j+1
                        sleep(0.5)

                    sleep(2)

                    pyautogui.click(x=644, y=619)

                else :
                    
                    hourrrr = 7 - int(hourrr)
                    minutee = int(minu)

                    os.startfile("apps\\Clock.lnk")
                    # pyautogui.click(x=851, y=749)

                    sleep(2)

                    pyautogui.click(x=105, y=126)

                    sleep(2)

                    pyautogui.click(x=1320, y=684)

                    sleep(2)

                    i = 0
                    while i < hourrrr:
                        pyautogui.click(x=619, y=279)
                        i=i+1
                        sleep(0.5)
                    j=0
                    while j < minutee:
                        pyautogui.click(x=744, y=156)
                        j=j+1
                        sleep(0.5)

                    sleep(2)

                    pyautogui.click(x=644, y=619)
                
                self.speak("The is all set...")

            elif "tell" and "temperature" in self.query:
                self.speak("Sir tell me the name of the city to find temperature:")
                city = self.takecommand().lower()
                try:
                    url2 = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key2}"
                    r = requests.get(url2)
                    data3 = r.json()
                    temp = data3['main']['temp']
                    temp2 = int(temp) - 273
                    temp2 = str(temp2)
                    self.speak(f"Current temperature in {city} is {temp2} degrees celcius")
                except Exception as e :
                    self.speak("There was a error may be the name of the city is not correct")

            elif "close telegram" in self.query:
                self.speak("Closing telegram sir...")
                press_and_release("ctrl+w")

            elif "close youtube" in self.query:
                self.speak("Closing youtube sir...")
                press_and_release("ctrl+w")

            elif "close instagram" in self.query:
                self.speak("Closing instagram sir...")
                os.system("taskkill /f /im Instagram.exe")

            elif "close whatsapp" in self.query:
                self.speak("Closing whatsapp sir...")
                os.system("taskkill /f /im Whatsapp.exe")

            elif "close calculator" in self.query:
                self.speak("Closing calculator sir...")
                os.system("taskkill /f /im Calculator.exe")

            elif "close clock" in self.query:
                self.speak("Closing clock sir...")
                os.system("taskkill /f /im Clock.exe")

            elif "open clock" in self.query:
                self.speak("Opening Clock sir")
                os.startfile("apps\\Clock.lnk")

            elif "open camera" in self.query:
                self.speak("Opening Camera sir...")
                os.startfile("apps\\Camera.lnk")
            
            elif "open gallery" in self.query:
                self.speak("Opening Gallery sir...")
                os.startfile("apps\\Photos.lnk")

            elif "open videos" in self.query:
                self.speak("Opening Videos sir...")
                os.startfile("apps\\Films_&_Tv.lnk")

            elif "open vs code" in self.query:
                self.speak("Opening VS code sir...")
                os.startfile("apps\\Visual_Studio_Code.lnk")

            elif "open screen recorder" in self.query:
                self.speak("Opening  screen recorder sir...")
                os.startfile("apps\\Fine_Screen_Recoder.lnk")

            elif "close camera" in self.query:
                self.speak("Closing camera sir...")
                os.system("taskkill /im WindowsCamera.exe /t /f")

            elif "close videos" in self.query:
                self.speak("Closing videos sir...")
                os.system("taskkill /f /im Films_&_Tv.exe")

            elif "close vs code" in self.query:
                self.speak("Closing VS code sir...")
                os.system("taskkill /f /im Code.exe")

            # elif "close gallery" in self.query:
            #     self.speak("Closing gallery sir...")
            #     # os.system("taskkill /im Photos.exe /t /f")
            #     pyautogui.click(x=1343, y=17)


            elif "close screen recorder" in self.query:
                self.speak("Closing Screen Recorder sir...")
                os.system("taskkill /f /im Fine_Screen_Recorder.exe")

            elif "open new tab" in self.query:
                self.speak("Opening new tab sir...")
                os.startfile("apps\\Google Chrome.lnk")

            elif "dismiss alarm" in self.query:
                pyautogui.click(x=1126, y=692)
                self.speak("Alarm dismissed sir...")

            elif "snooze alarm" in self.query:
                pyautogui.click(x=1226, y=683)
                self.speak("Alarm snoozed for 5 minutes")

            # elif "take photo" in self.query:
            #     os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\Camera.lnk")

            elif "volume up" in self.query:
                pyautogui.press("volumeup")
            elif "volume down" in self.query:
                pyautogui.press("volumedown")
            elif "mute" in self.query:
                pyautogui.press("volumemute")
            elif "unmute" in self.query:
                pyautogui.press("volumemute")

            elif "take video" in self.query:
                self.speak("Sir tell me for how many seconds")
                # ttimme = self.takecommand().lower()
                ttiimmee = str(self.takecommand())
                ttiimmee = ttiimmee.lower()
                ttiimmee = ttiimmee.replace("one","1")
                ttiimmee = ttiimmee.replace("two","2")
                ttiimmee = ttiimmee.replace("three","3")
                ttiimmee = ttiimmee.replace("four","4")
                ttiimmee = ttiimmee.replace("five","5")
                ttiimmee = ttiimmee.replace("six","6")
                ttiimmee = ttiimmee.replace("seven","7")
                ttiimmee = ttiimmee.replace("eight","8")
                ttiimmee = ttiimmee.replace("nine","9")
                ttiimmee = ttiimmee.replace("zero","0")
                ttiimmee = ttiimmee.replace(" ","")
                ttiimmee = int(ttiimmee)

                os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\Camera.lnk")

                sleep(2)

                pyautogui.click(x=1315, y=172)

                sleep(1)

                pyautogui.click(x=1319, y=392)

                sleep(ttiimmee)

                pyautogui.click(x=1319, y=392)
                
                self.speak("The video is recorded sir....")

            elif "open chatbot" in self.query:
                os.startfile("jarvischat.py")
                self.speak("The chatbot is opened sir going to sleep for some time")
                play("C:\\Users\\bhavy\\Downloads\\jarvishutdown.mp3")
                sys.exit()

            elif "play" and "a game" in self.query:
                self.speak("Which game to play sir...")
                self.speak("1. rock paper scissors")
                self.speak("2. X and O")
                self.speak("3. Flappy Birds")
                self.speak("4. Egg catcher")
                self.speak("5. guess the number")
                self.speak("6. hangman")
                # whattopaly = str(self.takecommand().lower())
                # whattopaly = whattopaly.replace("first","1")
                # whattopaly = whattopaly.replace("one","")
                # whattopaly = whattopaly.replace("1","")
                # whattopaly = whattopaly.replace("game","")
                # whattopaly = whattopaly.replace("second","2")
                # whattopaly = whattopaly.replace("third","3")
                # whattopaly = whattopaly.replace("fourth","4")
                # whattopaly = whattopaly.replace("one","1")
                # whattopaly = whattopaly.replace("two","2")
                # whattopaly = whattopaly.replace("three","3")
                # whattopaly = whattopaly.replace("four","4")

                # if "1" or "first" in whattopaly:
                #     while True:
                #         self.speak("sir tell me the name of the player:")
                #         name = self.takecommand()
                #         self.speak("what do you want to choose:")
                #         self.speak("Rock papers or scissors")

                #         playerTurn = self.takecommand().lower()

                #         if "rock" in playerTurn:
                #             playerTurn = 'r'
                #         elif "paper" in playerTurn:
                #             playerTurn = 'p' 
                #         elif "scissors" or "scissor" in playerTurn:
                #             playerTurn = 's'                           

                #         self.speak("Let me choose...")
                        
                #         sleep(2)

                #         self.speak("Ok sir choosed")

                #         randomint = random.randint(1,3)

                #         if randomint == 1:
                #             computerturn = 'r'
                #         elif randomint == 2:
                #             computerturn = 'p'
                #         else:
                #             computerturn = 's'

                #         result = game(computerturn,playerTurn)

                #         self.speak("Ok sir showing in...")
                #         self.speak("3")
                #         self.speak("2")
                #         self.speak("1")

                #         if computerturn == 's':
                #             self.speak("Jarvis choosses Scissor")
                #         elif computerturn == 'p':
                #             self.speak("Jarvis chosses paper")
                #         elif computerturn == 'r':
                #             self.speak("Jarvis chosses rock")

                #         if playerTurn == 's':
                #             self.speak(f"{name} choosses Scissor")
                #         elif playerTurn == 'p':
                #             self.speak(f"{name} chosses paper")
                #         elif playerTurn == 'r':
                #             self.speak(f"{name} chosses rock")

                #         if result == None:
                #             self.speak("No one wins! it is Tie!")
                #         elif result == True:
                #             self.speak(f"Computer losses! {name} Won!")
                #         elif result == False:
                #             self.speak(f"{name} Losses! Computer Won!")


                #         self.speak("sir do you wnat to continue then say continue and if you don't want to speak quit")

                #         conplay = self.takecommand().lower()

                #         if "quit" in conplay:
                #             self.speak("Ok sir ready for your next command")
                #             break
                #         elif "continue" in conplay:
                #             continue
                #         else:
                #             self.speak("Ok sir ready for your next command")
                #             break
                # elif "2" or "second" in whattopaly:
                #     # self.speak('Tic Tac Toe is on')
                #     # xstate=[0, 0, 0, 0, 0, 0, 0, 0, 0]
                #     # zstate=[0, 0, 0, 0, 0, 0, 0, 0, 0]
                #     # self.speak("Tell me the name of the palyer")
                #     # name2 = self.takecommand()
                #     # turn = 1
                #     # mainnumbers = [0,1,2,3,4,5,6,7,8]
                #     # while True:
                #     #     self.printboard(xstate,zstate)
                #     #     if turn == 1:
                #     #         self.speak(f"{name2}'s chance")
                #     #         value = str(self.takecommand().lower())
                #     #         value = value.replace("zero","0")
                #     #         value = value.replace("one","1")
                #     #         value = value.replace("two","2")
                #     #         value = value.replace("three","3")
                #     #         value = value.replace("four","4")
                #     #         value = value.replace("five","5")
                #     #         value = value.replace("six","6")
                #     #         value = value.replace("seven","7")
                #     #         value = value.replace("eight","8")
                #     #         value = int(value)
                #     #         xstate[value] = 1
                #     #         mainnumbers.remove(value)
                #     #     else :
                #     #         self.speak("Let me choose")
                #     #         Oturn = random.choices(mainnumbers)
                #     #         zstate[value] = Oturn
                #     #         mainnumbers.remove(Oturn)
                #     #     cwin = self.checkwin(xstate,zstate,name2)
                #     #     if cwin != -1:
                #     #         self.speak("Match draw")
                #     #         break
                #     # turn = 1 - turn
                #     self.speak("At chrome or at window")
                #     howtoplay = self.takecommand().lower()
                #     if "chrome" in howtoplay:
                #         self.speak("Opening in chrome sir...")
                #         webbrowser.open("https://bhavyaop2.000webhostapp.com/")
                #     if "window" in howtoplay:
                #         os.startfile("C:\\Users\\bhavy\\OneDrive\\Documents\\omg\\tictactoe py\\Tic_Tac_Toe_Game.py") 

                # elif "3" or "third" in whattopaly:
                #     self.speak("Starting Flappy Birds...")
                #     os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\Python programs\\Projects by Bhavya\\flappybirds.py")
                #     # self.speak("Sleeping foe 20 seconds")
                #     # sleep(2)
                # elif "4" or "fourth" in whattopaly:
                #     self.speak("Starting Egg Catcher...")
                #     os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\Python programs\\Projects by Bhavya\\egg_catcher.py")
                # elif whattopaly == "none":
                #     continue

            elif "play" and "first game" in self.query:
                while True:
                    self.speak("sir tell me the name of the player:")
                    name = self.takecommand()
                    self.speak("what do you want to choose:")
                    self.speak("Rock papers or scissors")

                    playerTurn = self.takecommand().lower()

                    if "rock" in playerTurn:
                        playerTurn = 'r'
                    elif "paper" in playerTurn:
                        playerTurn = 'p' 
                    elif "scissors" or "scissor" in playerTurn:
                        playerTurn = 's'                           

                    self.speak("Let me choose...")
                    
                    sleep(2)

                    self.speak("Ok sir choosed")

                    randomint = random.randint(1,3)

                    if randomint == 1:
                        computerturn = 'r'
                    elif randomint == 2:
                        computerturn = 'p'
                    else:
                        computerturn = 's'

                    result = game(computerturn,playerTurn)

                    self.speak("Ok sir showing in...")
                    self.speak("3")
                    self.speak("2")
                    self.speak("1")

                    if computerturn == 's':
                        self.speak("Jarvis choosses Scissor")
                    elif computerturn == 'p':
                        self.speak("Jarvis chosses paper")
                    elif computerturn == 'r':
                        self.speak("Jarvis chosses rock")

                    if playerTurn == 's':
                        self.speak(f"{name} choosses Scissor")
                    elif playerTurn == 'p':
                        self.speak(f"{name} chosses paper")
                    elif playerTurn == 'r':
                        self.speak(f"{name} chosses rock")

                    if result == None:
                        self.speak("No one wins! it is Tie!")
                    elif result == True:
                        self.speak(f"Computer losses! {name} Won!")
                    elif result == False:
                        self.speak(f"{name} Losses! Computer Won!")


                    self.speak("sir do you wnat to continue then say continue and if you don't want to speak quit")

                    conplay = self.takecommand().lower()

                    if "quit" in conplay:
                        self.speak("Ok sir ready for your next command")
                        break
                    elif "continue" in conplay:
                        continue
                    else:
                        self.speak("Ok sir ready for your next command")
                        break
            
            elif "play" and "rock papper scissor" in self.query:
                while True:
                    self.speak("sir tell me the name of the player:")
                    name = self.takecommand()
                    self.speak("what do you want to choose:")
                    self.speak("Rock papers or scissors")

                    playerTurn = self.takecommand().lower()

                    if "rock" in playerTurn:
                        playerTurn = 'r'
                    elif "paper" in playerTurn:
                        playerTurn = 'p' 
                    elif "scissors" or "scissor" in playerTurn:
                        playerTurn = 's'                           

                    self.speak("Let me choose...")
                    
                    sleep(2)

                    self.speak("Ok sir choosed")

                    randomint = random.randint(1,3)

                    if randomint == 1:
                        computerturn = 'r'
                    elif randomint == 2:
                        computerturn = 'p'
                    else:
                        computerturn = 's'

                    result = game(computerturn,playerTurn)

                    self.speak("Ok sir showing in...")
                    self.speak("3")
                    self.speak("2")
                    self.speak("1")

                    if computerturn == 's':
                        self.speak("Jarvis choosses Scissor")
                    elif computerturn == 'p':
                        self.speak("Jarvis chosses paper")
                    elif computerturn == 'r':
                        self.speak("Jarvis chosses rock")

                    if playerTurn == 's':
                        self.speak(f"{name} choosses Scissor")
                    elif playerTurn == 'p':
                        self.speak(f"{name} chosses paper")
                    elif playerTurn == 'r':
                        self.speak(f"{name} chosses rock")

                    if result == None:
                        self.speak("No one wins! it is Tie!")
                    elif result == True:
                        self.speak(f"Computer losses! {name} Won!")
                    elif result == False:
                        self.speak(f"{name} Losses! Computer Won!")


                    self.speak("sir do you wnat to continue then say continue and if you don't want to speak quit")

                    conplay = self.takecommand().lower()

                    if "quit" in conplay:
                        self.speak("Ok sir ready for your next command")
                        break
                    elif "continue" in conplay:
                        continue
                    else:
                        self.speak("Ok sir ready for your next command")
                        break

            elif "play" and "x and o" in self.query:
                # self.speak('Tic Tac Toe is on')
                # xstate=[0, 0, 0, 0, 0, 0, 0, 0, 0]
                # zstate=[0, 0, 0, 0, 0, 0, 0, 0, 0]
                # self.speak("Tell me the name of the palyer")
                # name2 = self.takecommand()
                # turn = 1
                # mainnumbers = [0,1,2,3,4,5,6,7,8]
                # while True:
                #     self.printboard(xstate,zstate)
                #     if turn == 1:
                #         self.speak(f"{name2}'s chance")
                #         value = str(self.takecommand().lower())
                #         value = value.replace("zero","0")
                #         value = value.replace("one","1")
                #         value = value.replace("two","2")
                #         value = value.replace("three","3")
                #         value = value.replace("four","4")
                #         value = value.replace("five","5")
                #         value = value.replace("six","6")
                #         value = value.replace("seven","7")
                #         value = value.replace("eight","8")
                #         value = int(value)
                #         xstate[value] = 1
                #         mainnumbers.remove(value)
                #     else :
                #         self.speak("Let me choose")
                #         Oturn = random.choices(mainnumbers)
                #         zstate[value] = Oturn
                #         mainnumbers.remove(Oturn)
                #     cwin = self.checkwin(xstate,zstate,name2)
                #     if cwin != -1:
                #         self.speak("Match draw")
                #         break
                # turn = 1 - turn
                self.speak("At chrome or at window")
                howtoplay = self.takecommand().lower()
                if "chrome" in howtoplay:
                    self.speak("Opening in chrome sir...")
                    webbrowser.open("https://bhavyaop2.000webhostapp.com/")
                if "window" in howtoplay:
                    os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\project 2.o\\tictactoe py\\Tic_Tac_Toe_Game.py") 

            elif "play" and "flappy birds" in self.query:
                self.speak("Starting Flappy Birds...")
                os.startfile("games\\flappybirds.py")
                sleep(1)
                # self.speak("Sleeping foe 20 seconds")
                # sleep(2)
            elif "play" and "egg catcher" in self.query:
                self.speak("Starting Egg Catcher...")
                os.startfile("games\\egg_catcher.py")
                sleep(1)

            elif "close flappy birds" in self.query:
                self.speak("Ok sir closing flappy birds")
                pyautogui.click(x=452, y=365)
                sleep(2)
                press_and_release("ctrl + c")

            elif "close egg catcher" in self.query:
                self.speak("Ok sir closing Egg catcher")
                pyautogui.click(x=452, y=365)
                sleep(2)
                press_and_release("ctrl + c")

            elif "what can you do" in self.query:
                self.speak("I can the do the following tasks:-")
                self.speak("Operated by voice\ncan provide information about different people near by you who donate different blood groups\nOpen close apps\ncontrol arrow\nplay games\nplay songs\nplay videos on youtube\ncheck your internet speed\n tell your battery percent\nans any of your question\nalso available in chat form\ncan write very long essays\nset alarm\ndismiss or snoose alarm\netc etc........ ")
                self.speak("These are the normal function")
                self.speak("I am too advance as you think")

            elif "open my site" in self.query:
                webbrowser.open("https://bhavyagreat.000webhostapp.com/")

            elif "open gseb solutions" in self.query:
                webbrowser.open("https://gsebsolutions.com/")

            elif "open ncert solution" in self.query:
                webbrowser.open("https://www.learncbse.in/")

            elif "who created you" in self.query:
                self.speak('Bhavya Dhanwani is the one only one who created me')

            elif "start" and "youtube downloader" in self.query:
                self.speak("Sir youtube video downloader is opened..")
                os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\project 2.o\\others\\youtbedownloader.py")

            elif "play" and "last game" in self.query:
                os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\project 2.o\\games\\hangman.py")
                self.speak("The game is opened...")

            elif "play" and "hangman" in self.query:
                os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\project 2.o\\games\\hangman.py")
                self.speak("The game is opened...")

            elif "play" and "guess the number" in self.query:
                os.startfile("C:\\Users\\bhavy\\OneDrive\\Desktop\\project 2.o\\games\\guessthenum.py")
                self.speak("The game is opened...")

            elif "take a break" in self.query:
                self.speak("Sir for how many seconds...")
                howmuchtime = str(self.takecommand())
                howmuchtime = howmuchtime.lower()
                howmuchtime = howmuchtime.replace("one","1")
                howmuchtime = howmuchtime.replace("two","2")
                howmuchtime = howmuchtime.replace("three","3")
                howmuchtime = howmuchtime.replace("four","4")
                howmuchtime = howmuchtime.replace("five","5")
                howmuchtime = howmuchtime.replace("six","6")
                howmuchtime = howmuchtime.replace("seven","7")
                howmuchtime = howmuchtime.replace("eight","8")
                howmuchtime = howmuchtime.replace("nine","9")
                howmuchtime = howmuchtime.replace("zero","0")
                howmuchtime = howmuchtime.replace(" ","")
                howmuchtime = int(howmuchtime)

                self.speak("ok sir going for a break...")

                sleep(howmuchtime)

                self.speak("I am back sir...")

            elif "say hello to" in self.query:
                nameeee = self.query
                nameeee = nameeee.replace("say","")
                nameeee = nameeee.replace("hello","")
                nameeee = nameeee.replace("to","")
                
                self.speak(f"Hello {nameeee} how are you")

            elif "start" and "writing" in self.query:
                self.speak("Ok sir writing...")
                while True:
                    whattowrite = self.takecommand()
                    if "quit" in whattowrite:
                        self.speak("ready for your next cmmand sir...")
                        break
                    elif "new line" in whattowrite:
                        press('enter')
                    else :
                        write(f"{whattowrite} ")
            
            elif "open text to image" in self.query:
                self.speak("Opening the site sir...")
                webbrowser.open("https://lexica.art/aperture")

            elif "text to image" in self.query:
                self.speak('Sir tell mee what tou want to create')
                prompttoimg = self.takecommand().lower()
                output = textimage(prompttoimg)
                if output == True:
                    self.speak("The image is generated sir...")

            else:
                reply = ai_response(self.query)
                self.speak(reply)

# sleep(2)
# os.startfile("videos\\JARVISintro.mp4")
# sleep(27)

# # click(x=1334, y=20)
# pyautogui.click(x=1334,y=20)
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
pyautogui.click(x=459, y=474)
exit(app.exec_())
sys.exit()