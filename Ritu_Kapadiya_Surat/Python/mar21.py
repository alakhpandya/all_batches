# Resource Management using 'with' statement
"""
# f = open('music.csv', 'a+')
# f.close()

with open('music.csv', 'a+') as f:  # same as f = open('music.csv', 'a+')
    f.seek(0)
    print(f.read())
print(f.closed)
"""

class ContextManager():
    def __init__(self, fileName, mode):
        self.fileName = fileName
        self.mode = mode

    def __enter__(self):
        # print("Enter Called...")
        self.fp = open(self.fileName, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print("Exit Called...")
        self.fp.close()
        print(exc_type)
        print(exc_value)
        print(traceback)

# f = ContextManager("music.csv", "r")
fileName = input("File name: ")
mode = input("Mode: ")
with ContextManager(fileName, mode) as f:
    # print("Hello World")
    print("Is the file closed? -", f.fp.closed)
    print(f.fp.read())
print("Is the file closed? -", f.fp.closed)
print("Program ended...")
"""
import speech_recognition as sr

sr.Microphone()
"""