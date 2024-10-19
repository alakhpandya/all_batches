# s1 = {1,2,3}
# s2 = {1,2,3,4,5}
# s3 = {5,6,7}
# print(s1.issubset(s2))
# print(s2.issuperset(s1))
# print(s1.isdisjoint(s3))

# Write a Python program to create a user defined list.
# n = int(input("Enter number of elements: "))
# print("Enter elements:")

# myList = []
# for i in range(n):
#     myList.append(input())

# myList = [input() for i in range(n)]
# print(myList)
"""
n = int(input("Enter number: "))    # 153
power = len(str(n))
digits = [int(digit)**power for digit in str(n)]
print("Armstrong.") if sum(digits) == n else print("Not Armstrong.")
"""

# n = int(input("Enter number: "))    # 153
# print("Armstrong.") if sum([int(digit)**len(str(n)) for digit in str(n)]) == n else print("Not Armstrong.")

# Frozensets: Immutable versions of sets
"""
s1 = {1,2,3}
fz1 = frozenset(s1)
fz2 = frozenset((12,13,2,14,15,15,15))
print(fz1)
print(fz2)

print(fz1.intersection(fz2))
"""

# Dictionaries: Unordered and Mutable collections of key-value pairs
"""
result = {"Physics":88, "Chemistry":94, "Maths":90}
print(len(result))
print(type(result))
print(min(result))
print(max(result))
print(sorted(result))

# print(result[1])
print(result["Maths"])
result["Maths"] = 92

result["Computers"] = 100

print(result)

d1 = {1:"Ritu", 2:"Alakh", 3:"Dhiraj"}
print(d1)

# d2 = {["Physics", "Computers"]: "Ritu", ["Maths", "AI"] : "Alakh"}
"""

party = {
    "tejas": 15,
    "ritu":"Juice",
    "pallavi": ("Salads", "Pizza", "BwI"),
    "kunika": ["Soup", "Main Course", "Icecream"],
    "alakh" : {"Soup", "Main Course", "Icecream"},
    "dhiraj" : frozenset({"Khichdi", "Sabji", "Buttermilk"}),
    "krishna" : {
        "BF":"Maggi", "Lunch":"Punjabi", "Dinner":"Gujarati"
    }
}
# print(party)

result = {"Physics":88, "Chemistry":94, "Maths":90, "Chemistry":66}
result["Computers"] = 100
# key = input("Enter key: ")
# value = input("Enter value: ")
# result[key] = value
print(result)

# Keys of a dictionary must be immutable & unique.

# Methods of dictionaries