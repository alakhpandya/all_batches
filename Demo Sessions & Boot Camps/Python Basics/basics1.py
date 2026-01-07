'''
print("Hello World!")
# Variables
state = "Gujarat"
print(state)
x = 53
y = 7
print(x + y)
z = 10.5
print(type(x))
print(type(z))
print(type(state))
'''

"""
# Collections
marks = [19 ,17, 20, 12, 15]
# index: 0,   1,  2,  3,  4
print(type(marks))
print(len(marks))
marks.append(18)
print(marks)
# marks.clear()
print(marks)


myTuple = (19 ,17, 20, 12, 15)
# index:    0,  1,  2,  3,  4
print(myTuple)
print(type(myTuple))

# sets
mySet = {19 ,17, 20, 12, 15}
print(mySet)
mySet.clear()
# myTuple.clear()

# Dictionaries
capitals = {
    "Gujarat" : "Gandhinagar",
    "Maharashtra" : "Mumbai",
    "Rajasthan" : "Jaipur"
}
print(len(capitals))
capitals["Madhya Pradesh"] = "Bhopal"
print(capitals)

print(capitals["Maharashtra"])
print(marks[3])

students={
    1 : "Rishabh",
    2 : "Nishith",
    3 : "Neepa",
    4 : "Vishva"
}
print(students[3])
"""

# Conditional statements (if-else)
"""
x = int(input("Enter x:"))
y = int(input("Enter y:"))

# print(type(x))

print(y < x)        # x > y, x <= y, x >= y, x == y, x !=  y

if x > y:
    print("X is bigger than Y")
    print("This is if condition.")
else:
    print("X is smaller than Y")

"""
"""
x = int(input("Enter x:"))
y = int(input("Enter y:"))

if x > y:
    print("X is bigger than Y")
elif x < y:
    print("X is smaller than Y")
else:
    print("Both are equal")

print("Program Ended Successfully!")
"""

"""
x = int(input("Enter x:"))
y = int(input("Enter y:"))

if x >= y:
    print("X is bigger than Y")

elif x <= y:
    print("X is smaller than Y")

elif x < y:
    print("X is strictly less than Y")
# if x == y:
else:
    print("Both are equal")

print("Program Ended Successfully!")

"""

# Loops - while loop
"""
counter = 1
while counter <= 5:
    print("Welcome to Python Tutorial")
    counter = counter + 1

print("Program Ended Successfully!")
"""
"""
marks = [19, 15, 25]
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
"""

fruits = ["Mango", "Apple", "Banana", "Pineapple", "Kiwi", "Strawberries", "Grapes"]
"""
i = 0
while i < len(fruits):      # i = 0,1,2,3,4,5,6
    print(fruits[i])
    i = i + 1
"""
# for loop
"""
for i in fruits:        # i="Mango", "Apple", "Banana", "Pineapple", "Kiwi", "Strawberries", "Grapes"
    # print(fruits[i])
    print(i)
    if len(i) > 6:
        print("Long name")
    else:
        print("Short name")


for fruit in fruits:
    print(fruit)
    if len(fruit) > 6:
        print("Long Name")
    else:
        print("Short Name") 
"""

# range in for loop
# print(range(10))
# for i in range(10):     # i = 0,1,2,3,4,5,6,7,8,9
#     print(i)
"""
for i in range(5, 16):
    print(i)
    
"""
"""
for i in range(1, 11):
    print(i)
    if i > 5:
        pass
print("End of program")
"""
"""
fruits = ["Mango", "Apple", "Banana", "Pineapple", "Kiwi", "Strawberries", "Grapes"]
for fruit in fruits:
    print(fruit)
    if len(fruit) > 6:
        print("Long Name")
        break
    else:
        print("Short Name") 
print("Enjoy having at least one fruit a day!!")
"""
"""
fruits = ["Mango", "Apple", "Banana", "Pineapple", "Kiwi", "Strawberries", "Grapes"]
for fruit in fruits:
    if len(fruit) > 6:
        print("Long Name")
        continue
    else:
        print("Short Name")
    print(fruit) 
print("Enjoy having at least one fruit a day!!")
"""

# functions

def func1(fruit_name, nick_name="My Favourite Fruit"):
    print(f"Hi, {fruit_name} is a long name!")
    print("length of the name =", len(fruit_name))
    print("Nick name of the fruit =", nick_name)

# func1()
"""
fruits = ["Mango", "Apple", "Banana", "Pineapple", "Kiwi", "Strawberries", "Grapes"]
for fruit in fruits:
    if len(fruit) > 6:
        print("Long Name")
        func1(fruit)
        continue
    else:
        print("Short Name")
    print(fruit) 
print("Enjoy having at least one fruit a day!!")
"""

# func1("rose apple")
# func1("lemon", "your favourite fruit")
"""
def func2(a, b):
    s = a + b
    print("sum =", s)
    return s

d = func2(5,7)
c = 8
print(d + c)
"""

"""
def checkPositive(x):
    if x > 0:
        print("Number is positive.")
        return True
    else:
        print("Number is negative.")
        return False


a = int(input("a :"))
b = int(input("b :"))

# print(checkPositive(a))
if checkPositive(a):
    print(a + b)
else:
    print(a - b)
"""

n = int(input("n = "))
"""
for i in range(2, n):
    if n % i == 0:
        print("Composite number")
        break
    print("Prime")
"""

def checkPrime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Composite")
            return False
    print("Prime")
    return True
    

checkPrime(n)