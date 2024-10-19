"""
2. Write a program to find the number of vowels, consonents and white space characters in a given string if there is no special characters other than spaces.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13

s = "Hello how are you"
spaces = s.count(" ")
print(spaces)
s2 = s.lower()
vowels = s2.count("a") + s2.count("e") + s2.count("i") + s2.count("o") + s2.count("u")
print(vowels)
consonents = len(s) - vowels
print(consonents)
"""
"""
fruits = ["apple", "banana", "kiwi", "grapes", "mangoes", "berries"]
i = 0
while i < len(fruits):
    print(fruits[i])
    if fruits[i] == "grapes":
        pass
    i += 1
print("Here are all your fruits...")
"""

# There is no "switch-case" in Python

# Basic calculator
"""
a = float(input("Enter two numbers:\n"))
b = float(input())

while True:
    operator = input("Operation (+, -, *, /, % or 'x' to quit): ")

    if operator == "+":
        print(f"{a} + {b} = {a + b}")
    elif operator == "-":
        print(f"{a} - {b} = {a - b}")
    elif operator == "*":
        print(f"{a} * {b} = {a * b}")
    elif operator == "/":
        print(f"{a} / {b} = {a / b}")
    elif operator == "%":
        print(f"{a} % {b} = {a % b}")
    elif operator == "x":
        break
    else:
        print("Please enter a valid operator. Try again...")

print("Thanks for using my calculator!")
"""

# Biggest use of while loop - to create infinite loops

# while True:
#     print("Something")

"""
HW: Modify the above code so that it flows as below:
Ask two numbers from user
ask operation
perform the operation
ask: do you want to continue or quit?
quit- print: Thanks for using my calculator!
continue- Ask: Do you want to enter new number or want to keep the same numbers?
    New numbers: repeat from Step-1
    Same numbers: repeat from Step-2
"""

# while-else??? = Break-Else
"""
1. Write a code that takes an integer from user and print whether it is divisible by 17 or not.
2. Write a code that takes an integer from user and print whether it is divisible by any number upto 17 (including 17) or not.
3. Write a code that takes an integer from user and print whether it is Prime or Composite.
"""