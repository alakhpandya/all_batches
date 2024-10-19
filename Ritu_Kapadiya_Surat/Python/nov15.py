# Loops: while, for
"""
i = 5
while i > 0:
    print(f"{6-i}. Hello World!")
    i -= 1
# print(i)
"""
# iterating through a collection using while loop:
"""
fruits = ["mango", "banana", "cherry", "peach", "apple"]
i = -1
while i < len(fruits)-1:
    i += 1
    if fruits[i] == "peach":
        # break
        # continue
        pass
    print(fruits[i])
"""

"""
myString = "mango"
j = 0
while j < len(myString):    # j = 0,1,2,3,4
    print(myString[j])
    j += 1
"""

# infinite loops:
"""
print("Enter two numbers:")
a = float(input("a = "))
b = float(input("b = "))

while True:
    op = input("Operation (+, -, *, / or x to quit): ")
    if op == "+":
        print(f"{a} + {b} = {a+b}")

    elif op == "-":
        print(f"{a} - {b} = {a-b}")

    elif op == "*":
        print(f"{a} * {b} = {a*b}")

    elif op == "/":
        print(f"{a} / {b} = {a/b}")

    elif op.lower() == "x":
        break

    else:
        print("Invalid Operation, please try again...")
        
"""
# Ask a integer from user and print whether it is prime or not.
# 641: 2,
"""
n=int(input("Enter a number:"))
i=2
flag = 1
while i<n/2:
    if n%i==0:
        flag = 0
        break
    i += 1

if flag == 1:
    print("Prime")
else:
    print("Not Prime")
"""

# while-else: break-else

n=int(input("Enter a number:"))
i=2
while i<=n/2:
    if n%i==0:
        print("Not Prime")
        break
    i += 1
else:
    print("Prime")