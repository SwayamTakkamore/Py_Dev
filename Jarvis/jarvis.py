import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pafy
import urllib.request
import re
import inquirer
import os
import sys
import random
import smtplib
import hashlib
import vlc
import speedtest
from genericpath import isdir
from time import sleep
from rich.progress import track, Progress
from youtubesearchpython import PlaylistsSearch


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

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

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, Please tell me how may I help you")

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
        # print(e)
        print("Say that again please...")
        return "None"
    return query


os.chdir('C:\\')
if(not os.path.isdir('Jarvis_files')):
        os.mkdir('C:\\Jarvis_files\\')
        os.mkdir('C:\\Jarvis_files\\zzps\\')
else:
    None


os.chdir('C:\\Jarvis_files\\zzps')

if(not os.path.exists("zzpslist.txt")):
        with open("zzpslist.txt", "w") as f:
            f.write("0")
        with open("zzpslist.txt", "r") as f:
            zzpass = f.read()
            
path = 'C:\\Jarvis_files\\zzps\\'

sha256_pass = "Write your Passcode SHA256 here"    #My password hashcode 
sha256_file = f"{path}zzpslist.txt" #My passlist file location
sha256_file = open(sha256_file, 'r')

for password in sha256_file:
    hash_obj = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()         #Decode the hashcode

    if hash_obj == sha256_pass:                     #Detects that hashcode or password is matching or not
        pword = password


def sendEmail(to, content):
    myMail = 'your email address'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(myMail, pword)
    server.sendmail(myMail, to, content)
    server.close()

def __init__(self):
        self.played = []
        self.video_ids = []
        self.media = None

    #	FUNCTION TO PLAY AUDIO
def ytplay(self, url):

        #	ADD URL TO LIST OF PLAYED SONGS
        self.played.append(url)

        #	INITIALIZE VIDEO
        video = pafy.new(url)
        audio = video.getbestaudio()
        self.media = vlc.MediaPlayer(audio.url)

        #	PRINT VIDEO DETAILS
        print(f"\n{'-' * 70}\n")

        print(bcolors.HEADER + "Now Playing: " + bcolors.OKCYAN + video.title)
        print(bcolors.HEADER + "\nViews: " + bcolors.OKCYAN + f"{video.viewcount:,d}")
        print(bcolors.HEADER + "\nDuration: " + bcolors.OKCYAN + video.duration)
        print(bcolors.WARNING + "\nPress 'CTRL+C' to Skip Song!\n" + bcolors.ENDC)

        with Progress(transient=True) as prog:
            song_play = prog.add_task(
                "[green]Playing Song", total=video.length)

            #	START PLAYER
            self.media.play()

            while self.media.is_playing() == False:
                pass

            while self.media.is_playing():
                sleep(1)
                prog.update(song_play, advance=1)

        print(bcolors.OKGREEN + "DONE PLAYING %s!" % video.title)

class ytplay_final:

    def __init__(self):
        self.played = []
        self.video_ids = []
        self.media = None

    def playvideo(self, url):

        #	ADD URL TO LIST OF PLAYED SONGS
        self.played.append(url)

        #	INITIALIZE VIDEO
        video = pafy.new(url)
        audio = video.getbestaudio()
        self.media = vlc.MediaPlayer(audio.url)

        #	PRINT VIDEO DETAILS
        print(f"\n{'-' * 70}\n")

        print(bcolors.HEADER + "Now Playing: " + bcolors.OKCYAN + video.title)
        print(bcolors.HEADER + "\nViews: " + bcolors.OKCYAN + f"{video.viewcount:,d}")
        print(bcolors.HEADER + "\nDuration: " + bcolors.OKCYAN + video.duration)
        print(bcolors.WARNING + "\nPress 'CTRL+C' to Skip Song!\n" + bcolors.ENDC)

        with Progress(transient=True) as prog:
            song_play = prog.add_task(
                "[green]Playing Song", total=video.length)

            #	START PLAYER
            self.media.play()

            while self.media.is_playing() == False:
                pass

            while self.media.is_playing():
                sleep(1)
                prog.update(song_play, advance=1)

        print(bcolors.OKGREEN + "DONE PLAYING %s!" % video.title)

    def autoplay(self, url):
        #	PLAY CURRENT VIDEO
        self.playvideo(url)

        self.video_ids = []
        video_ids_dupes = []
        #	CHANGE CURRENT VIDEO TO NEXT ONE
        html = urllib.request.urlopen(url)
        video_ids_dupes = re.findall(
            r"watch\?v=(\S{11})", html.read().decode())

        #	REMOVE DUPLICATES FROM LIST
        for i in video_ids_dupes:
            if "https://www.youtube.com/watch?v=" + i not in self.played:
                self.autoplay("https://www.youtube.com/watch?v=" + i)
                # RECURSION PAGMAN


    def search_playlist(self, search):
        playlistsSearch = PlaylistsSearch(search, limit=1)
        self.play_playlist(playlistsSearch.result()["result"][0]["link"])

    def search_youtube(self, search: str):
        # Check if the given search term is a valid youtube video link
        if(search.startswith("https://www.youtube.com")):
            res = urllib.request.urlopen(search)

            if(res.getcode() == 200):
                return search

        search_url = "https://www.youtube.com/results?search_query={}" + search.replace(" ", "+")

        html = urllib.request.urlopen(search_url)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        url = ("https://www.youtube.com/watch?v=" + video_ids[0])
        return url
        
    def ytplay_two(self):
            search = takeCommand().lower()
            print(bcolors.ENDC , end="")
            # search = "off the grid"				# For bug fixing
            url = self.search_youtube(search)
            try:
                self.playvideo(url)
            except KeyboardInterrupt:
                self.media.stop()
                del self.media
                exit()

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

