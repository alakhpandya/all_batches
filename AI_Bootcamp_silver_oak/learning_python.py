# Python Basics

# print("Hello\n")
# print('Dhruvi')
"""
a = 15
print(a)
"""
'''
a = 15
# 15 = a
b = 12.5
print("b =", b)

print(a > b)
print(a == b)
'''
'''
myList = [1,2,3,4,5]
yourList = ["Apple", 2, "Mango", 3, "Banana", 1, "Kiwi", "Grapes", 1.5]
print(yourList)
myFavouriteFruit = yourList[0]
myLuckyNumber = yourList[5]
print(myFavouriteFruit)
print(myLuckyNumber)
'''
'''
a = int(input("Enter a: "))
b = float(input("Enter b: "))
print(a + b)
'''
"""
students = []
a = input("Student-1: ")
b = input("Student-2: ")
c = input("Student-3: ")

students.append(a)
students.append(b)
students.append(c)

print(students)
"""
'''
n = int(input("No of students: "))
i = 0
while i < n:
    i += 1
    print("Hello Ritika!")
    print("How are you?")
print("Are you enjoying the boot camp?")
'''
'''
students = []
i = 1
while i <= 5:
    # print("Student -", i, "name: ")
    s = input(f"Student-{i} name: ")
    students.append(s)
    i += 1

print(students)
'''
# if-else
'''
a = int(input("a: "))
b = int(input("b: "))
if a > b:
    print("a is bigger")
else:
    print("b is bigger")
'''

# infinite while loop
"""
numbers = []
while True:
    p = int(input("Enter next number: "))
    numbers.append(p)
    done = input("Are you done? Y/N: ")
    if done == "Y":
        break

print(numbers)
"""

# Nested lists:
'''
matrix = [
    [12, 33, 55],
    [44, 0, -12],
    [22, 23, 77]
]

# print(matrix)
print(matrix[1][2])
'''

# Sets in Python
# s1 = {12, 15, 33, -9, 0, 14.4, 33, 33, 33, 33, 33}
# print(s1)

# Dictionaries
'''
result = {"C" : 90, "C++": 95, "Python" : 100}
print(result["Python"])
result["Java"] = 85
# print(result)
result["C"] = 92
print(result)
'''
'''
result = {}
emptySet = set()
'''

# for loop
# fruits = ["Apple", "Mango", "Banana", "Kiwi", "Grapes"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# int i;
# for(i = 0; i < 5; i++){   // i = 0, 1, 2, 3, 4
#     printf("%s", fruits[i]);
# }
# printf("%d", i);

"""
for fruit in fruits:    # fruit = "Apple", "Mango", "Banana", "Kiwi", "Grapes"
    print(fruit)
"""

# range(5) = 0, 1, 2, 3, 4
# range(10)

# for i in range(5):  # i = 0,1,2,3,4
#     print(fruits[i])


# Functions
'''
def helloDevgarh():
    print("Uncover Devgarh's best with our Travel Guide for 2023. Expert tips & must see recommendations.It is still owned by the descendants of the Royal line of Rawats, the Rawat and Rani Saheb of Devgarh, basically you are their guests. Station, Train Frequency, Distance. (MJ)MARWAR JN, 170, 37.06 Kms. (SOD)SOJAT ROAD, 40, 40.59 Kms. (JAL)JAWALI, 14, 51.7 Kms. (SOS)SOMESAR, 28, 51.82 Kms.")

# helloDevgarh()

def sqrt(n):
    print("Sqrt =", n ** 0.5)

# sqrt(300)

def avg(a, b):
    print("avg =", (a + b)/2)
    return (a + b)/2

print(avg(5, 10) + avg(15, 20))
'''

'''
def avg(a, b):
    print("avg =", (a + b)/2)
    return (a + b)/2

a = int(input("Enter two integers:\n")) # 5
b = int(input())    # 6
avg(a, b)
'''

# OOP

class Car:
    seats = 5
    def __init__(self, name, fuel, price):
        self.name = name
        self.fuel = fuel
        self.price = price

    # method
    def printInfo(self):
        print("Name: ", self.name)
        print("Fuel: ", self.fuel)
        print("Price: ", self.price)
        print("Seats: ", self.seats)
"""
c1 = Car()
c1.name = "Thar"
c1.fuel = "Diesel"
c1.price = 2000000
c1.printInfo()

c2 = Car()
c2.name = "Alto"
c2.fuel = "CNG"
c2.price = 300000
# print(c1.seats)
# print(c2.seats)

c2.printInfo()
"""
c1 = Car("Thar", "Diesel", "2000000")
c2 = Car("Alto", )

# Modules/Libraries: Pygame