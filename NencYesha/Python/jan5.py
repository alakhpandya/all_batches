# Collections in Python
"""
Ordered     Mutable     list    []
Ordered     Immutable   tuple   ()
Unordered   Mutable     set     {}
Unordered   Immutable   frozenset

strings: Ordered & Immutable collections of characters              " " or ' '
dictionaries: Unordered & Mutable collections of key : value pairs  {}
"""

# tuple: Ordered & Immutable collection of members
"""
t1 = (23, 56, 90, 23, -12, -48.3, 0, 23, 100, -200, 23, -90)
print(t1[4])
print(t1[-4])
print(t1[2 : 10])
print(len(t1))

t2 = (11, -47, "Nency", "Yesha", "Pen State", 1982)
print(t2)

# Another way to create a tuple
t3 = 23, -12, -48.3, 0, 23, 100, -200, 23
print(t3)

t4 = "Ahmedabad", "New York", "Berlin"
print(t4)

# creating a tuple with single element
t5 = "Surat",
print(t5)
print(type(t5))

t6 = 37,
print(t6)
print(type(t6))

t7 = ("Mumbai",)
print(t7)
print(type(t7))

number = (105,)
print(number)
print(type(number))

# tuples are immutable
myList = [23, -12, -48.3, 0, 23, 100, -200, 23]
myList[2] = -50
print(myList)

# t1[2] = 190       Not allowed
"""
# methods for tuples
"""
t1 = (23, 56, 90, 23, -12, -48.3, 0, 23, 100, -200, 23, -90)

print(t1.count(23))
# print(t1.count(23, 3, 10))        Not Available

print(t1.index(100))
# print(t1.index(-100))
print(t1.index(23))
print(t1.index(23, 5))
print(t1.index(23, 8, 11))
"""

# unpacking of collections
student_data = ("Aanya", 16, "Female")
# name = student_data[0]
# age = student_data[1]
# gender = student_data[2]

name, age, gender = student_data
print(name)
print(age)
print(gender)

# Next Class: more about the unpacking, remaining collections