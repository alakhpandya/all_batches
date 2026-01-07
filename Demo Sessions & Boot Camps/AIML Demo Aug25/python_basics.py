"""
print("AIML Demo")

# Creating Variables in Python:
x = 5
city = "Ahmedabad"

# Collections in Python: list, dictionary, tuple, set
myList = [5, 9, 13, 15, 18, 20]
myTuple = (5, 9, 13, 15, 18, 20)

print("myList =", myList)
print("my tuple =", myTuple)

myTuple = (6, 4, 2)
print("my tuple =", myTuple)

myList.append(25)
print("my list =", myList)

# myTuple.append(20)            Error

fruits = ["apple", "mango", "banana", "grapes", 23, 45, 13.5, 3j-7]
print("New collection =", fruits)

a = {2,32,501, 21,-44}
b = {14,
     33,
     25,
     -18
     }
print("A =", a)

capitals = {
    "Gujarat" : "Gandhinagar",
    "Maharashtra" : "Mumbai",
    "Tamil Nadu" : "Chennai",
    "India" : "Delhi"
}
print(capitals)

print("length of capitals dictionary:", len(capitals))

print(capitals["Tamil Nadu"])
capitals["Tamil Nadu"] = "Madras"

capitals["Rajasthan"] = "Jaipur"

print(capitals)

fruits = ["apple", "mango", "banana", "grapes", "pineapple"]
print(fruits[3])
my_fav_fruit = fruits[1]
print(my_fav_fruit.upper())

my_lucky_no = myTuple[0]
print(my_lucky_no)

x = 0
while x <= 4:
    print(fruits[x])
    x = x + 1
print("End of program")
"""

# Basic Operator:
"""
print(6 / 4)
print(6 % 4)
print(35 // 4)
print(6 * 3)
print(6 ** 3)
"""
"""
fruits = ["apple", "mango", "banana", "grapes", "pineapple"]
x = 0
while x <= 4:
    if x % 2 == 0:
        print(fruits[x].upper())
    else:
        print(fruits[x])
    x = x + 1
print("End of program")
"""
# length < 6: small name, = 6 : medium name, > 6 long name
"""
fruits = ["apple", "mango", "banana", "grapes", "pineapple"]
x = 0
while x <= 4:
    if len(fruits[x]) < 6:
        print(fruits[x], "- Small name")
    elif len(fruits[x]) = 6:
        print(fruits[x], "- Medium name")
    else:
        print(fruits[x], "- Long name")
    x = x + 1
print("End of program")
"""

fruits = ["apple", "mango", "banana", "grapes", "pineapple"]

"""
x = 0
while x <= 4:       # x = 0, 1, 2, 3, 4, 5
    print(fruits[x])
    x = x + 1
"""
"""
for fruit in fruits:        # x = "apple", "mango", "banana", "grapes", "pineapple"
    print(fruit)


class Table():
    legs = 4
    def __init__(self, type, meterial, color):
        self.type = type
        self.meterial = meterial
        self.color = color

    def printDetails(self):
        print("========= Detials of the Table =========")
        print("Type:", self.type)
        print("Legs:", self.legs)
        print("Meterial:", self.meterial)
        print("Color:", self.color)


study_table_1 = Table("study table", "eng_wood", "white")
# print(study_table_1.legs)
# study_table_1
study_table_1.printDetails()

dining_table_1 = Table("dining table", "tic", "beige")
dining_table_1.printDetails()


# for (i = 0; i < 10; i++)
# for i in range(10):
for i in range(1, 11):
    print(i)
"""

x = float("inf")
print(x > 98245847320710983734982374798209387923078590827345907204958732409857203495709324872509374207)
