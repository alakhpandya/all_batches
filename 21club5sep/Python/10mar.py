# Most wide use of while loop: to create infinite loop
"""
while True:
    print("Enter two numbers:")
    a = float(input())
    b = float(input())
    choice = input("Enter operation: +, -, * or /\n")
    if choice == "+":
        print(f"{a} + {b} = {a+b}")
    elif choice == "-":
        print(f"{a} - {b} = {a-b}")
    elif choice == "*":
        print(f"{a} * {b} = {a*b}")
    elif choice == "/":
        print(f"{a} / {b} = {a/b}")
    else:
        print("Invalid Operation, please try again...")
    quit = input("Want to quit? Y/N?\n").lower()
    if quit == "y":
        break
"""
# while - else : call it break-else
"""
1. Ask a number from user and determine whether it is prime or not.
"""
"""
n = int(input("Enter any integer: "))
i = 2
while i < n**0.5 + 1:
    if n % i == 0:
        print("Not Prime.")
        break
    i += 1
else:
    print("Prime.")
"""
fruits = ["Apple", "Banana", "Kiwi", "Mango", "Grapes", "Orange"]
"""
i = 0
while i < len(fruits):      # i = 0,1,2,3,4,5
    print(fruits[i])
    i += 1
"""
for i in fruits:    # i = "Apple", "Banana", "Kiwi", "Mango", "Grapes", "Orange"
    print(i)
