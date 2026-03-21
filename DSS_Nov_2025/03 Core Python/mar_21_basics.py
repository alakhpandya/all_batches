# print("Hello!")
# print('Welcome!')     # In-line comment
# print("Hello Everyone!")

"""
This is
Not a 
Multi-line comments
This are strings only but mostly used as
Docstring.
"""

# print("Good Morning!!")
# print("""Happy learning!!""")

# Creating variables in Python
a = 98
# print("a", end="\n")    # default
# print("a", end="")    # default
# print("a", end="\t")    # default
# print("a", end=",")    # default
# print(a)

# print("a =",a)
# print("a =", a, " - this is your variable")

b = 109.95
# print(type(a))
# print(type(b))

c = "Python"
# print(type(c))

a = 98094387237485890749010932844598419374983479807143298047524398079018324798013434
b = 98094387237485890749010932844598419374983479807143298047524398079018324798013434.98094387237485890749010932844598419374983479807143298047524398079018324798013434
# print(type(b))

# print(type(False))

a = "Saturday"
b = a * 5
# print(b)

# Taking inputs from the user
x = """
a = input("Enter a: ")
print("You entered:", a)
b = input("Enter b: ")
print(a + b)
"""
# print(x)

d = '''Hello Students,
I am glad to inform you about some news.'''


# Typecasting
"""
a = 90.7
b = str(a)
print("b =", b)
print(type(b))
c = float(b)
print("c =", c)
print(type(c))
d = int(c)
print("d =", d)
"""

# Calculator program
"""
a = float(input("a: "))
b = float(input("b: "))

op = input("+, -, * or /: ")
# There is no switch-case in Python
if op == "+":
    ans = a + b
    print("sum =", ans)
elif op == "-":
    ans = a - b
    print("diff =", ans)
elif op == "*":
    ans = a * b
    print("Multiplication =", ans)
elif op == "/":
    ans = a/b
    print("Division =", ans)
else:
    print("Please enter a valid operation")
"""

# Loops in Python: while, for
"""
a = int(input("a: "))       # 3
while a > 0:        # a = 3, 2, 1, 0
    print("Loop is running")
    a -= 1      # a = a - 1
    # a-- is not available in Python
"""
"""
# a = True
# while a:
while True:
    hw = input("Did you complete the homework? y/n: ")
    if hw == "n":
        print("Complete it.")
    elif hw == "y":
        pass
        # a = False
        break
    else:
        print("Enter a valid choice.")
"""
"""
1. Create a calculator program
2. Put it in an infinite while loop - Give user one more operation "x" to exit the loop
"""

print("*" * 100)
print("Welcome to calculator".center(100))
print("*" * 100)

a = float(input("a: "))
b = float(input("b: "))
while True:
    op = input('+, -, *, / or "x" to exit: ').lower()
    if op == "+":
        ans = a + b
        print("sum =", ans)
    elif op == "-":
        ans = a - b
        print("diff =", ans)
    elif op == "*":
        ans = a * b
        print("Multiplication =", ans)
    elif op == "/":
        ans = a/b
        print("Division =", ans)
    elif op.lower() == "x":
        break
    else:
        print("Please enter a valid operation")