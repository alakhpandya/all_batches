
stock = []
class Car():
    seating_capacity = 5
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel

    def printDetails(self):                             # Polymorphism
        print(f"------Details of {self.name}-----")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating:", self.seating_capacity)

    def updateSeating(self):
        seating = int(input("Enter new seating capacity: "))
        self.seating_capacity = seating

    @staticmethod
    def displayStock():
        print("Serial numbers of cars in stock:")
        print("Sr.No.\tCar Name")
        i = 0
        for car in stock:
            print(f"{i}\t{car.name}")
            i += 1
        c = int(input("Enter serial number of the car: "))
        return c

    @classmethod
    def addNewCar(cls):
        print("Enter the following details please...")
        name = input("Name: ")
        price = int(input("Price: "))
        fuel = input("Fuel: ")
        return cls(name, price, fuel)

class Truck():
    loading_capacity = 3

    def printDetails(self):
        print(f"------Details of {self.name}-----")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Max Load:", self.loading_capacity)

c1 = Car("Skoda", 2000000, "Petrol")
# c1.printDetails()
c2 = Car("Kia", 1500000, "Diesel")
# c2.printDetails()
stock.append(c1)
stock.append(c2)
while True:
    print("Press 1 to print details of a car")
    print("Press 2 to change seating capacity of a car")
    print("Press 3 to add new car")
    print("Press 9 to exit")
    choice = int(input())
    if choice == 1:
        c = Car.displayStock()
        stock[c].printDetails()
    
    elif choice == 2:
        c = Car.displayStock()
        stock[c].updateSeating()
    
    elif choice == 3:
        c = Car.addNewCar()
        stock.append(c)
    
    elif choice == 9:
        break

    else:
        print("Invalid input, please try again...")
    

# 4 pillars of OOP: Polymorphism, Inheritance, Abstraction, Encapsulation
# Next Class: Inheritance- Employee Management System