# OOP
"""
1. Code Re-usablilty    :   DRY - Do Not Repeat Yourself
2. Resembles with real world

Class : Virtual Concept
Object: Physical entity
"""
"""
class Car:
    seating_capacity = 5    # class variable

    def printDetalils(self):
        print(f"-----------Details of {self.name}------------")
        print("Name :", self.name)
        print("Price :", self.price)
        print("Fuel :", self.fuel)
        print("Seating Capacity :", self.seating_capacity)
        print("------------X---------X----------X-------------")

c1 = Car()
c1.name = "Creta"   # object variables
c1.price = 200
c1.fuel = "D"

c2 = Car()
c2.name = "Baleno"
c2.price = 80
c2.fuel = "P"


# print("Name :", c1.name)
# print("Price :", c1.price)
# print("Fuel :", c1.fuel)
# print("Seating Capacity :", c1.seating_capacity)

c3 = Car()
c3.name = "XUV500"
c3.price = 220
c3.fuel = "D"
c3.seating_capacity = 7

# print("------------------------------------------")
# print("Name :", c3.name)
# print("Price :", c3.price)
# print("Fuel :", c3.fuel)
# print("Seating Capacity :", c3.seating_capacity)

# print("------------------------------------------")
# print("Name :", c2.name)
# print("Price :", c2.price)
# print("Fuel :", c2.fuel)
# print("Seating Capacity :", c2.seating_capacity)

# print("-------------------------------------------")
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)

c1.printDetalils()
c2.printDetalils()
c3.printDetalils()
"""
class Car():
    seating_capacity = 5
    wheels = 5
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel

    def printDetalils(self):
        print(f"-----------Details of {self.name}------------")
        print("Name :", self.name)
        print("Price :", self.price)
        print("Fuel :", self.fuel)
        print("Seating Capacity :", self.seating_capacity)
        print("------------X---------X----------X-------------")

c1 = Car("Creta", 200, "D")
c2 = Car("Baleno", 80, "P")
c3 = Car("XUV500", 220, "D")
c3.seating_capacity = 7
print("Which Car's details do you want to see?")
print("Press 1 for c1")
print("Press 2 for c2")
print("Press 3 for c3")
choice = int(input())
if choice == 1:
    c1.printDetalils()
elif choice == 2:
    c2.printDetalils()
elif choice == 3:
    c3.printDetalils()
else:
    print("Invalid Car... Please try again")