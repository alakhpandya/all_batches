"""
We cannot nest mutables in unordered collections.

s1 = {
    frozenset({1,2,3}),
    frozenset({3,4,5}),
    56,
    "myString",
    (5,6,7)
}

Find out- Which collections can you use as keys of a dictionary?
"""
# Keys of a dictionary must be immutable and unique.
"""
d1 = {"Physics":83, "Maths":88, "Python":99, "Maths":73}
print(d1)
restaurent = {
    "Priyansh":"Ras-Puri",
    "Dhiraj": ("Khichdi", "Kadi", "Buttermilk"),
    "Tejas": 13,
    "Samir": ["Soup", "Sabji-Roti", "Icecream"],
    "Alakh": {"Soup", "Sabji-Roti", "Icecream"},
    "Rahul": {"BF":"Maggie", "Lunch":"Punjabi", "Dinner":"Gujarati"}
}
print(restaurent)
"""
# Dictionary Methods
d1 = {"Physics":83, "Maths":88, "Python":99, "Computers":98, "Chemistry":84}
# d1.clear()
# del d1
d2 = d1
d3 = d1.copy()
account_holders = ["Viral", "Harshil", "Krisha", "Priyansh", "Het"]
d4 = dict.fromkeys(account_holders, 1000)
print(d4)
"""
HW:
1. Do the above task without using fromkeys() method, account_holders should be user defined.
2. Find the difference between d1.get("Python") and d1["Python"]
"""
print(d1.get("Python"))
print(list(d1.keys()))
print(d1.values())
print(d1.items())
# Next Class: for loop in dictionaries, remaining dictionary methods, practice examples