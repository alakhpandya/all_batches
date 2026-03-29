# Mutable & Ordered: list 
# Mutable & Unordered: set, dictionary
# Immutable & Ordered: string, tuple 
# Immutable & Unordered: frozenset
"""
s1 = "I am A STRING."
s1 = s1.lower()
print(s1)
"""
"""
l1 = [1,2,3,4]
print(l1)
print(type(l1))

l2 = [1, 2, "A'bad", "Delhi", 10.4]
print(l2)
print(type(l2))

l1.append(100)
# print(l1.append(100))

l1.clear()
print(l1)

# del l1
# print(l1)
"""
l2 = [21, 44, 90, -32, -5, 1, 0, 23, -18]
# ind: 0   1   2    3   4  5  6   7    8
# -ve:-9  -8  -7   -6  -5 -4 -3  -2   -1

# Accessing through index
"""
print(l2[2])
print(l2[-4])

# Slicing
# print(l2[1 : 5])
# print(l2)

s2 = "Dr.Jay Shah, MD"
print(s2[3 : -4])
s3 = "Dr.Mala Ruparel, MD"
print(s3[3 : -4])

# print(l2[1 : 15])
print(l2[3:])
# print(l2[15])
# print(l2[ : 5])
"""
# print(l2)
# print(l2[1 : 8 : 2])
# print(l2[1 : 8 : 3])
# print(l2[1 : 8 : 300])

# print(l2[1 : 7 : 1])
# print(l2[7 : 1 : -1])
# print(l2[7 : 1 : -2])
# print(l2[::-1])

# Ask length of the list (n) from the user, then run a loop 'n' times to take 'n' inputs from the user & create a list that contains those inputs. 
# Sample Execution:
"""
length of the list = 5
Enter 5 members of the list:
23
Gandhinagar
14.7
-39.5
-0.07
Your list is: ["23", "Gandhinagar", "14.7", "-39.5", "-0.07"]
"""
"""
n = int(input("length of the list = "))
print(f"Enter {n} members of the list:")
my_list = []
while n > 0:    # n = 5, 4, 3, 2, 1
    # print("Hi")
    tmp = input()
    my_list.append(tmp)
    n = n-1
print("Your list is:", my_list)
"""

"""
your_list = ["apple", "banana", "mango", "orange", "grapes", "kiwi", "guava"]
n = len(your_list)
i = 0
# print(n)
while i < n:    # i = 0, 1, 2, 3, 4, 5, 6, 7
    # print(your_list[i])
    print(i)
    i += 1
print("Thanks for using our program!")
"""

# For loop in Python:
"""
your_list = ["apple", "banana", "mango", "orange", "grapes", "kiwi", "guava"]
for i in your_list:     # i = "apple","banana","mango","orange","grapes","kiwi","guava"
    if i == "orange":
        # break
        # continue
        pass
    print(i)
print("End of the code")
"""
"""
fruits = ["apple", "banana", "mango", "orange", "grapes", "kiwi", "guava"]
for fruit in fruits:     # i = "apple","banana","mango","orange","grapes","kiwi","guava"
    if fruit == "orange":
        # break
        # continue
        pass
    print(fruit)
print("End of the code")
"""
# Make a list of n cities where n & the names of the cities should be provided by the user. Also ask name of a city and print all the cities other than that city.
"""
n = int(input("Enter no. of cities: "))
print(f"Enter {n} cities:")
cities = []
while n > 0:
    cities.append(input())
    n = n-1
# print("List of cities:", cities)
skip = input("City to be skept: ")
for city in cities:
    if city == skip:
        continue
    print(city)
"""
"""
# x = 57
x = "Data Science"
for i in x:
    print(i)
"""

# for loop of c or javascript
# for (i=0; i<10; i++)
# print(range(5))

# fruits = ["apple", "banana", "mango", "orange", "grapes", "kiwi", "guava"]
# n = len(fruits)
# for i in range(n):
#     print(i)

# for i in range(5, 15):
#     print(i, end=", ")

# for i in range(10, 30, 2):
#     print(i, end=", ")

# for i in range(30, 10, -2):
#     print(i, end=", ")

# for i in range(-10, 20, 2):
#     print(i, end=", ")
"""
fruits = ["apple", "banana", "mango", "orange", "grapes", "kiwi", "guava"]
for i in range(-7, 2, 2):       # i = -7,-5,-3,-1,1
    # print(i, end=",")
    print(fruits[i])
"""

# Take an integer from the user & print if it is even or odd
n = int(input("n = "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Create a user defined list of integers. Create another list that contains "Even" or "Odd" depending on the corresponding elements of the user's list.
# Eample: user defined list: [1, 4, -2, 0]
# Output: ["Odd", "Even", "Even", "Even"]