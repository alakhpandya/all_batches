"""
s1 = "         \t   \n    Hello World!          \t\t         \n     \n    "
# print(s1)
# print(s1.lstrip())
# print(s1.rstrip())
# print(s1.strip())

s2 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$Happy Birthday!$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
# print(s2.lstrip("$"))
# print(s2.rstrip("$"))
# print(s2.strip("$"))

s3 = ":):):):):):):):):):):):):):):):):):)Happy Birthday!:):):):):):):):):):):):):):):):):):):):):):):):):):):):):):)"
print(s3.strip(":)"))

# s4 = "ab"
# print(s4.zfill(5))
print("Enter the following details:")
date = input("Date(dd): ")
month = input("Month(mm): ")
print(f"Date you entered is: {date.zfill(2)}/{month.zfill(2)}/2022")
"""

# Collections in Python:
"""
Ordered     Mutable     list        []
Ordered     Immutable   tuple       ()
Unordered   Mutable     set         {}
Unordered   Immutable   frozenset

strings: Ordered and Immutable collections of characters                " " / ' '
dictionaries: Unordered and Mutable collections of key-value pairs      {}
"""

# list: Ordered and Mutable collection of members
vegetables = ["green chilli", "potato", "tomato", "lady finger", "beat root", "brinjal", "Cucumber"]
print(vegetables)
print(type(vegetables))
"""
name = list("Ritu")
print(name)

numbers = [12, 37, 0 , -4557, -21, 9837295485, 23.56, -37.98]
print(numbers)
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sorted(numbers))      # sorted() always give you a NEW LIST.
print(numbers)
print(sorted(numbers, reverse=True))
"""
"""
print(min(vegetables))
print(max(vegetables))
print(sorted(vegetables))

mix_veg = ["green chilli", "potato", "tomato", "lady finger", "beat root", "brinjal", "Cucumber", 12, 37, 0 , -4557, -21, 9837295485, 23.56, -37.98]

print(mix_veg)
"""

"""
Ordered:
Order is important
+ve Index no of each members
-ve Index no of each members
Slicing is possible with +ve/-ve index numbers.


Slicing is exactly the same as in strings
"""
numbers = [12, 37, 0 , -4557, -21, 9837295485, 23.56, -37.98]
numbers[3: 10]
numbers[2: -2]
numbers[1 : 10 : 2]
numbers[10 : 1 : -2]