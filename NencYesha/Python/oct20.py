"""
s1 = "As Diwali is coming everyone in on holiday-mode from this week itself!"
# print(s1.partition("everyone"))
print(s1.partition("in"))
print(s1.rpartition("in"))
myList = s1.split()
print(myList)

# join
s2 = "_"
print(s2.join(myList))
print(" ".join(myList))
"""
# Lists: Ordered & Mutable collections of members
vegetables = ["potato", "cabbage", "tomato", "apple", "carrot", "Orange", "ladyfingure", "broccoli", "cilantro"]
print(vegetables)
"""
numbers = [23, 47, 259, 7, 13, 79434488992114578964312456710, -34, 23.6, -33.8, 0, 47]
print(numbers)
print(len(vegetables))
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))      # Sorted always returns NEW LIST
print(numbers)
print(sorted(numbers, reverse=True))
"""
# print(max(vegetables))
# print(min(vegetables))
# print(sorted(vegetables))

# s1 = "NencYesha"
# print(max(s1))
# print(sorted(s1))

n = [23, 47, 259, 47, 13, 79, 47, -34, 23.6, -33.8, 0, 47, "tomato", "apple", "carrot", "Orange"]
# print(n[3])
# print(n[2 : 9])
# print(n[9 : 2 : -1])

# list methods
n.append(1000)
# n.clear()
# del n
# print(n)

m = n.copy()
# print(m)
print(n.count(47))
l = [2000, 3000, 4000]
# n.append(l)
n.extend(l)
print(len(n))
print(n)

# Next Class: .index() method