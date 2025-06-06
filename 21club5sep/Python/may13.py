# Object Oriented Programming
"""
1. Easy to manage
2. Easy to make programs
"""

"""
name = ["xuv500", "Creta"]
height = [2000, 1750]
length = [2850, 2250]
ground_clearance =[]
bhp = []
torque = []
"""
# x = 5
# print(type(x))

class Car:
    seating_capacity = 5      # class variable

c1 = Car()
print(c1)
print(type(c1))

# Object Variables
c1.name = "Fortuner"
c1.price = 4000000
c1.fuel = "Petrol"
print(c1.name)
print(c1.price)
print(c1.fuel)
c1.seating_capacity = 7
print(c1.seating_capacity)

c2 = Car()
c2.name = "BMW 750i"
c2.price = 15000000
c2.fuel = "Hybrid"
print(c2.seating_capacity)

# Prove that seating_capacity is an object variable of c1