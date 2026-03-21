# print("$"*10)
print("="*50)
print("Welcome to calculator")
print("="*50)

"""
a = 13
# print(a)
print("a =", a)
print(type(a))

b = 17.5
print("b =", b)
print(type(b))

c = "55"
print("c =", c)
print(type(c))

"""
# d = input("Type something:")
# print("You typed:", d)

# e = int(input("Enter a number: "))
# f = float(input("Enter another number: "))
# print("Sum =", e + f)

# x = 928349509274385978460952794072089475025987094782509348702985724398572095873409587529857342098754325987234059872345986093847589769023475894376098324750349875203987
# print(x)
# print(type(x))
"""
a = int(input("a = "))
b = int(input("b = "))
op = input("Operation (+, -, * or /): ")

if op == "+":
    print("sum =", a+b)
elif op == "-":
    print("difference =", a-b)
elif op == "*":
    print("multiplication =", a*b)
else:
    print("Try again...")

ex = input("Enter X to exit or any other key to repeat: ")
print("End of the code.")

"""

# While loop
"""
x = 5
while x > 0:
    print("x =", x)
    print("Inide the loop.")
    # x = x - 1
    x -= 1
"""
print("Out of the loop.")

# Infinite while loop:
while True:
    x = int(input("Enter a +ve number: "))
    if x > 0:
        break
    else:
        print("You have not entered a positive number, try again.")

print("Congratulations!!")