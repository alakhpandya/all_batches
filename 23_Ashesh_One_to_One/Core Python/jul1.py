# OOP
"""
x = 5
print(x)
print(type(x))
y = "Python"
print(y)
print(type(y))
# y = y - "Ashesh"
y.reverse()
"""
class Car:
    seating_capacity = 5    # class variable

c1 = Car()

# Object Variables
# c1.color = "Red"
c1.price = 1000000
c1.model = "Baleno"
c1.fuel = "Petrol"

print("-----------Details of C1-----------")
print("Model:", c1.model)
print("Price:", c1.price)
print("Fuel:", c1.fuel)
print("Seating Capacity:", c1.seating_capacity)

c2 = Car()
# print(c2.price)
print("Seating Capacity of c2:", c2.seating_capacity)

c3 = Car()
c3.model = "Innova"
c3.seating_capacity = 7
print("-----------Details of C3-----------")
print("Model:", c3.model)
# print("Price:", c3.price)
# print("Fuel:", c3.fuel)
print("Seating Capacity:", c3.seating_capacity)

print("Seating Capacity of c2:", c2.seating_capacity)

print(c1.__dict__)
print(c3.__dict__)

# Next Class: functions inside a class