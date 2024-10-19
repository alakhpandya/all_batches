import pyttsx3

engine = pyttsx3.init()
# engine.say("Good Evening Krisha!")
# engine.runAndWait()

# print(engine.getProperty("rate"))

engine.setProperty("rate", 175)

# engine.say("Hello! Echo here, Good evening!")
# engine.runAndWait()

# sapi5 = sound API

# print(engine.getProperty("voices"))
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("I hope I am a female voice!")
engine.runAndWait()

print(engine.getProperty("volume"))