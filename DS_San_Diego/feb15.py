# Collections in Python:
"""
ordered     mutable     list        []
ordered     immutable   tuple       ()
unordered   mutable     set         {}
unordered   immutable   frozenset   frozenset()

string: ordered & immutable collection of characters    " "/' '
dictionaries: unordered & mutable collection of key:value pairs     {}
"""

t1 = (10, 15, 10, 29, 13, 14, 10, 15, 15, 29, 15, 10, 13, 45, 13, 14, 29, 45, 14, 45)
# ind: 0   1   2 ...
# -ve:
"""
print(t1)
print(type(t1))

# Access through index:
print(t1[5])
print(t1[-6])

print(t1[5 : -6])
print(t1)

t2 = ("apple", "mango", "banana", "cherries", "kiwi")
print(t2)
print(sorted(t2))

t3 = (12, 15.43, ["Mumbai", 10, -0.75], "San Diego", 12, ("Ahmedabad", -26.4, 0), "USA", 12, 33, "India", 45, 12, 59)
print(t3)
"""
# t4 = (25,)
# print(t4)
# print(type(t4))

# t5 = ("Alakh",)
# print(t5)
# print(type(t5))

# print(len(t4))

"""
t2 = "apple", "mango", "banana", "cherries", "kiwi"
print(t2)

t4 = "Ahmedabad",
print(t4)

t5 = 53.6,
print(t5)
"""

# t1 = (10, 15, 10, 29, 13, 14, 10, 15, 15, 29, 15, 10, 13, 45, 13, 14, 29, 45, 14, 45)
# ind: 0   1   2 ...
# -ve:
# print(t1)

# t1 = (20, 30)
# print(t1)

# Tuple methods:
"""
print(t1.count(14))
# print(t1.count(14, 6))      invalid

# print(t1.index(15))
print(t1.index(15, 2))
print(t1.index(15, 2, 10))
# print(t1.index(15, 2, 6))
"""

"""
s1 = "(10, 15, 10, 29, 13, 14, 10, 15, 15, 29, 15, 10, 13, 45, 13, 14, 29, 45, 14, 45)"
l1 = [10, 15, 10, 29, 13, 14, 10, 15, 15, 29, 15, 10, 13, 45, 13, 14, 29, 45, 14, 45]

import sys

print(sys.getsizeof(t1))
print(sys.getsizeof(s1))
print(sys.getsizeof(l1))
"""

t1 = ("Sanjay", "MTech", 21, "Delhi", "Computer Science", "Swimming")

# name = t1[0]
# edu = t1[1]
# age = t1[2]

# Unpacking/Multiple Assignment of a tuple or a list
"""
name, edu, age, city, course = t1

print(name)
print(edu)
print(age)
"""
# name, edu, *others = t1
# print(name)
# print(edu)
# print(others)

# *others, course, hobby = t1
# print(course)
# print(hobby)
# print(others)

name, *details, course, hobby = t1
# name, *info1, city, *info2 = t1       Invalid

# Next Class: Operators in Python