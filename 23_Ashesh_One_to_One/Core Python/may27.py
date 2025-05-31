# Sets: Unordered & Mutable collection of members in which repeatition is eliminated
# s1 = {12, 34, 11, 66, 94}
# Unordered means:
"""
No +ve/-ve indices
No accessing through index
No slicing
"""
"""
print(len(s1))
print(s1)
print(type(s1))
print(sorted(s1))
"""
# s1[2] = 1000
# Creating an empty set
"""
s2 = {}
print(s2)
print(type(s2))

s3 = set()
print(s3)
print(type(s3))
print(len(s3))
"""
# set methods:
"""
s1 = {12, 34, 11, 66, 94}
s1.add(57)
s1.add(58)
s1.add(59)
s1.add(59)
s1.add(59)
print(s1)

s1.clear()
print(s1)
del s1

s2 = s1.copy()
s3 = s1
s1.discard(66)
print(s1)
s1.remove(94)
print(s1)
s1.discard(600)
# s1.remove(900)
print(s1.pop())
print(s1)

s4 = {100, 200, 300, 66, 94, 34}
s1.update(s4)
print(s1)
"""
# set operation methods
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s3 = {7,8,9,10,11}
# universal = set()
# for i in range(1, 16):
#     universal.add(i)
# universal = {i for i in range(1, 16)}

# s4 = s1.union(s2)
# print(s4)
# print(s1.intersection(s2))
# print(s2.intersection(s1))
# print(s1.difference(s2))        # s1 - s2 = {1,2,3}
# print(s2.difference(s1))        # s2 - s1 = {6,7,8}
# print(s1.symmetric_difference(s2))            # (s1 - s2) U (s2 - s1)
# print(s1.issubset(universal))
# print(universal.issuperset(s1))

# print(s1.isdisjoint(s2))
# print(s1.isdisjoint(s3))


# s1 = s1.intersection(s2)
# s1.intersection_update(s2)
# print(s1)
# s1.difference_update(s2)        # s1 = s1 - s2
# s1.symmetric_difference_update(s2) 
# s1.update(s2)
n = int(input("Enter n: "))     # "1634"
# power = len(str(n))
# digits = []
# for digit in str(n):
#     digits.append(int(digit) ** power)
# digits = [int(digit)**len(str(n)) for digit in str(n)]
print("Armstrong") if sum([int(digit)**len(str(n)) for digit in str(n)]) == n else print("Not Armstrong.")
# Dictionary: Unordered & Mutable collection of kye:value pairs
"""
result = {"Dhiraj":96, "Alakh":92, "Ashesh":97, "Rahul":85}
"""
# Next Class: frozensets