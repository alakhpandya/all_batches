# Tuple: ordered & immutable collection of elements
"""
tp1 =   (11, 22, 31, 95, -6)
# index:  0   1   2   3   4
# -ve:   -5  -4  -3  -2  -1
print(tp1[3])
print(tp1[-3])
print(tp1, type(tp1))
# tp1[3] = 96
ourClass = ("Mihir", "Niyati", "Rushil", "Juhi", "Aashna", "Poojan", "Alakh")
# -ve index:  -7        -6        -5       -4       -3        -2       -1
# Slicing is exactly the same as in strings or in lists
print(ourClass[2:6])
print(ourClass[-7:-1])
print(ourClass[::2])
print(ourClass[::-1])

# Defining single element tuples:
# tp2 = ("Mihir")
tp2 = ("Mihir",)
# tp3 = (18)
tp3 = (18,)
print(tp1)
print(tp2, type(tp2))
print(tp3, type(tp3))

# ANother way to define a tuple
ourClass = "Mihir", "Niyati", "Rushil", "Juhi", "Aashna", "Poojan", "Alakh"
print(ourClass)
print(type(ourClass))
print(len(ourClass))
print(min(ourClass))
print(max(ourClass))
print(sorted(ourClass))     # Sorted always returns a LIST

# Methods Tuples
numbers = (33, 22, 11, 33, 45.7, "Mihir", 33, 999)
ct = numbers.count(33)
print(ct)
print(numbers.index(33))
print(numbers.index(33, 1, 5))
print(numbers.index(33, 5))
# print(numbers.index(33, 4, 6))
# print(numbers.index("Alakh"))

# Changing tuples anyhow
temp = list(numbers)
print(temp)
temp.pop()
print(temp)
numbers = tuple(temp)
print(numbers)

tp4 = ourClass + numbers
print(tp4)

# creating a user-defined tuple
list1 = []
size = int(input("How many elements do you want to enter in the tuple?"))
print("Enter elements:")
for x in range(size):
    list1.append(input())
tp5 = tuple(list1)
print("Your tuple:", tp5)

del ourClass
print(ourClass)
"""

# Multiple Assignment/ Unpacking of a tuple
# student_data = ("Mihir", 18, "India")
# name = student_data[0]
# age = student_data[1]
# country = student_data[2]
# print(f"Name: {name}\nAge: {age}\nCountry: {country}")

# name, age, country = student_data
# print(f"Name: {name}\nAge: {age}\nCountry: {country}")

# name, age = student_data
# name, age, country, gender = student_data

student_data = ("Mihir", 18, "Male", "India", "Sports", "Royal")
name, age, *others = student_data
print(f"Name: {name}\nAge: {age}\nOthers: {others}")

name, *others, university = student_data
print(f"Name: {name}\nUniversity: {university}\nOthers: {others}")

*others, country, hobby, university = student_data
print(f"Country: {country}\nHobby: {hobby}\nUniversity: {university}\nOthers: {others}")

# name, *others, country, *others2 = student_data       not allowed

# while loop & for loop in tuple are exactly the same as in list