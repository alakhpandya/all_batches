# Collections in Python:
"""
ordered     mutable     list        []
ordered     immutable   tuple       ()
unordered   mutable     set         {}
unordered   immutable   frozenset   frozenset()

string: ordered & immutable collection of characters    " "/' '
dictionaries: unordered & mutable collection of key:value pairs     {}
"""

# Sets in maths: unordered & mutable collections of members in which repeatition is eliminated
# Unordered means (apart of order being not important): No indexing, No accessing through index, No negative indices, No Slicing

s1 = {10, 12, 13, 15}
print(s1)
print(type(s1))
s2 = {"Rushabh", "Krushy", "Alakh"}
# index: 0          1        2
print(s2)
gift = {"Snickers", "Kit kat", "Dairy milk", "Amul", "5 Star"}

print(len(gift))
print(sorted(gift))
gift_list = list(gift)
print(gift_list)
l1 = ["India", "USA", "Australia", "Japan"]
quad = set(l1)
print(quad)
print(tuple(quad))

empty = {}
print(empty)
print(type(empty))

empty2 = set()
print(empty2)
print(type(empty2))
print(len(empty2))

s2 = {13, 14, 15, 16, 17}

print(len(s1.union(s2)))
print(s1.union(s2))

# Normal Methods:
print(s2.add(20))
print(s2)

str1 = "Hello Krushy!"
print(str1.upper())

# s2.clear()
# print(s2)
# del s2

# sorted = "Hi Rushabh!"
# del = "Hi Rushabh!"
# print(sorted)

# Some Keywords: in, is, if, else, elif, for, while, del etc

s3 = s2.copy()  # Deep Copy
s4 = s2         # Shallow Copy

# s2.clear()
del s2
print(s3)
print(s4)