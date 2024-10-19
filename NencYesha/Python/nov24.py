# loops: while loop, for loop
"""
i = 1
while i <= 5:
    print("Hello World!")
    i += 1
print("End of the code...")
"""
# There is no switch case in Python
"""
print("Enter two numbers:")
a = float(input())
b = float(input())

while True:
    op = input("Enter operation (+, -, *, /, sin to find sin(a) or 'x' to quit or 'y' to skip this iteration) : ")
    if op == "+":
        print(f"{a} + {b} = {a+b}")
    elif op == "-":
        print(f"{a} - {b} = {a-b}")
    elif op == "*":
        print(f"{a} * {b} = {a*b}")
    elif op == "/":
        print(f"{a} / {b} = {a/b}")
    elif op == "x":
        break
    elif op == "y":
        continue
    elif op == "sin":
        pass
    else:
        print("Sorry, this operation is not availabe presently. Please try again...")
    
    print("Your operation is performed...")
print("End of the code...")
"""

fruits = ["Blueberries", "Orange", "Apple", "Strawberries", "Banana", "Guava"]
i = 0
while i < len(fruits):      # i = 0,1,2,3,4,5...
    if fruits[i] == "Banana":
        # break
        pass
    print(fruits[i])
    i += 1
print("Thanks for having fruits!")