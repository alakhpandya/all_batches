# Dictionaries: Mutable & Unordered collections of key:value pairs
"""
s1 = {1,2,3,4}
d = {1 : "Rushabh", 2 : "Krushy", 3 : "Alakh"}
print(d[2])

capitals = {"Gujarat" : "Gandhinagar", "Maharashtra" : "Mumbai", "Rajasthan" : "Jaipur"}
print(capitals["Maharashtra"])

capitals = {
    "India":"New Delhi",
    "US":"Washington DC"
}
"""
# Classwork-1
restaurent = {
    "Tejas":"Ras-Puri",
    "Dhiraj": ("Khichdi", "Kadi", "Buttermilk"),
    "Rushabh": 13,
    "Krushy": ["Aam Ras", "Sabji-Roti", "Gujarati Dal-Rice", "Icecream"],
    "Alakh": {"Aam Ras", "Sabji-Roti", "Gujarati Dal-Rice", "Icecream", "Icecream"},
    "Rahul": {"BF":"Maggie", "Lunch":"Punjabi", "Dinner":"Gujarati"}
}
"""
sr_no = {
    1 : "Tejas",
    2 : "Alakh"
}

no = int(input("Roll no: "))    # 2
print("no =", no)
person = sr_no[no]
print("person =", person)
print("food =", restaurent[person])
"""
# print(restaurent)
name = input("Person's name: ").capitalize()
# print(restaurent[name])
"""
for Dhiraj:
Khichdi
Kadi
Buttermilk
"""

if name == "Tejas" or name == "Rushabh":
    print(restaurent[name])
else:
    food_items = restaurent[name]
    for item in food_items:
        print(item)