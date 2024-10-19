# List : ordered & mutable collection of members/elements
"""
veg = ["potatoes", "carrots", "cabbage", "beatroot", "reddish", "tomato"]
# index:    0          1           2         3          4           5
# -ve in:   -6         -5         -4        -3          -2          -1
print(len(veg))
print(veg[3])
print(veg)
print(type(veg))
print(veg[-4])
print(veg[1:5])     # slicing never changes the original data
print(veg)
print(veg[::2])
print(veg[::-2])
print(veg[-6:-2])
print(veg[-2:-6:-1])
var = veg[4]
print(var.upper())

numbers = [33,13,22.5,889,-23,0,13]
print(numbers)
print(type(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))      # sorted always returns a new list
print(numbers)

print(max(veg))
print(min(veg))
print(sorted(veg))

num = 55
str1 = str(num)
list1 = list("Mihir")
print(list1)
print(max("mihir"))
print(min("mihir"))
print(sorted("mihir"))

mixVeg = ["carrots", "2", "potatoes", "1", "cabbages", "-2", "onion", "1.6"]
print(min(mixVeg))
print(max(mixVeg))
print(sorted(mixVeg))
"""
# List Methods
numbers = [33, 13, 22.5, 889, -23, 0, 13]
print(numbers.append(9))
print(numbers)              # Lists are mutable
print(numbers.append(9))
print(numbers.append(9))
print(numbers.append(9))
print(numbers)
# numbers.clear()
# print(numbers)
# del numbers
# print(numbers)

# numbers2 = numbers.copy()
# print(numbers2)
# numbers.clear()
# print(numbers2)

"""
numbers2 = numbers
print(numbers2)
numbers.clear()
print(numbers2)
"""
list2 = [11,22,33,44,55]
print(numbers.count(13))
numbers.extend(list2)
print(numbers)

print(numbers.index(22))
print(numbers.index(13))    # index of first occurance
print(numbers.index(13, 2, 11)) 
numbers.insert(6, 30)
print(numbers)

print(numbers.pop())
print(numbers)

print(numbers.pop(6))
print(numbers)

numbers.remove(22)
print(numbers)

# numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)