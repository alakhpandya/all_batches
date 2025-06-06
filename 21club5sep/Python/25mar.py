# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# s3 = {5,6,7,8}
# universal = {x for x in range(1,11)}
# s1.intersection_update(s2)
# s1.difference_update(s2)
# s1.symmetric_difference_update(s2)
# s1.union_update(s2) is not there because s1.update(s2) does the same
# print(s1)
# print(s1.issubset(s2))
# print(s1.issubset(universal))
# print(universal.issuperset(s1))
# print(s1.intersection(s3))
# print(s1.isdisjoint(s3))

# Classwork:
"""
1. Create a set of 6 fruits and print names of all of them by iterating through the set using while/for loop.
2. Write a Python code to create a user defined set.
"""

# HW:
"""
Try to nest collections of Python in one another and derive conclusion based on your observation. Prepare a formal paper of your research.
"""
# frozenset: immutable version of set.
"""
s1 = {1,2,3,4}
fs1 = frozenset(s1)
fs2 = frozenset({3,4,5,6})
fs3 = frozenset([5,6,7,8])
fs4 = frozenset((7,8,9,10))
l5 = [x for x in range(1,11)]
fs5 = frozenset(l5)
print(fs1)
print(fs2)
print(fs3)
print(fs4)
print(fs5)
"""
# Dictionary: Unordered and Mutable collection of key:value pairs
d1 = {"Physics":83, "Maths":88, "Python":99}
# Can't access through index numbers
# Accessing through key
print(d1["Maths"])
d1["Physics"] = 85
print(d1)
# Next Class: Why need of frozensets?, more about dictionaries
