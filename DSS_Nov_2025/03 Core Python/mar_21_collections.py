# Mutable & Ordered: list 
# Mutable & Unordered: set, dictionary
# Immutable & Ordered: string, tuple 
# Immutable & Unordered: frozenset
"""
s1 = "I am A STRING."
s1 = s1.lower()
print(s1)
"""
"""
l1 = [1,2,3,4]
print(l1)
print(type(l1))

l2 = [1, 2, "A'bad", "Delhi", 10.4]
print(l2)
print(type(l2))

l1.append(100)
# print(l1.append(100))

l1.clear()
print(l1)

# del l1
# print(l1)
"""
l2 = [21, 44, 90, -32, -5, 1, 0, 23, -18]
# ind: 0   1   2    3   4  5  6   7    8
# -ve:-9  -8  -7   -6  -5 -4 -3  -2   -1

# Accessing through index
"""
print(l2[2])
print(l2[-4])

# Slicing
# print(l2[1 : 5])
# print(l2)

s2 = "Dr.Jay Shah, MD"
print(s2[3 : -4])
s3 = "Dr.Mala Ruparel, MD"
print(s3[3 : -4])

# print(l2[1 : 15])
print(l2[3:])
# print(l2[15])
# print(l2[ : 5])
"""
print(l2)
# print(l2[1 : 8 : 2])
# print(l2[1 : 8 : 3])
print(l2[1 : 8 : 300])