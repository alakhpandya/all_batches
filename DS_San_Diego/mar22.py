s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9,10}
s3 = {9,10,11,12,13}
s4 = {1,1,2,4,5,6,6,3,8}
s5 = {5,4,3,2,1}

# diff = s1.difference(s2)
# print(diff)       # s1 - s2

# s1.difference_update(s2) # same as s1 = s1.difference(s2)
# print(s1)

# diff1 = s1.difference(s2)    # s1 - s2 = {1,2,3}
# diff2 = s2.difference(s1)    # s2 - s1 = {6,7,8,9,10}

# diff1.union(diff2)      # {1,2,3,6,7,8,9,10}
# symmetric difference of s1 & s2 = (s1 - s2) U (s2 - s1)

# symm_diff = s1.symmetric_difference(s2)
# print(symm_diff)

# Symmetric difference is commutative.
# symmetric difference of s2 & s1 = (s2 - s1) U (s1 - s2)

# s1.symmetric_difference_update(s2)

# s1 is subset of s2
# print(s1.issubset(s4))
# print(s1.issubset(s2))

# print(s4.issuperset(s1))
# print(s2.issuperset(s1))


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9,10}
s3 = {9,10,11,12,13}
s4 = {1,1,2,4,5,6,6,3,8}
s5 = {5,4,3,2,1}

# print(s1.intersection(s3))
# print(s1.isdisjoint(s3))
# print(s1.isdisjoint(s2))

# Nesting of collections - Creating a multi-dimensional matrix
m1 = [1,2,3,4,5]
m2 = [[1,2], [5,6]]
m2 = [
    [1, 2],
    [5, 6]
]

m3 = [
    [1,2,5],
    [-4,3,6],
    [0,8,4]
]
# print(m3)

# print(len(m3))
# print(m3[0])
# print(m3[2])
# print(m3[1][2])
print(m3[0][1])

# lists, tuples, sets

# Can I create sets inside a list? - Yes
# sets in a tuple? - 

# Can I create sets inside sets?
# temp = {
#     {1,2,3},
#     {4,5,6}
# }
# print(temp)

# We can not nest mutable collections in unordered collections and that's why, we can't create sets inside sets.

f1 = frozenset({1,2,3,4})
# print(f1)
# l1 = [4,5,6]
# f2 = frozenset(l1)
f2 = frozenset([4,5,6])
# print(f2)

temp = {f1, f2}
print(temp)

print(f1.intersection(f2))

# Next Class: Dictionaries