# Import Area
import pyttsx3
from datetime import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia

# Global Variables & Constants
engine = pyttsx3.init()
engine.setProperty("rate", 175)



# Function Area
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    time = datetime.now().hour
    speak("Hello! Please tell me your name...")
    user = getCommand()
    if 4 <= time < 12:
        speak("Good Morning" + user)
    elif 12 <= time < 17:
        speak("Good Afternoon" + user)
    elif 17 <= time < 24:
        speak("Good Evening" + user)
    else:
        speak("You should now consider sleeping..." + user)


def getCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:   # source = sr.Microphone()
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")
            audio_file = r.listen(source)
            print("Recognizing...")
            command = r.recognize_google(audio_file)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        command = ""
         
    except sr.UnknownValueError:
        print("unknown error occured")
        command = ""

    return command


# Main Program
# wishMe()
print("How may I help you?")
speak("How may I help you?")
command = getCommand().lower()      # "open google.com"
print(command)
if "www" in command or "dot" in command:
    if "www" not in command:
        command = "www." + command
    webbrowser.open(command)

if "application" in command:
    cmd_list = command.split()
    app = cmd_list[cmd_list.index("application") - 1]
    os.system(app)

if "wikipedia" in command:  # search sportsbike on wikipedia
    cmd_list = command.split()
    search_term = cmd_list[cmd_list.index("wikipedia") - 2]
    search_result = wikipedia.summary(search_term, sentences=2)
    print(search_result)
    speak(search_result)

if "song" in command or "music" in command or "play" in command:
    song_folder = "D:\songs"
    song_names = os.listdir(song_folder)
    os.startfile(os.path.join(song_folder, song_names[0]))
