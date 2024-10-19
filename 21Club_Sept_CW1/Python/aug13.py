s1 = "The largest democracy in the world is INDIA."
"""
print(s1.split())
print(s1.split("e"))
print(s1.split("e", 2))

print(s1.rsplit("e", 2))
print(s1.rsplit("e"))

print(s1.split("in"))
print(s1.partition("in"))
print(s1.partition("e"))
print(s1.rpartition("e"))

s2 = "The largest democracy in the world is INDIA.\nWe are going to celebrate 75th independence day next week.\nTourists will see Indian flags on many homes and shops on that day."
print(s2)
# print(s2.split("\n"))
print(s2.splitlines())
"""
"""
myFriend = "Saurabh,Patel,987654321,saurabh.patel@gmail.com,Mumbai,23/2/1996"
contact = myFriend.split(",")
print(contact)
# contact_string = "_".join(contact)
# contact_string = ",".join(contact)
# contact_string = " ".join(contact)
contact_string = "".join(contact)
print(contact_string)
"""
"""
s2 = "        \t\t         \n\n      Happy Birthday!     \n   \t  \t          \n"
# print(s2)
# s3 = s2.lstrip()
# print("s3 =", s3)
# s3 = s2.rstrip()
# print("s3 =", s3)

# s3 = s2.strip()
# print("s3 =", s3)


s4 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Happy Birthday!$$$$$$$$$$$$$$$$$$$$$$$$$$"
print(s4.strip("$"))
print(s4.lstrip("$"))
print(s4.rstrip("$"))
"""
"""
print(s1.replace("e", "E"))
print(s1.replace("in", "out"))
print(s1.replace("e", "E", 2))
"""
"""
date = input("Date: ")              # 5
month = input("Month: ")            
year = 2022
print(f"Date in dd/mm/yyyy format: {date.zfill(2)}/{month.zfill(2)}/{year}")
"""

# Collections in Python
"""
Properties:             Collecion:
Ordered     Mutable     list
Ordered     Immutable   tuple
Unordered   Mutable     set
Unordered   Immutable   frozenset

special collection:
strings: collections of characters  (Ordered & Immutable)
dictionaries: collections of key:value pairs (Unordered & Mutable)
"""

# list: Ordered and Mutable collections of members
fruits = ["apple", "banana", "kiwi", "orange", "mango"]
# Ordered means:
"""
Index numbers of each element
Accessing through -ve or +ve index numbers
slicing with -ve or +ve index numbers
slicing with -ve or +ve step size
"""