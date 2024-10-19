# Collections in Python:
"""
ordered     mutable     list        []
ordered     immutable   tuple       ()
unordered   mutable     set         {}
unordered   immutable   frozenset   frozenset()

string: ordered & immutable collection of characters    " "/' '
dictionaries: unordered & mutable collection of key:value pairs     {}
"""

d = {"Physics":83, "Maths":88, "Python":99, "Computers":98, "Chemistry":84}

# Updating existing key with new value:
# d["Physics"] = 87

# Adding a new key-value pair
# d["Data Science"] = 94

# Deleting a key-value pair:
# d["Computers"] = ""       Doesn't work
# del d["Computers"]

# Assigning null value to a key:
# d["Computers"] = None

# Deleting the entire dictionary:
# del d
"""
d2 = {
    1 : "Freny",
    (2, 3) : ("Krushy", "Rushabh"),
    # [4, 5] : ("Alakh", "Dhiraj")          Doesn't work
    # {4, 5} : ("Alakh", "Dhiraj")        Doesn't work
    # {4 : "Faculty", 5 : "Director"} : ("Alakh", "Dhiraj")     Doesn't work
    frozenset({4, 5}) : ("Alakh", "Dhiraj")     # worked!
}
print(d2)
"""
# That means, keys of a dictionary must be immutable & unique.
d = {"Physics":83, "Maths":88, "Python":99, "Computers":98, "Chemistry":84, "Maths":92}


# Methods of dictionaries
# d.clear()
print(d)

# d2 = d.copy()

# dict.fromkeys():
"""
owners = ["Krushy", "Rushabh", "Alakh", "Dhiraj"]
deposits = dict.fromkeys(owners, 10000)
# deposits = {"Krushy" : 10000, "Rushabh" : 10000, "Alakh" : 10000, "Dhiraj" : 10000}
print(deposits)
"""

# print(d.get("Chemistry"))
# HW: What's the difference between accessing through key (d["Chemistry"]) or accessing through get() method?

# Next Class: methods starting from d.items()