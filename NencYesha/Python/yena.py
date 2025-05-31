import pyttsx3
from datetime import datetime
import speech_recognition as sr
from googlesearch import search
import wikipedia
import webbrowser
# from google import google
import os
from AppOpener import open, close, give_appnames


BOSS = "Nency & Yesha"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.now().hour
    # hour = 2
    if 5 <= hour < 12:
        speak("Good Morning" + BOSS)
    elif 12 <= hour < 16:
        speak("Good Afternoon" + BOSS)
    elif 16 <= hour < 20:
        speak("Good Evening" + BOSS)
    elif 20 <= hour < 24:
        speak("Good Night" + BOSS)
    else:
        speak(BOSS + "You should be sleeping at this moment")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("How may I help you?")
        print("Listening...")
        audio = r.listen(source)
    command = ""
    try:
        command = r.recognize_google(audio)
        print("I think you said: " + command)
    except sr.UnknownValueError:
        print("I could not understand what you just said. Would you mind repeating it please?")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return command.lower()

# initializing pyttsx3
engine = pyttsx3.init()

# changing the speed of speaking
engine.setProperty('rate', 160)

# changing voice to a female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# main
greet()

while True:
    command = takeCommand()
    if "bye" in command or "see you" in command:
        break

    print(command)
    if command.startswith('what') or command.startswith('where') or command.startswith('which') or command.startswith('who') or command.startswith('when') or command.startswith('how'):
        
        # what is the capital of India?
        """
        results = google.search(command, 1)
        speak('wait, let me think...')
        for result in result:
            # print(search)
            if 'wiki' in result.description:
                terms = search.split('/')
                term = terms[-1]
                info = wikipedia.summary(term, sentences = 2)
                print(info)
                speak(info)
        
        """
        terms = command.split('the')
        # print(terms)
        term = terms[-1].lstrip()
        info = wikipedia.summary(term, sentences = 2)
        print(info)
        speak(info)
        

    if "youtube" in command:
        url = "https://youtube.com"
        webbrowser.open(url)

    if "open" in command and ".com" not in command:
        pass

    if "." in command:
        terms = command.split()
        for term in terms:
            if "." in term:
                website = term
                break
        if "https" not in term:
            url = "https://" + website
        webbrowser.open(url)
        

    if "vs code" in command or "visual studio code" in command:
        # print("if exectued for command:", command)
        path = "C:\\Users\\Alakh Pandya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    if "application" in command:
        terms = command.split()
        for i in range(1, len(terms)):
            if "application" in terms[i]:
                term = terms[i-1]
        apps = give_appnames()
        appList = []
        for app in apps:
            if term in app:
                appList.append(app)
        # print(appList)
        if len(appList) > 1:
            for application in appList:
                print(application)

            print("Which one do you want to open?\n")
            speak(f"There are {len(appList)} apps matching your choice. Which one do you want to open?\n")
            final_app = takeCommand()
        open(final_app)

speak("Good bye" + BOSS)