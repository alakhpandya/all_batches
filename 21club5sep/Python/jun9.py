# File Handling
# fp = open("first.txt")
# print(fp.read())
# fp.close()

"""
syntax: fp = open("file_path", "Mode1Mode2")
Mode1                   Description                                         Mode2
r       read mode       Opens the file for reading only.                    t       text mode       Default Mode
                        Raises FileNotFoundError if file does not exist.
                        Does not clear the content of the file.
                        Cursor is placed at the begining of the file.

w       write mode      Opens the file for writing only.                    b       binary mode
                        Creates the file if it does not exist.
                        Clears the content of the file at the time of opening
                        Cursor is placed at the begining of the file.

a       Append Mode     Opens the file for writing only.
                        Creates the file if it does not exist.
                        Does not clear the content of the file.
                        Cursor is placed at the end of the file.

x       Exclusively     Creates the file.
        Create          Also allow writing into the file.
                        Raises FileExistsError if the file already exists.
                        Cursor is placed at the begining of the file.

r+  read plus mode      Opens the file for reading and writing both.
                        Raises FileNotFoundError if file does not exist.
                        Does not clear the content of the file.
                        Cursor is placed at the begining of the file.

w+  write plus mode     Opens the file for writing and reading.
                        Creates the file if it does not exist.
                        Clears the content of the file at the time of opening
                        Cursor is placed at the begining of the file.

a+  Append plus Mode    Opens the file for writing and reading.
                        Creates the file if it does not exist.
                        Does not clear the content of the file.
                        Cursor is placed at the end of the file.

"""
# fp = open("second.txt", "rt")       # default mode
# fp.close()

# fp = open("second.txt", "r+t")
# fp.write("3")
# fp.close()

# fp = open("first.txt")
# print(fp.closed)
# content = fp.read()
# print(type(content))
# print(fp.readline())
# print(fp.readline())
# print(fp.readlines())
# fp.close()
# print(fp.closed)


f_user_data = open("user_data.txt")
user_data = f_user_data.readlines()
f_user_data.close()

print(user_data)
# for row in user_data:
#     print(row, end="")

def getUser_pwd(sr_no):
    return user_data[sr_no].split("\t")[3]

print(getUser_pwd(3))