# d1 = {1:"Mihir", 2:"Alakh", 31:"Krishna", 4:"Madhusudan Sir"}
"""
d1.clear()
print(d1)
d2 = d1.copy()
d3 = d1
del d1
print(d2)
print(d3)
list1 = ["Mihir", "Alakh", "Krishna", "Madhusudan Sir"]
d2 = dict.fromkeys(list1, 10000)
print(d2)

print(d1[31])
print(d1.get(31))

# print(d1[32])
print(d1.get(32))
print(d1.get(3, "Not-found"))

print(list(d1.keys()))
print(list(d1.values()))
print(list(d1.items()))
for x in d1:
    print(x)

print()

for x in d1.values():
    print(x)

print()
for x in d1.items():
    print(x)
"""
# print(d1.pop(1))
# print(d1)

# print(d1.pop(3))              Return
# print(d1.pop(3, "Not-found"))

# print(d1.popitem())
# print(d1)
# d2 = {"PL":"Python", "Course":"Pyramid", "Gift":"Mangoes"}
# d1.update(d2)
# print(d1)
d1 = {"Mihir":"Bhindi ki sabji", "Alakh":"Muthiya", "Dhiraj":"Bajri no rotlo", "Sahil":"khichdi-kadhi"}
person = input("Enter the key you want to add: ")
food = input("Enter the value of that key: ")
# print(d1.setdefault(person, food))
if d1.setdefault(person, food) == food:
    print("key:value pair updated successfully!")
else:
    print("Alert! Key already exist with value:", d1.setdefault(person, food))
    overwrite = input("Want to overwrite existing key? y or n?")
    if overwrite == "y":
        d1[person] = food
        print("key:value pair overwritten successfully!")
    else:
        print("key:value pair updating failed.")
print(d1)

# Practice Example
"""
1. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.

"""