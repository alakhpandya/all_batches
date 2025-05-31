# What is True & what is False, if-else etc

# 1 means True

# a = True
# print(type(a))

# b = int(input("b: "))
# if True:
#     print("Be positive")

# c = bool(float(input("c: ")))
# c = ""
# c = []
# c = ()
"""
c = False
if c:
    print("C is True")
else:
    print("C is False")
"""
"""
False: 0, Empty string "", Empty list [], Empty tuple (), Empty set, Empty frozenset, Empty dictionary
True: 1 or any non-zero number, True, In fact anything that Python doesn't treat as False will be treated as True.
"""
"""
a = float(input("a: "))
c = 5
if a > 0:
    print("'a' is positive!")
    c += 1
    print("New value of c =", c)
# print("if done")      Error
elif a == 0:
    print("'a' is zero!")
    print("New value of c =", c)
else:
    print("'a' is negative!")
    c -= 1
    print("New value of c =", c)
print("Thanks for using our program!")

a = int(input("a : "))
b = int(input("b : "))
if a >= b:
    print("a >= b")
# print("1st block done...")
if a == b:
    print("a == b")
# print("2nd block done...")
if a <= b:
    print("a <= b")
# print("Program finished.")


a = int(input("a : "))
b = int(input("b : "))
if a >= b:
    print("a >= b")
elif a == b:
    print("a == b")
elif a <= b:
    print("a <= b")
print("Program finished.")
"""

# shorthand if, if-else

# a = int(input("a : "))
# if a > 0: print("'a' is positive.")
# print("End of the program!")

a = int(input("a : "))

print("'a' is either positive or zero") if a >= 0 else print("'a' is negative.")
"""
if a >= 0: 
    print("'a' is either positive or zero.")
else:
    print("'a' is negative.")
"""
print("End of the program!")

# There is no shorhand notations for if-elif-else ladder

# HW for this week:
"""
1. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. 
Example:
input: Alakh Janakkumar Pandya
output: A.J.Pandya
2. Write a program to find the number of vowels, consonents and white space characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13 
3. Write a Python code that prints the index numbers of all the occurrences of "o" in a given string of length 5.
4. Write a program to make a new string with the word "the" deleted in the given string.
eg:
input string: This is the lion in the cage.
output: This is lion in cage.
5. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
Example:
input string: Keep yourself mute while not speaking.
output: Keep_yourself mute while not#speaking.

If-else examples:
1. A school has following grading system. Write a Python code that takes percentage of a student and display his/her grade.
below 35%       :   F
from 35 to 44   :   E
from 45 to 54   :   D
from 55 to 64   :   C
from 65 to 74   :   B
75 or more      :   A

2. Write a Python program to find whether a given year is a leap year or not. 
Test Data : 2016
Expected Output :
2016 is a leap year.
"""