"""
10 different model
details of each car: model name, ex show room price, fuel type, length, width, height, ground clearance, kerb weight, net weight, engine hp, engine torque, airbags, seating capacity, mileage, on road price, quantity

c1 = ["Amaze"]
c2 = ["City"]
c3 = ["Accord"]
c4 = ["Civic"]
"""
# a = 5
# print(type(a))

# b = "Hello World!"
# b.__add__("!")
"""
Write a program & ask number of input strings from the user (t). Next, ask all 't' number of strings from user & print number of vowels & consonents in those strings.

first line of code will always be numeber of inputs.

example-
input-1:
2
royal
technosoft

output-1
2 3
3 7


def main():
    # Your code goes here

    return

if __name__ == "main":
    main()
"""

class Car:
    seating_capacity = 5        # class variable

c1 = Car()
# object variables
c1.modelName = "Amaze"
c1.fuel = "Petrol"
c1.price = 700000

print("------Details------")
print("Name:", c1.modelName)
print("Fuel:", c1.fuel)
print("Price:", c1.price)
print("Seating Capacity:", c1.seating_capacity)



c3 = Car()
c3.modelName = "XUV 700"
c3.fuel = "Electric"
c3.price = 2500000
c3.seating_capacity = 7

print("------Details------")
print("Name:", c3.modelName)
print("Fuel:", c3.fuel)
print("Price:", c3.price)
print("Seating Capacity:", c3.seating_capacity)

c2 = Car()
# object variables
c2.modelName = "Baleno"
c2.fuel = "Diesel"
c2.price = 900000

print("------Details------")
print("Name:", c2.modelName)
print("Fuel:", c2.fuel)
print("Price:", c2.price)
print("Seating Capacity:", c2.seating_capacity)

print(c2.__dict__)      # dictionary of all the object variables of c2
print(c3.__dict__)

# c3.airbags