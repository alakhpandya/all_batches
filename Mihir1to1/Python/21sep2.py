# Resourse Management using with statement.
# Normal Progarm without "with" statement
"""
f = open("trial.txt", "a+t")
f.write("Let's wait for Sunday.")
f.close()
"""
# Same program using "with" statement
"""
content = input("Enter content: ")
with open("trial.txt", "a+t") as f:     # same as f = open("trial.txt", "a+t")
    f.write("\n" + content)
print(f.closed)
"""

# With block in OOP
class FileManager():
    def __init__ (self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__ (self):
        self.f = open(self.file_path, self.mode)
        return self.f

    def __exit__ (self, exc_type, exc_value, exc_traceback):
        self.f.close()
        print(exc_type)
        print(exc_value)
        print(exc_traceback)

# obj1 = FileManager("trial2.txt", "w")
content = input("Enter content: ")
with FileManager("trial2.txt", "w") as obj1:
    obj1.write(content)

print(obj1.closed)

# Program flow:
"""
1. obj1 = FileManager("trial2.txt", "w") will be created. (__init__ will be called)
2. __enter__() will be called. obj1.f = open(obj1.file_path, obj1.mode) will be created.
3. code written inside with block will be executed. content will be written in the file.
4. __exit__() will be called. obj1.f.close() will be executed.
"""