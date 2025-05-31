"""
1. Listen what we speak - Reproducing speech into text (Speech Recognition)
2. Understand the meaning
3. Action:
    greet
    opening a website
    finding something from wiki
    opening an app on the computer
    play songs
    open pictures from the computer
4. Speak - Text To Speech (TTS)
"""

"""
import pyttsx3

engine = pyttsx3.init() 

# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 175)     # setting up new voice rate

voices = engine.getProperty('voices')
print(voices)
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


engine.say("Hello Nency & Yesha")
engine.runAndWait()
"""
"""
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Say something!")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("I think you said: " + command)
    except sr.UnknownValueError:
        print("I could not understand what you just said. Would you mind repeating it please?")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return command
"""
from AppOpener import open, close, give_appnames

apps = give_appnames()
application = input("App name: ")
appList = []
for app in apps:
    if application in app:
        appList.append(app)
print(appList)
if len(appList) > 1:
    for x in appList:
        print(x)
    final_app = input("Which one do you want to open?\n")