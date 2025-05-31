"""
class Car:
    seating_capacity = 5
    def __init__(self, model_name, fuel, price):
        self.model_name = model_name
        self.fuel = fuel
        self.price = price

    # Methods
    def printDetails(self):
        print("------Details------")
        print("Name:", self.model_name)
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seating Capacity:", self.seating_capacity)


class TwoWheeler:
    pass

t1 = TwoWheeler()
c1 = Car("Amaze", "Petrol", 700000)

# c1.printDetails()

c2 = Car("XUV700", "Diesel", 2800000)
c2.printDetails()
"""
# DRY: Do not Repeat Yourself
# Inheritance
"""
class Car():
    seating_capacity = 5

class HatchBack(Car):
    airbags = 2

class Sedan(Car):
    airbags = 4

class PremiumHatchback(HatchBack):
    automaticTransmission = True

c1 = Car()
print(c1.seating_capacity)

h1 = HatchBack()
print(h1.airbags)
print(h1.seating_capacity)

s1 = Sedan()
print(s1.airbags)
print(s1.seating_capacity)

p1 = PremiumHatchback()
print(p1.airbags)
print(p1.automaticTransmission)
print(p1.seating_capacity)
"""
"""
class Parent():
    vehicle = "Car"

class Child(Parent):
    education = "Masters"
    vehicle = "Maestro"


c1 = Child()
print(c1.vehicle)
print(c1.education)

c2 = Child()
c2.vehicle = "Bike"
print(c2.vehicle)
# print(c2.profession)      MRO: Method Resolution Order

"""
# Types of inheritance
"""
1. Single
2. Multilevel
3. Multiple
4. Hierachicle
5. Hybrid
"""

class Parent1():
    vehicle = "car"

class Parent2():
    profession = "grocery store"

class Child(Parent1, Parent2):
    pass

c1 = Child()
print(c1.vehicle)
print(c1.profession)

# Next Class: Multiple inheritance in greater detail