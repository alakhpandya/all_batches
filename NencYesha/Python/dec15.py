# infinite while loop
"""
a = float(input("Enter two numbers:\n"))
b = float(input())
while True:
    op = input("Which operation do you want to perform? +, -, *, / or x to exit:")
    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} * {b} = {a * b}")
    elif op == "/":
        print(f"{a} / {b} = {a / b}")
    elif op == "x":
        break
print("Thanks! See you soon!")
"""
# for loop
"""
fruits = ["Blueberries", "Orange", "Apple", "Strawberries", "Banana", "Guava"]
for i in fruits:        # i = "Blueberries", "Orange", "Apple", "Strawberries", "Banana", "Guava"
    if i == "Banana":
        # break
        # continue
        pass
    print(i)
"""
# range:
# print(range(5))
"""
# for i in range(5):
# for i in range(5, 10):
# for i in range(5, 15, 2):
# for i in range(5, 15, 3):
# for i in range(15, 5, -1):
#     print(i)
"""

# for-else: break-else
"""
n = int(input("Enter any integer: "))
for i in range(2, n):       # i = 2,3,4,5....,n-1
    if n % i == 0:
        print("Not prime...")
        break
else:
    print("Prime.")
"""
