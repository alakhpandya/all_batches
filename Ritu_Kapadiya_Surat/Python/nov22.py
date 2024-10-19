"""
t1 = (12, 43, -55.4, -60, 12, 69, 108, 12, 74, 984, 12)
print(t1.count(12))
# print(t1.count(12, 3))    invalid
print(t1.index(-60))
print(t1.index(12, 5))
print(t1.index(12, 5, 7))
"""
# sets: Unordered & Mutable collection of members in which, repeatition is eliminated.

# s1 = {13, -23, 76, 100, 200, 100, 100, 100}
"""
print(s1)
print(type(s1))

s1.add(12)
s1.add(12)
s1.add(12)
s1.add(12)
print(s1)

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1, reverse=True))
"""

"""
No index
No slicing
"""
# s1[3] = 1000

# creating an empty set
"""
s2 = {}
s2 = set()
print(s2)
print(type(s2))
print(len(s2))

t1 = (12, 43, -55.4, -60, 12, 69, 108, 12, 74, 984, 12)
s3 = set(t1)
print(s3)

s4 = set("alakh")
print(s4)
"""

# s1.clear()
# print(s1)
# del s1

# s2 = s1.copy()
# s3 = s1

# s1.discard(-23)
# s1.remove(-23)
# s1.remove(1000)

# print(s1)
# print(s1.pop())
# print(s1)

# s2 = {20, 30, 40, 50}
# s1.update(s2)
# print(s1)

s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
universal = {1,2,3,4,5,6,7,8,9,10}


# uni = s1.union(s2)
# uni = s2.union(s1)
# print(uni)

# inter = s1.intersection(s2)
# inter = s2.intersection(s1)
# print(inter)

# diff = s1 - s2
# diff1 = s1.difference(s2)
# diff2 = s2.difference(s1)
# print(diff1)
# print(diff2)
# print(diff1.union(diff2))       # symmetric difference of s1 & s2

# sym_diff = s1.symmetric_difference(s2)
# sym_diff = s2.symmetric_difference(s1)
# print(sym_diff)


# s1.intersection_update(s2)

# s1.difference_update(s2)

# s1.symmetric_difference_update(s2)

print(s1)

# There is no such method as s1.union_update(s2) because .update() doed the same job.

# Next class: remaining set methods & list comprehesion, start new collection
"""
HW:
try to nest every collection in one another.
"""