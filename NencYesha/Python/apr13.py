# Unpacking of a collection/Multiple Assignment
"""
# a = 10
# b = 20
# a, b = 10, 20
print("Enter two numbers:")
a = float(input())
b = float(input())
print("a =", a)
print("b =", b)
a, b = b, a
print("a =", a)
print("b =", b)
"""

student_data = ("Nency", 17, "Female")
"""
name = student_data[0]
age = student_data[1]
gender = student_data[2]
"""
# name, age, gender = student_data
# print("Name: ", name)
# print("Age: ", age)
# print("Gedner: ", gender)

student_data = ("Aanya", 16, "Female", "India", "Swimming", "Student")
# name, age, gender, country, hobby = student_data

# name, age, gender, *other_details = student_data
# print(name)
# print(age)
# print(gender)
# print(other_details)

# *extraInfo, hobby, profession = student_data
# print("Hobby:", hobby)
# print("Profession:", profession)
# print("Extra info:", extraInfo)

# name, age, *others, profession = student_data
# print("Name: ", name)
# print("Age: ", age)
# print("Profession: ", profession)
# print("Other Details: ", others)

"""
name, *info, profession = student_data
print("Name:", name)
print("Profession:", profession)
print("Extra info:", info)
"""

# sets: Unordered & Mutable collections of members in which repeatition is eliminated
"""
s1 = {12, 15, 7, 92, -34, 8.6, -43.1, 0, 15, 15, 12, 12}
print(s1)
print(len(s1))  # len = 8
"""
"""
Unordered means:
No +ve/-ve index numbers
No accessing through index like- print(s1[3]), s1[3] = 1500
No slicing like- s1[2 : 9]

print(s1.add(1500))
print(s1)

# s2 = (11,12,13,14,15) # len = 5
s2 = (11,12,13,14,15) # len = 5
# s1.add(s2)
# print(len(s1))
# print(s1)
"""
# s2 = (11,12,13,14,15) # len = 5
# s1.update(s2)
# print(s1)
# print(len(s1))
"""
# s2 = {}
s2 = set()
print(s2)
# print(type(s1))
print(type(s2))
print(len(s2))
"""
# t1 = (1,2,3,4,5)
# s2 = set(t1)
# l1 = list(t1)

# result = { "Maths" : 90, "Physics" : 92, "English" : 88 } 

# s1.clear()
# print(s1)

# s2 = s1.copy()
# print(s2)

s1 = {12, 15, 7, 92, -34, 8.6, -43.1, 0, 15, 15, 12, 12}

# s1.discard(8.6)
# s1.remove(8.6)
# s1.discard(9.6)
# s1.remove(9.6)
# x = s1.pop()
# print("Removed element:", x)

print(s1)

# Next Class: mathematical methods of sets, dictionaries

