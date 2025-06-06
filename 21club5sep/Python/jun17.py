# Resource management using "with"
"""
fp = open("first.txt", "a+")
fp.write("\nHello World!")
fp.close()
"""
"""
with open("first.txt", "a+") as fp:
    fp.write("\nHello World!")
    print(fp.closed)
print(fp.closed)
"""
class contextManager():
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        self.fp = open(self.file_name, self.file_mode)
        return self.fp

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.fp.close()
        print(exc_type)
        print(exc_value)
        print(exc_traceback)

fname = input("Enter file name: ")
fmode = input("Mode: ")

with contextManager(fname, fmode) as obj1:
    print(obj1.readline())

print(obj1.closed)