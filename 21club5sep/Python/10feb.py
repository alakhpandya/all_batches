# Difference between Methods & Functions
s1 = "Today is THURSDAY."
# diff 1: how we write them
# len(s1)
# s1.capitalize()
# print(s1)
# print(type(s1))
# l1 = [11,22,33,44,55]
# diff 2: they are applied to
# functions: all the possible data types
# methods: only on a specific data type
# s1.index()
# l1.index()
# len(s1)
# len(l1)

# Magical Methods/ Dunder Methods
"""
s2 = "Hello"
s3 = "Python"
# print(s2 + s3)
# print(s2.__add__(s3))
a = 5
b = 15
# print(a + b)
# print(a.__add__(b))
"""
# Case - related methods
s2 = s1.capitalize()
print(s1)         # strings are immutable

print(s2)
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())

s3 = "What is ß"
print(s3.lower())
print(s3.casefold())

# Next class: .center()