# Dictionaries: Unordered & mutable collection of key:value pairs
"""
s1 = {1,2,3,4}
d1 = {1:"Mihir", 2:"Alakh", 3:"Krishna", 4:"Madhusudan Sir"} 
print(d1)
print(type(d1))
# Accessing through keys:
print(d1[3])
d2 = {
    "Mihir":"Chinese", 
    "Dhiraj":("Mango juice", "Roti", "Buttermilk"), 
    "Krishna":["Soup", "Main Course", "ice cream", "Thumsup"], 
    "Alakh":{"Soup", "Main Course", "ice cream"}, 
    "Rahul":{"BF":"Maggie", "Lunch":"Punjabi", "Dinner":"Gujarati"}, 
    "Tejas":13
}
# We can take any data type as values in dictionaries
print(d2)
print()
d3 = {
    1:"Mihir",
    "Programming Language" : "Python",
    ("age", "gender") : (19, "Male"),
    # ["Country", "State", "City"] : ["India", "Gujarat", "Ahmedabad"]
    # {"Country", "State", "City"} : {"India", "Gujarat", "Ahmedabad"}
    # {1:2, 3:4} : "Student"
    frozenset({"Country", "State", "City"}) : {"India", "Gujarat", "Ahmedabad"}
}
print(d3)
# Keys must be immutable & unique
d4 = {
    1:"Dhiraj",
    2:"Alakh",
    3:"Aarti",
    2:"Madhusudan Sir"
}
print(d4)

d2 = {
    "Mihir":"Chinese", 
    "Dhiraj":("Mango juice", "Roti", "Buttermilk"), 
    "Krishna":["Soup", "Main Course", "ice cream", "Thumsup"], 
    "Alakh":{"Soup", "Main Course", "ice cream"}, 
    "Rahul":{"BF":"Maggie", "Lunch":"Punjabi", "Dinner":"Gujarati"}, 
    "Tejas":13
}

print(d2)
choice = input("Whose meal do you want to see?")
if choice == "Dhiraj" or choice == "Krishna" or choice == "Alakh":
    i = 1
    print("Sr.No.\tItem Name")
    for x in d2[choice]:
        print(f"{i}.\t{x}")
        i += 1

elif choice == "Rahul":
    choice2 = input("Which meal do you want to see? BF/Lunch/Dinner?")
    print(d2[choice][choice2])

else:
    print(d2[choice])
"""
"""
d2 = {
    "Mihir":"Chinese", 
    "Dhiraj":("Mango juice", "Roti", "Buttermilk"), 
    "Krishna":["Soup", "Main Course", "ice cream", "Thumsup"], 
    "Alakh":{"Soup", "Main Course", "ice cream"}, 
    "Rahul":{"BF":"Maggie", "Lunch":"Punjabi", "Dinner":"Gujarati"}, 
    "Tejas":13
}
d2["Alakh"] = "Panipuri"    # To change existing key's value
d2["Madhusudan Sir"] = "Paubhaji"   # To add a key value pair
print(d2)
del d2["Alakh"]
print(d2)
d3 = dict(Name = "Mihir", Age = 19, Gender = "Male")
print()
print(d3)
d4 = d2
del d2
# print(d2)
print(d4)
"""
# for loop in dictionaries
"""
d2 = {
    "Mihir":"Chinese", 
    "Dhiraj":("Mango juice", "Roti", "Buttermilk"), 
    "Krishna":["Soup", "Main Course", "ice cream", "Thumsup"], 
    "Alakh":{"Soup", "Main Course", "ice cream"}, 
    "Rahul":{"BF":"Maggie", "Lunch":"Punjabi", "Dinner":"Gujarati"}, 
    "Tejas":13
}
print("{")
for x, y in d2.items():            # it will take only keys
    print(f"{x} : {y},")
print("}")
"""
myList = [("a", 1, "A"), ("b", 2, "B"), ("c", 3, "C"), ("d", 4, "D")]
for x, y, z in myList:
    print(z)