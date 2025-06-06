"""
Collections in Python:

Mutable		Ordered		list        []
Immutable	Ordered		tuple       ()
Mutable		Unordered	set         {}
Immutable	Unordered	frozenset

string: collection of characters	:	Immutable	Ordered             " "  or  ' '
dictionary: collection of key:value pairs:	Mutable		Unordered       {}
"""
# list: Mutable & Ordered collection of members (elements)
l1 =    [54, 90, -43, 22, 11, 6, 305, 4]
# index: 0    1    2   3   4  5    6  7
# -ve  : -8  -7   -6  -5  -4  -3  -2 -1
print(l1)
print(type(l1))
print(l1[2])
l1[1] = 80
print(l1)
# Slicing is exactly the same as in strings
print(l1[1:7:2])
print(l1)           # slicing never changes the original data
print(l1[-1:-8:-2])
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))          # sorted will always give you a NEW LIST
print(l1)

vegetables = ["tomato", "potato", "spinach", "cabbage", "beatroot", "carrot", "peas"]
print(vegetables)
print(len(vegetables))
print(min(vegetables))
print(max(vegetables))
print(sorted(vegetables))

# print(sum(l1)/len(l1))
# print(sum(vegetables))

mix_veg = ["tomato", "2", "potato", "0.5", "spinach", "1", "cabbage", "-0.75", "carrot", "3"]
print(sorted(mix_veg))

# Next class: min, max, sorted on strings, unpacking of collections, list methods