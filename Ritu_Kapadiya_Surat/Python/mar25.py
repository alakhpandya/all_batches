# Virtual Assistant- speech recognition, produce speech
"""
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio)
    print("I think you said- " + command)
except sr.UnknownValueError:
    print("Sorry, would you please repeat...")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


import pyttsx3
engine = pyttsx3.init()


# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print(rate)                        #printing current voice rate
engine.setProperty('rate', 175)     # setting up new voice rate


voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

engine.say("I will speak this text")
engine.runAndWait()
"""

import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Say something")
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("I think you said- " + command)
    except sr.UnknownValueError:
        speak("Sorry, would you please repeat...")
        print("Sorry, would you please repeat...")
        command = ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        command = ""

    return command



# main program:
speak("Hello Ritu how can I help you?")
command = listen()
print(command)
