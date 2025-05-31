# Escape sequence characters
# Taking input through msg in input()
# f-string
"""
Escape sequence characters:
\
\n      New line character
\t      Tab character
\b      Backspace
\r      Carriage return
"""
# print('Alpha said Beta"Gammma is teasing Delta"')
# print("I don't want to become web developer")
# print('Alpha said Beta"Gammma is teasing Delta but Gamma says I',"didn't",'tease delta"')
# print('the loccation of python interpreter is "c:\\new folder\\temp\\Python"')

# print("Alpha said Beta \"Gammma is teasing Delta but Gamma says I didn't, tease delta\"")
# print('the loccation of python interpreter is "c:\\new folder\\temp\\Python\\"')
# print("Python\b\b\bRoyal")
# print("Python\b\b\bR")
# print("Weekends are comming!\rSunday")

# Taking inputs:
"""
print("Enter a number:")
a = int(input())
b = float(input("Enter second number:\n"))
print("sum =", int(a) + float(b))
print(type(a))
print(type(b))
c = 98372461987641781698372469178469817234698172569871643928561498561987613240783408104510324813458134501830098437289574398272798395782042795
print(c, type(c))
d = 9837246198764178169837246917846981723469817256987164392856.1498561987613240783408104510324813458134501830098437289574398272798395782042795
print(d, type(d))
"""
# print("Enter five numbers:")
"""
i = 1
a = float(input(f"Enter number - {i}: "))
i += 1
b = float(input(f"Enter number - {i}: "))
c = float(input())
d = float(input())
e = float(input())
# print("Average of", a, "\b,", b, "\b,", c, "\b,", d, "&", e, "is:", (a+b+c+d+e)/5)
print(f"Average of {a}, {b}, {c}, {d} & {e} is: {(a+b+c+d+e)/5}")
"""
# Non-numeric datatypes/Collections/Iterables
"""
string: Ordered and Immutable collection of characters

Ordered     Mutable     list
Ordered     Immutable   tuple
Unordered   Mutable     set
Unordered   Immutable   frozenset

dictionary: Unordered and Mutable collection of key:value pairs
"""