s1 = "Today is Thursday in India and in San Diego it must be running Wednesday"
print(s1)
# print(type(s1))

x = len(s1)
print(x)

# Methods vs Functions
len(s1)
# print(s1.upper())
a = 25
# a.upper()     Error

# Methods of strings
s1.capitalize()     # converts the first character of the string into uppercase and every other char into lower case
# s1 = s1.upper()
# print(s1)
# print(s2)

s1.casefold()   # converts into lower case
s1.lower()   # converts into lower case
s1.upper()  # converts into upper case
s1.title()  # converts first character of every word into upper case and every other character into lowercase
s1.swapcase()   # swap the uppercase characters into lower & vice versa


# print(s1.center(100))
# print(s1.center(100, "-"))
# print(s1.center(150, "@"))
# print(s1.center(50, "@"))
# print(s1.ljust(100, "%"))
# print(s1.rjust(100, "$"))
# print(s1.rjust(100))

# s2 = "Hello"
# s3 = s2*5
# print(s3)
# s4 = "World"
# s5 = s2+s4
# print(s5)

"""
 -------------------------------------------------------------------------------
|                      Welcome to the Python Course for DS                      |
 -------------------------------------------------------------------------------

The location of Python interpreter in your system is: "C:\program Files\new Folder\temp\python\"
"""
# strings: Ordered & Immutable sequece of characters.

s1 =    "Today is Thursday in India and in San Diego it must be running Wednesday and it's a nice day!"
# index: 0123456789..................................................................................92

print(s1.count("a"))
# print(s1.count("A"))
# print(s1.count("it"))
# print(s1.count("day"))
# print(s1.count("and"))
print(s1.count("a", 9))
print(s1.count("a", 9, 70))     # first included, last excluded

# Next Class: String slicing