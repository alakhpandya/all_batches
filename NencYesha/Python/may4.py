s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
s4 = {3,2,4,6,7,8}
# list comprehension
"""
list1 = []
for x in range(10):
    list1.append(x)

list1 = [x for x in range(1, 11)]
print(list1)
"""
u = {x for x in range(1, 11)}
"""
uni = s1.union(s2)
print(uni)
print(s2.union(s1))
s1.update(s2)       # instead of s1.union_update(s2)
"""
"""
print(s1.intersection(s2))
print(s2.intersection(s1))
s2.intersection_update(s1)   # same as: s2 = s2.intersection(s1)

diff1 = s1.difference(s2)    # s1 - s2
diff2 = s2.difference(s1)    # s2 - s1
s1.difference_update(s2)     # same as: s1 = s1.difference(s2)

print(diff1.union(diff2))
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
# s1 = s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(s1)
"""
# print(s1.issubset(s2))
# print(s2.issubset(u))
# print(u.issuperset(s1))

# print(s1.intersection(s3))
# print(s1.isdisjoint(s2))
# print(s1.isdisjoint(s3))

# Dictionaries: Unordered & Mutable collections of key : value pairs
d1 = {1 : "Nancy", 2 : "Yesha", 3 : "Shrina", 4 : "Preyasi"}
print(d1[2])
result = {
    "Math 140" : 3.9,
    "CMPSC 121" : 2.8,
    "ENGL 15" : 3,
    "PHYS 211" : 3.8
}
print(result["CMPSC 121"])
print(result)

d2 = {
    ("Nancy", "Yesha") : "EY31A",
    ("Alakh", "Hetal", "Dhyani") : "EY54B"
}
print(d2)

# Keys must be immutable

# d3 = {
#     ["Nancy", "Yesha"] : "EY31A",
#     ["Alakh", "Hetal", "Dhyani"] : "EY54B"
# }


d4 = {
    {"Nancy", "Yesha"} : "EY31A",
    {"Alakh", "Hetal", "Dhyani"} : "EY54B"
}

# frozenset: immutable version of sets
fz1 = frozenset({1,2,3,4})
# As frozensets are immutable, we can use them as keys of a dictionary.