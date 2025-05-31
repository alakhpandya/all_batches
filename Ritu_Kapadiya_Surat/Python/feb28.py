# File Handling
"""
Mode1       Name        Description                                                             Mode2   Name
r           read        Opens the file for reading operation only                               t       Text    #default
                        Returns the FileNotFoundError if the file does not exist
                        Places the cursor at the begining of the file
                        Does not erase the content of the file at the time of opening

w           write       Opens the file for writing only                                         b       Binary
                        Creates the file if the file does not exist
                        Clears the entire content of the file at the time of opening
                        Cursor is placed at the begining of the file.

a           append      Opens the file for writing only
                        Creates the file if the file does not exist
                        Does not clear the content of the file
                        Cursor is placed at the end of the file.

x           Exclusive   Creates the file if does not exist
            Create      Returns the FileExistsError if the file is already existing
                        Allows write operation only

r+          Read Plus   Opens the file for reading & writing both
                        Returns the FileNotFoundError if the file does not exist
                        Places the cursor at the begining of the file
                        Does not erase the content of the file

w+          Write Plus  Opens the file for writing and reading both
                        Creates the file if the file does not exist
                        Clears the entire content of the file at the time of opening
                        Cursor is placed at the begining of the file.

a+          Append Plus Opens the file for writing & reading both
                        Creates the file if the file does not exist
                        Does not clear the content of the file
                        Cursor is placed at the end of the file.
"""
# Syntax:
# name_of_file_pointer = open("file_name_with_extension_and_full_path", "Mode1Mode2")

# File Created: first.txt
"""
f = open('first.txt')
print(f.read())
f.close()

f_external = open('D:\\Royal\\Python\\new_folder\\temp.txt')
print(f_external.read())
f_external.close()
"""
"""
f = open("second.txt", "r")

f.close()
"""
# f = open("first.txt", "rt")
# f = open("first.txt")
"""
# data = f.read()
data = f.read(10)
print(data)
# print(type(data))
data2 = f.read(15)
print(data2)
print("Cursor's position:", f.tell())
f.seek(40)
print("Cursor's position:", f.tell())
print(f.read())
f.seek(0)
print("Cursor's position:", f.tell())
"""
"""
first_line = f.readline()
print(first_line)
second_line = f.readline()
print(second_line)

# f.write("15")
print(f.writable())
print(f.readable())


data = f.readlines()
print(data)
"""
# f.close()
"""
f = open("Second.txt", "wt")
f.write("Ritu won the first prize!")
a = "50"
f.write(a)
myContent = [
    "\nToday is 4th March...\n",
    "We will remember today's date.."
]
f.writelines(myContent)

f.close()
"""
"""
f = open("first.txt", "a")
f.write("\nToday is Saturday.")
f.close()
"""
"""
f = open("third.txt", "x")
print(f.writable())
f.close()
"""
"""
f = open('first.txt', 'r+t')
# print(f.writable())
# print(f.readable())
f.read()
f.write("I am so happy with this Mode!")
f.close()
"""
"""
f = open("third.txt", "w+")
f.write("I am not very sure that I liked this Mode...")
f.seek(0)
print(f.read())
f.close()
"""

# An example of file handling: A file that is having the following format:
"""
Batch: Python
Days: Tuesdays & Saturdays
Sr.No   Name            Role
0       Alakh           Instructor
1       Ritu            Student
2       Vedika          Student
3       Dhyani          Student
4       Aarav           Student
5       Shruti          Management
"""