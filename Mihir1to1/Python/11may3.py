# If conditions
# Make a Python program to check if the given number is positive or not.
"""
number = float(input("Enter any number: "))
# Python is indent-oriented language
if number > 0:
    print(f"{number} is positive...")
elif number == 0:
    print(f"{number} is neutral...")
else:
    print(f"{number} is negative...")
"""
# shorthand notations (valid only for one senetenced if):
"""
number = float(input("Enter any number: "))
if number > 0: print(f"{number} is positive...")

number = float(input("Enter any number: "))
print(f"{number} is positive...") if number > 0 else print(f"{number} is negative...")
"""
# We don't have shorthand notation for if... elif... else
# THERE IS NO SWITCH CASE IN PYTHON
# Calculator Program
print("Enter two numbers:")
number1 = float(input())
number2 = float(input())
print("Enter:")
print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")
choice = int(input())
if choice == 1:
    print(f"{number1} + {number2} = {number1 + number2}")
elif choice == 2:
    print(f"{number1} - {number2} = {number1 - number2}")
elif choice == 3:
    print(f"{number1} * {number2} = {number1 * number2}")
elif choice == 4:
    print(f"{number1} / {number2} = {number1 / number2}")
else:
    print("Invalid operation.. please try again!")