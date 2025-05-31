"""
s1 = "Python is fun @ ROYAL with all the faculties."
print(s1.partition("ROYAL"))
print(s1.partition("th"))
print(s1.partition(" "))
print(s1.rpartition("th"))
print(s1.rpartition(" "))

print(s1.replace("fun", "awsome"))
# print(s1.replace(" ", "_"))
print(s1.replace(" ", "_", 3))

s2 = "Ashesh learns Python.\nHe learns it quickly.\nHe will be graduate in the spring 2023.\nAll the best Ashesh!"
print(s2.splitlines())
# print(s2)
# print(s1.strip.__doc__)
# print(help(s1.strip))

day = input("Enter today's date & month number:")   # 02    21
month = input() # 11   04
print(f"Today's date in dd/mm/yyyy format: {day.zfill(2)}/{month.zfill(2)}/2022")
"""
# Homework:
"""
String-list examples:
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
3.  Write a Python code that prints the index numbers of all the occurrences of "o" in a given string of length 5.
4. Write a program to make a new string with the word "the" deleted in the given string.
eg:
input string: This is the lion in the cage.
output: This is lion in cage.
5. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
"""

# list: Ordered and Mutable collections of members
# Ordered means:
"""
Unique positive and negative index numbers of each and every member
Access the element by its +ve or -ve index number
Slicing is available - slicing never changes the original data, it returns you a new collection of the same type.
Slicing can be done with +ve or -ve step, with -ve index and/or with one -ve one +ve index combined.
"""
numbers = [11, 22, 33, 44, 11, 9, 13, 11, -56, 7.56, -15.87, 11, 37, 11]
n2 = numbers[-2: 2: -2]
print(numbers)
print(n2)
print(type(numbers))
print(len(numbers))

print(min(numbers))
print(max(numbers))
print(sorted(numbers))      # sorted() always gives you a NEW LIST.
print(sorted(numbers, reverse=True))

# what will happen if we apply these functions on strings?