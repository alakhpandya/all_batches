# frozensets: immutable versions of sets
# In Python, we can not create mutable collections inside unordered collections.
# s1 = {1, "string", (1, 2), [3,4]}
# print(s1)
"""
s2 = {
    {1,2,3},
    {3,4,5}
}
"""
"""
l1 = [1,2,3]
fs1 = frozenset(l1)
fs2 = frozenset((3,4,5,4,5,4))
fs3 = frozenset({5,6,7})
# fs4 = frozenset(7,8,9)
print(fs1)
print(fs2)
print(fs3)
"""
# Dictionary: Unordered and Mutable collection of key:value pairs
"""
result = {"Nisha":86, "Gopi":94, "Muskan":92, "Mihir":88}
r = {"Mihir":88, "Nisha":86, "Muskan":92, "Gopi":94}
print(result)
print(r)
print(result == r)
# print(r[0])
print(result["Muskan"])
result["Muskan"] = 96
print(result)

result["Mohan"] = 82
print(result)
"""
# Keys of dictionaries must be unique and immutable.
# r1 = {1:"Mohan", "Sumit":"Python", ("Neha", "Jignasa"):"AI", ["Neha", "Jignasa"]:"DS"}
# print(r1)
from sys import getsizeof


r = {"Mihir":88, "Nisha":86, "Muskan":92, "Gopi":94, "Nisha":97}
print(r)

# We can put any collection or numbers as values
"""
r.clear()
print(r)
r1 = r.copy()
r2 = r
acheivers = ["Ashesh", "John", "Mathew", "Michelle", "Jenifer"]
# reward = {}
# for person in acheivers:
#     reward[person] = 1000
reward = dict.fromkeys(acheivers, 1000)
print(reward)

print(r.get("Gopi", False))
print(r.get("Alakh", "Sorry, this value does not exist..."))
print(r.get("Alakh", False))
print(r.get("Alakh", [1,2,3,4]))
# print(r["Alakh"])

l1 = r.keys()
l2 = list(r.keys())
# for key in l1:
#     print(key)
print(getsizeof(l1))
print(getsizeof(l2))

print(r.values())

print(r.items())
"""
# for student in r:       # same as writing: for student in r.keys():
#     print(student)

# for marks in r.values():
#     print(marks)

# for student, marks in r.items():
#     print(f"{student} got {marks} marks.")

# l1 = ["a", "b", "c"]
# l2 = [1, 2, 3]
# print(list(zip(l1, l2)))
# for student, marks in zip(l1, l2):
#     print(student, marks)

# Next class methods starting from r.pop()