# File handling

f = open("batch.txt")                   # same as f = open("batch.txt", "rt")

# print(f.read())
# print(f.read(20))
# data = f.read(50)
# data = f.read()
# print(data)
# print(type(data))

# print(f)
# for row in f:
#     print(row)

# print("cursor =", f.tell())
# print(f.read(50))
# print("cursor =", f.tell())
# print(f.read(20))
# print("cursor =", f.tell())

# f.seek(51)
# f.seek(0)
# print(f.read())

# print(f.readable())
# print(f.readline())
# print(f.readline())

# print(f.readlines())

f.close()

# Syntax for opening the file:
# file_pointer = open("file_path", "Mode1Mode2")

# Modes:
"""
Mode1   Name of the mode    Description                                         Mode2   Name of the mode
r       read                It opens the file for reading only.                 t       text mode               Default
                            Cursor is placed at the begining of the file.
                            Does not create the file if it does not exist.
                            Does not erase the content of the file.

w       write               Opens the file for writing only.                    b       binary mode
                            Creates the file if it does not exist.
                            Erase the entire content of the file at the time of opening.
                            Cursor is placed at the begining of the file.

a       append

"""

f = open("myFile.txt", "w")      # same as f = open("batch.txt", "wt")
# print(f.readable())
# print(f.writable())

f.write("This is the first file that I am writing using Python...")

sample_list = [
    "Hey, how are you?\n",
    "I thought I will find you at the park, but you were not there.\n",
    "So, I visited the temple and came back to the home."
]
f.writelines(sample_list)

# print(f.closed)
f.close()
# print(f.closed)

