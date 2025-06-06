# This class: min, max, sorted on strings, unpacking of collections, list methods
"""
string1 = "Today we started 20 minutes late."
print(min(string1))
print(max(string1))
print(sorted(string1))      #  sorted will always give you a NEW LIST
"""
# Unpacking of a Collection/ Multiple Assignment
# student_data = ["Siddhant", 24, "Male"]
# name = student_data[0]
# age = student_data[1]
# gender = student_data[2]
# print(f"Name: {name}\nAge: {age}\nGender: {gender}")
"""
x, y = 20, 40
x, y = y, x
print(f"x = {x}\ty = {y}")
"""
"""
# name, age, gender = student_data
# print(f"Name: {name}\nAge: {age}\nGender: {gender}")

# Errors in unpacking:
# name, age, gender, hobby = student_data
student_data = ["Siddhant", 24, "Male", "Guitar", "India", "Software Engineer"]
# name, age = student_data
# name, age, *others = student_data
# print(f"Name: {name}\nAge: {age}\nOther Details: {others}")
# *other_details, country, profession = student_data
# print(f"Country: {country}\nProfession: {profession}\nOther Details: {other_details}")
# name, *info, profession = student_data
# print(f"Name: {name}\nProfession: {profession}\nOther Details: {info}")
# name, *info, hobby, *others, profession = student_data
name = student_data[0]
hobby = student_data[3]
profession = student_data[-1]
print(f"Name: {name}\nProfession: {profession}\nHobby: {hobby}")
"""
l1 = [54, 22, 44, 37, 96, 22, 83, 22, 65, 100, 22, 301]
# print(l1.append(9000))
l1.append(9000)
print(l1)
# Next Class: Methods starting with 'c'