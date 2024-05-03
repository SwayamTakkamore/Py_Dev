from email import message
from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import hashlib
import speedtest
import requests
import numpy as np
from sys import byteorder
from array import array
from struct import pack
from bs4 import BeautifulSoup
from genericpath import isdir
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(self):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am jarvis, Please tell me how may I help you")
    print("I am jarvis, Please tell me how may I help you")
    speakflag = 1

def wishMe2():
    speak("Please tell me how may I help you")
    print("Please tell me how may I help you")

def takeCommand():

    # It take Microphone Access From User and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 450
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception:
        speak("Sorry, I am unable to understand")
        print("Say that again please...")
        return "None"
    
    return query

def mail(to, content):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    sender_email = 'sample123@gmail.com'
    password = "Sample@123"
    speak(" whom do you want to send mail to ?")
    receiver_mail_id = takeCommand()
    mail_id_list = {"sample 2" : "sample2@gmail.com","sample 3" : "sample3@gmail.com"}
    to = mail_id_list[receiver_mail_id]
    
    s.starttls()
    s.login(sender_email, password)
    speak("what message should i send?")
    content = takeCommand()

    s.sendmail(to, content)
    speak("sending mail...")
    s.quit()
    speak("mail sent successfully!")


def sendEmail(to, content):
    myMail = 'sample123@gmail.com'
    pword = 'Sample@123'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(myMail, pword)
    server.sendmail(myMail, to, content)
    server.close()

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def test_run():
    d, u, p = test()
    print('Download: {:.2f} Mb/s\n'.format(d / 1024 / 1024))
    speak('download speed is, {:.2f} M B P S\n'.format(d / 1024 / 1024))
    print('Upload: {:.2f} Mb/s\n'.format(u / 1024 / 1024))
    speak('Upload speed is, {:.2f} M B P S\n'.format(u / 1024 / 1024))
    print('Ping: {} ms\n'.format(p))
    speak('Ping is{} ms\n'.format(p))

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city):
	city = city.replace(" ", "+")
	res = requests.get(
		f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	print("Searching...\n")
	soup = BeautifulSoup(res.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
	print(location)
	print(info)
	print(weather+"°C")

def main(self):
        if speakflag == 0:
            wishMe(self)
        else:
            wishMe2()
        query = takeCommand().lower()
        return 1

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'thank you' in query:
            speak("welcome")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is {strTime}")

        elif 'open vs code' in query:
            os.system("code")

        elif 'open python' in query:
            os.system("python")
        
        elif 'send mail' in query:
            try:
                speak("to whom should I mail?")
                codeLst = takeCommand()
                Cs1 = {"sample 2" : "sample2@gmail.com","sample 3" : "sample3@gmail.com"}
                cslist = Cs1[codeLst]
                speak("what should I say?")
                content = takeCommand()
                to = cslist
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry , I am unable to send this mail")

        elif 'hello' in query:                                              # It reply on hello
            speak("hello!, I'm jarvis")

        elif 'good night' in query:                                         # It reply on Good Night
            speak("Very Good Night, Bye bye")
            exit()

        elif 'quit' in query:                                               # To Exit
            speak("quitting !")
            exit()

        elif 'exit' in query:                                               # To Exit
            speak("exitting!")
            exit()

        elif 'bye' in query:                                                # To Exit
            speak('bye!')
            exit()

        elif 'how are you' in query:
            speak("I am Fine, Hope you're also Fine")

        elif 'where do you live?' in query:
            speak("i live in your PC")   

        elif 'test the internet speed' in query:
            try:
                speak("Sure! please wait for a second")
                print("Testing...")
                test_run()
            except:
                speak("Sorry! I'm unable to test it")

        elif 'test internet speed' in query:
            try:
                speak("Sure! please wait for a second")
                print("Testing...")
                test_run()
            except:
                speak("Sorry! I'm unable to test it")

        elif 'check weather' in query:
            speak("please tell the Name of the City")
            city = takeCommand()
            city = city+" weather"
            weather(city)
            print("Have a Nice Day:)")

if __name__ == "__main__":
    # wishMe()
    speakflag = 0
    #if 1:                             #It is to take only one command.
    while True:                         #It is to take commands infinite times.
        speakflag = main(speakflag)