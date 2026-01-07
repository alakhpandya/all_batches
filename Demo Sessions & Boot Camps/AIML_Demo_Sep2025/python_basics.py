"""
print("Welcome to the Demo")

# Variables
x = 15
print(x)
print("x =", x)         # printing a variable
"""
x = 15
y = 14.5
# print(y)

# print(type(x))
# print(type(y))
z = "Python"
# print(type(z))
a = "45"
b = int(a)
# print(type(b))

b = "4.5"
c = float(b)
# print(type(c))

# c = 55.7
# d = int(c)
# print(d)
# print(type(d))

# Collections: strings, lists, tuples, sets, dictionaries
"""
a = "Python"
l1 = [12, 1.3, "Mumbai", 23, 11, 10, 32, -11]
# ind: 0,   1,   2
print(l1)

# print(l1[1])
print(l1[1 : 5])

l1.append("A'bad")
print(l1)

# l1.clear()
# print(l1)

print("a :", len(a))
print("l1 :", len(l1))
"""
# tuples - immutable
"""
t1 = (12, 1.3, "Mumbai", 23, 11, 10, 32, -11)
# height = None
# Weight = None
# t1 = (height, Weight)
print(t1[3])
"""

# sets - Unordered, Mutable
"""
s1 = {12, 34, -23, 0, -23}
# No indexing, Repeatition is eliminated
s1.add("AI")
print(s1)

# Dictionaries
# d1 = {"Gujarat" : "Gandhinagar", "Rajasthan" : "Jaipur"}
d1 = {
    "Gujarat" : "Gandhinagar",
    "Rajasthan" : "Jaipur"
}
print(d1["Gujarat"])
d1["Maharashtra"] = "Mumbai"
print(d1)
print(len(d1))
"""
# numpy, pandas, matplotlib, skelearn
"""
a = 9894272897349857243098513024789274289720490984325709438750923470952470579823409570298475029348750923487590324750982
print(type(a))
"""
# Vector search

# Conditional Statements: if-else
"""
if (condition) {


}
"""

# a = int(input("a = "))
# b = int(input("b = "))
# print("a =", a)
# print("a + b =", a + b)

# conditions: a < b, a <= b, a > b, a >= b, a == b, a != b
# print(a < b)
"""
if a <= b:
    print("a is smaller than b")
    print("have a nice day!")
print("keep going..")
if a == b:
    print("Both are equal")
if a >= b:
    print("a is bigger than b")
else:
    print("a is bigger than b")
print("Program ended...")
"""

# Loops: while, for
"""
l1 = [12, 1.3, "Mumbai", 23, 11, 10, 32, -11]
i = 0
while i < len(l1):      # i = 0,1,2,3,4,5,6,7,8
    print(l1[i])
    i += 1          # same as: i = i + 1
"""
# infinite loops:
"""
l1 = [12, 1.3, "Mumbai", 23, 11, 10, 32, -11]
i = 0
while True:
    print(l1[i])
    if l1[i] == "Mumbai":
        break
    i = i + 1
"""
"""
l1 = [12, 1.3, "Mumbai", 23, 11, 10, 32, -11]

for i in l1:           # i = 12, 1.3, "Mumbai", 23, 11, 10, 32, -11
    if i == 23:
        # pass
        continue
    print(i)
"""
"""
state = ["Gujarat", "Rajasthan", "Maharashtra"]
capitals = ["Gandhinagar", "Jaipur", "Mumbai"]
# print(zip(state, capitals))

# for i, j in zip(state, capitals):
    # print(i)
    # print(j)
    # print(f"{j} is capital of {i}")     # f-string

# for state, city in zip(state, capitals):
#     print(f"{city} is the capital of {state}")


# Functions

def func1():
    print("Hi, I am func-1!")

# print(func1)
# func1()


def func2(a, b=10):
    # print(f"a = {a}")
    # print(f"b = {b}")
    # print(f"a + b = {a + b}")
    # return a + b
    if a > b:
        return True

    return False

# func2(23)
# print(func2(23, 7))
sum = func2(23, 7)
# print(func2)

print(sum)

"""
# range
"""
for(i=0; i<5; i++){

}
"""
"""
# for i in range(10):
# for i in range(5, 15):
for i in range(5, 15, 2):
    print(i)
"""

"""
def primeCheck(n):
    for i in range(2, n):
        if n % i == 0:
            print("Composite")
            return False
    print("Prime")
    return True


primeCheck(49)
"""

# OOP
white = (255, 255, 255)

class Car():
    wheels = 5          # class variable

    def __init__(self, make, model, color="white"):
        self.make = make
        self.model = model
        self.color = color

    def printDetails(self):
        print("-------Details---------")
        print("Wheels :", self.wheels)
        print("Make :", self.make)
        print("Model :", self.model)
        print("Color :", self.color)

"""
myCar = Car()
# print(myCar.wheels)
myCar.make = "Tata"         # Object variable
# print(myCar.make)
myCar.model = "Safari"

yourCar = Car()
# print(yourCar.wheels)
# print(yourCar.make)
yourCar.make = "Mahindra"
yourCar.model = "XUV700"

myCar.printDetails()
yourCar.printDetails()
"""

myCar = Car("Tata", "Safari")
yourCar = Car("Mahindra", "XUV700", "Black")
# someonesCar = Car()

myCar.printDetails()
yourCar.printDetails()