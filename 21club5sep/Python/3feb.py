"""
Write a Python code to print the following message:

In Python "\t" is used to give a "tab". But, if you want to print '\t', you need to type '\\t'
"""
"""
Escape sequence characters in Python:
\	Escape Sequence Character
\t	tab
\n	new line
\b	backspace
\r	carriage return
"""

"""
print("Hello Python!\b\b\bRoyal")
print("Hello Python!\rRoyal")
"""
# end statement
"""
print("Hello Viral!", end="\t")
print("987654321")

print("Hello Viral!", end="")
print("987654321")

print("Hello Viral!", end=" Mobile no: ")
print("987654321")

print("Hello Viral!", end=" ")
print("987654321")

print("Hello Viral!", end="\b\b\b")
print("987654321")

print("Hello Viral!", end="\r")
print("987654321")

print("Hello Viral!\n")
print("987654321")
"""
# variables in Python
"""
a = 5
print("a")
print(a)
print("a =", a)
print(type(a))

b = 9834598109837510982374598710987413295981347698714098729803741967941387598132740981745908324769081789041327490871340698710943875198023740918273598071349801790874508917349087139082472139847

print("b =", b, "\ntype of b :", type(b))

c = 56.78
print("c =", c, "\ntype of c :", type(c))

d = 6 + 4j
print("d =", d, "\ntype of d :", type(d))

e = "5"
f = '6'
# there is no "char" datatype in Python. It is "str" only.
# g = Ahmedabad			Error
# h = 6 + j4			Error
"""
# Taking inputs
# option - 1:
"""
print("Enter an integer:")
a = int(input())
print("a =", a)
# option - 2:
b = float(input("Enter second integer: "))
print("b =", b)
# print(a, "+", b, "=", int(a) + float(b))
print(a, "+", b, "=", a + b)
print("type of a:", type(a))
print("type of b:", type(b))
"""
# option - 3:
print("Enter two integers:")
a = int(input())
b = int(input())
print("a/b =", a/b)
"""
HW:
Write a Python code that takes 5 integers from user (call them a, b, c, d & e) and print their average EXACTLY as below:
sample execution:
Enter 5 integers:
3
4
5
6
7
The average of 3, 4, 5, 6 and 7 is: 5.0
"""