def main():

    query = takeCommand().lower()

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

    elif 'play music' in query:
        
        try:
            music_dir = 'E:\\Songs\\Favourite Songs'
            songs = os.listdir(music_dir)
            # print(songs)
            list1 = random.choice(os.listdir(music_dir))
            os.startfile(os.path.join(music_dir, list1))
        except:
            speak("sorry sir!, can't play")
        #lst = len(songs-1)

    elif 'play song' in query:
        music_dir = 'D:\\Songs\\Favourite Songs'
        songs = os.listdir(music_dir)
        # print(songs)
        list1 = random.choice(os.listdir(music_dir))
        os.startfile(os.path.join(music_dir, list1))
        # lst = len(songs-1)

    elif 'i got success' in query:
        speak("oh, wow! congratulations...")

    elif 'thank you' in query:
        speak("welcome sir")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open vs code' in query:
        codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'open python' in query:
        pyPath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
        os.startfile(pyPath)

    elif 'send mail' in query:
        try:
            speak("to whom should I mail, sir?")
            codeLst = takeCommand()
            Cs1 = {"swayam":"takkamoreswayam@gmail.com","game maker":"gamemaker1456@gmail.com","mom":"takkamoren@gmail.com","s t productions":"stpros@1456","aryan":"","s t production":"stpros1456@gmail.com"}
            #print(Cs1)
            cslist = Cs1[codeLst]
            speak("what should I say?")
            content = takeCommand()
            to = cslist
            sendEmail(to, content)
            speak("Email has been sent!, sir")
        except Exception as e:
            print(e)
            speak("Sorry Sir, I am unable to send this mail")

    elif 'hello' in query:                                              # It reply on hello
        speak("hello sir!, I'm jarvis")

    elif 'good night' in query:                                              # It reply on Good Night
        speak("Very Good Night sir, Bye bye")
        exit()

    elif 'quit' in query:                                               # To Exit
        speak("quitting sir!")
        exit()

    elif 'exit' in query:                                               # To Exit
        speak("exitting sir!")
        exit()

    elif 'tata' in query:                                               # To Exit
        speak("tata sir!")
        exit()

    elif 'bye' in query:                                                # To Exit
        speak('bye sir!')
        exit()

    elif 'kya bolti public' in query:
        speak('O P bolti!')

    elif "what's up" in query:
        speak("I'm good, How about you dear!")

    elif 'how are you' in query:
        speak("I am Great, Hope you're also as I am")

    elif 'play from youtube' in query:
        speak("What do you want to play sir?")
        player=ytplay_final()
        try:
            player.ytplay_two()
        except:
            speak("Thank you sir")

    elif 'test the internet speed' in query:
        try:
            speak("Sure sir! please wait for let me test it")
            print("Testing...")
            test_run()
        except:
            speak("Sorry sir! Can't test")

    elif 'test internet speed' in query:
        try:
            speak("Sure sir! please wait for let me test it")
            print("Testing...")
            test_run()
        except:
            speak("Sorry sir! Can't test")



if __name__ == "__main__":

    wishMe()
    while True:                         #It is to take commands infinite times.
    #if 1:                             #It is to take only one command.
        query = takeCommand().lower()
        
        if query == 'hey jarvis':
            speak("yes sir!")
            main()

        if query == 'hi jarvis':
            speak("yes sir!")
            main()

        # Logic for executing tasks based on query
        # Code is still not completed...
        # Last Changes - 13/06/2023






        # Credit - Swayam Takkamore
