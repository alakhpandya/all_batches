# Set methods
"""
s1 = {11,55,23,67,-98.6,7395,0,22.8}
s1.add(83)
# print(s1)
# s1.clear()
# print(s1)
# del s1
# print(s1)
# s2 = s1.copy()
# s3 = s1
# print(s1)
# # del s1
# s1.clear()
# print(s2)
# print(s3)
print(s1.discard(22.8))
s1.discard(22.8)
print(s1)
print(s1.remove(0))
# s1.remove(0)          raises error
print(s1)
print(s1.pop())
print(s1)
s1.update({1,2,3})
s1.update(["C", "Python"])
s1.update(("Alakh", "Dhiraj"))
s1.update("Mihir")
print(s1)
"""
# set operations
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
s4 = {1,4,5,8,6,3,9,2}
# inter = s1.intersection(s2)   # commutative
# print(inter)
# s1 = s1.intersection(s2)
# s1.intersection_update(s2)
# print(s1)
uni = s1.union(s2)              # commutative
print(uni)
"""
diff1 = s1.difference(s2)
print(diff1)
diff2 = s2.difference(s1)       # non-commutative
print(diff2)
print(diff1.union(diff2))       # symmetric difference
"""
symdiff = s1.symmetric_difference(s2)   # commutative
print(symdiff)

# s1.difference_update(s2)
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)

# s1.update(s2) is same as union_update

print(s1.isdisjoint(s3))
print(s1.issubset(s4))
print(s3.issubset(s4))
print(s4.issuperset(s1))
print(s4.issuperset(s3))
"""
HW:
nest the collection in one another and write conclusion of your experiment
"""
# forzen sets: sets those are immutable are called frozen sets
fs1 = frozenset({1,2,3,4})
print(fs1)
print(type(fs1))