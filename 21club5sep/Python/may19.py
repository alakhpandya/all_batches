"""
class Car:
    seating_capacity = 5      # class variable

    def printDetails(self):
        print(f"------Details of {self.name}-----")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating:", self.seating_capacity)

c1 = Car()
# print(c1)
# print(type(c1))

# Object Variables
c1.name = "Fortuner"
c1.price = 4000000
c1.fuel = "Petrol"
c1.seating_capacity = 7
c1.printDetails()

c2 = Car()
c2.name = "BMW 750i"
c2.price = 15000000
c2.fuel = "Hybrid"
# print(c2.seating_capacity)

# print(type(c2.__dict__))
# print(c2.__dict__)
# print(c1.__dict__)
print()
c2.printDetails()
"""
stock = []
class Car():
    seating_capacity = 5
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel

    def printDetails(self):
        print(f"------Details of {self.name}-----")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating:", self.seating_capacity)

    def updateSeating(self):
        seating = int(input("Enter new seating capacity: "))
        self.seating_capacity = seating

c1 = Car("Skoda", 2000000, "Petrol")
# c1.printDetails()
c2 = Car("Kia", 1500000, "Diesel")
# c2.printDetails()
stock.append(c1)
stock.append(c2)
print("Press 1 to print details of a car")
print("Press 2 to change seating capacity of a car")
choice = int(input())
if choice == 1:
    print("Serial numbers of cars in stock:")
    print("Sr.No.\tCar Name")
    i = 0
    for car in stock:
        print(f"{i}\t{car.name}")
        i += 1
    c = int(input("Enter serial number of the car: "))
    stock[c].printDetails()
elif choice == 2:
    pass
else:
    print("Invalid input, please try again...")
# print(stock)

"""
Homework:
write the missing code in section "elif choice == 2:"
add one more option "Press 3 to add new car" and write the code that adds new car with name, price and fuel given by user.
"""