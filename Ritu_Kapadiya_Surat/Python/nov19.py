fruits = ["mango", "banana", "cherry", "peach", "apple"]
# for fruit in fruits:    # i = "mango", "banana", "cherry", "peach", "apple"
#     print(fruit)

# countryList = ["India", "US", "UK", "Germany", "Canada", "Australlia"]
# for country in countryList:
#     if country == "Germany":
#         # pass
#         # continue
#         break
#     print(country)


# for character in "Mango":
#     print(character)

# m1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# m1[1][2]

"""
result = [
    ["Meet", 98, "Maths"],
    ["Kunika", 97, "Computers"],
    ["Pallavi", 88, "Fine Arts"]
]

for w, x, y, z in result:
    print(f"{x} got {y} marks in {z}")
"""
# range(5) = 0,1,2,3,4

# for i in range(5):
# for i in range(5, 15):
# for i in range(5, 30, 2):
#     print(i)

# for-else = break-else
"""
n = int(input("Enter a number: "))
for i in range(2, (n/2)+1):
    if n % i == 0:
        print("Not Prime.")
        break
else:
    print("Prime.")
"""


"""
Loop examples:
1. Write a Python code that takes an integer from user and prints number of digits in that integer.
2. Write down a Python code that creates a user defined list
3. Write a Python code to print each of the elements of a given list in a new line
4. Write a Python program that prints whether the number given is a prime number or not.
5. Write a Python program that prints whether the number given is a perfect number or not.
6. Write a Python program that prints whether the number given is an Armstrong number or not.
7. Write a Python program that prints all the prime numbers between two integers given by user.
8. Write a Python program that prints all the perfect numbers between two integers given by user.
9. Write a Python program that prints all the Armstrong numbers between two integers given by user.
"""

# Remaining collections
"""
Ordered     Mutable     list        []
Ordered     Immutable   tuple       ()
Unordered   Mutable     set         {}
Unordered   Immutable   frozenset

strings: Ordered and Immutable collections of characters                " " / ' '
dictionaries: Unordered and Mutable collections of key-value pairs      {}
"""

# tuples: Ordered and Immutable collection of members
"""
Ordered means:
index numbers of each member
-ve index numbers
can access members through +ve/-ve index number
slicing is possible
"""
"""
t1 = (12, 43, -55.4, -60, 12, 69, 108, 12, 74, 984, 12)
print(t1)
print(type(t1))
f = tuple(fruits)
print(f)
min(t1)
max(t1)
print(sorted(t1))

# t1 = tuple(sorted(t1))
# print(t1)

# creating single element tuples
t2 = (72,)
print(t2)
print(type(t2))

# Another way to create a tuple:
numbers = 12, 43, -55.4, -60, 12, 69, 108, 12, 74, 984, 12
print(numbers)
print(type(numbers))

t4 = 72,


# t3 = ("India")
t3 = "India", 
print(t3)
print(type(t3))


print(t1[2:7])
print(t1[2:10:2])
print(t1[-2:-10:-2])

print(t1[4])
t1[4] = 5000
"""
# Unpacking of a collection/Multiple Assignment

student_data = ("Rahul", 17, "Male", "Guitar", "Programmer", "India")
# name = student_data[0]
# age = student_data[1]
# gender = student_data[2]
# name, age, gender = student_data
# name, age, gender, *others = student_data

# print(f"Name: {name}\nAge: {age}\nGender: {gender}\nOther Details: {others}")

# *info, hobby, profession, country = student_data
# print(f"Hobby: {hobby}\nProfession: {profession}\nCounty: {country}\nOther Details: {info}")

# name, age, *other_details, country = student_data

# name, *details1, hobby, *details2 = student_data

a, b, c = 20, 30, 40

print("a =", a)
print("b =", b)
print("c =", c)

# a, b = b, a
# print("a =", a)
# print("b =", b)

a, b, c = c, a, b
print("a =", a)
print("b =", b)
print("c =", c)

# Next class: tuple methods, sets