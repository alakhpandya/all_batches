"""
t1 = (54, 22, 44, 37, 96, 22, 83, 22, 65, 100, 22, 301)
# Tuple methods
print(t1.count(22))
print(t1.index(22))
print(t1.index(22, 3, 10))

# Another way to create a tuple:
t2 = 37, 96, 22, 83, 22, 65, 100
print(t2)
print(type(t2))

t3 = "C", "C++", "java", "Python"

# Creating tuple with single element
t4 = "grapes",
t5 = (19,)
print(t4)
print(type(t4))
print(t5)
print(type(t5))
"""
"""
Collections in Python:

Mutable		Ordered		list        []
Immutable	Ordered		tuple       ()
Mutable		Unordered	set         {}
Immutable	Unordered	frozenset

string: collection of characters	:	Immutable	Ordered             " "  or  ' '
dictionary: collection of key:value pairs:	Mutable		Unordered       {}
"""
# Sets: unordered and mutable collections of members in which repeatition is eliminated
"""
s1 = {54, 22, 44, 37, 96, 22, 83, 22, 65, 100, 22, 301}
print(type(s1))
print(s1)
print(len(s1))
"""
"""
Unordered: 
order is not important
no index
no -ve index
no slicing
no accessing through index
"""
# print(s1[3])
# s1[3] = 1000

# s2 = {}
# print(s2)
# print(type(s2))

# creating an empty set
"""
s3 = set()
print(s3)
print(type(s3))
print(len(s3))
"""
# set methods:
"""
s1.add(500)
s1.add(500)
s1.add(500)
s1.add(500)
print(s1)
# s1.clear()
# del s1
s2 = s1.copy()
s3 = s1
s1 = {54, 22, 44, 37, 96, 22, 83, 22, 65, 100, 22, 301}
# s1.discard(301)
# print(s1)
# print(s1.pop())
# print(s1)
# s1.remove(37)
# print(s1)
# s1.discard(2000)
# s1.remove(2000)
s2 = {101, 201, 301, 401, 501}
s1.update(s2)
print(s1)
"""
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
universal = {x for x in range(1,11)}
# print(universal)
uni = s1.union(s2)
print(uni)
print(s1.intersection(s2))
# print(s1.intersection(s3))
print(s2.intersection(s1))
print(s1.difference(s2))    # s1 - s2
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
