# File Handling
"""
f = open("trial2.txt")       # same as f = open("trial.txt", "rt")
# print(f.read())           Reads the entire file
# print(f.read(10))         Reads first 10 characters
# print(f.read(15))         Reads next 15 characters
# print(f.readline())       # Reads 1st line of the file
# print(f.tell())
# f.seek(15)
# print(f.read())
print(f.readlines())
f.close()

Modes in Python:
Mode1   Name    Mode2   Name
r       read    t       text    Default
w       write   b       binary
a       append
x       exclusively create
r+      read plus
w+      write plus
a+      append plus
syntax:
f = open("file path", "Mode1Mode2")

Modes in Detail:
Mode    Name        Description
r       Read        Opens the file to read. (Can't write)
                    Reading starts from the begining of the file.
                    (Cursor is placed at the begining of the file.)
                    Does not create file if it is not existing, returns FileNotFoundError.
                    Does not clear the content of the file as soon as it is open.


w       Write       Opens the file for writing. (Can't read)
                    Creates the file if it does not exist.
                    Clears the entire content of the file as soon as it is open.
                    Writing starts from the begining of the file.
                    (Cursor is placed at the begining of the file.)

a       append      Opens the file for writing. (Can't read)
                    Creates the file if it does not exist.
                    Does not clear the content of the file.
                    Writing starts from the end of the file.
                    (Cursor is placed at the end of the file.)

x       exclusive   Creates the file. (Can't read, but can write)
        create      If the file already exists, raise FileExistsError.
                    Writing starts from the begining of the file.
                    (Cursor is placed at the begining of the file.)

r+      read plus   Opens the file to read and write both.
                    Reading/writing starts from the begining of the file.
                    (Cursor is placed at the begining of the file.)
                    Does not create file if it is not existing, returns FileNotFoundError.
                    Does not clear the content of the file.

w+      write plus  Opens the file for writing and reading both.
                    Creates the file if it does not exist.
                    Clears the entire content of the file as soon as it is open.
                    Writing/Reading starts from the begining of the file.
                    (Cursor is placed at the begining of the file.)

a+      append plus Opens the file for writing and reading both.
                    Creates the file if it does not exist.
                    Does not clear the content of the file.
                    Writing/reading starts from the end of the file.
                    (Cursor is placed at the end of the file.)
"""
# Write Mode:
f = open("trial.txt", "w")      # same as f = open("trial.txt", "wt")
# print(f.readable())
# print(f.writable())
# f.write("\nbecause Mihir's Unity was completed first.")
f.close()
