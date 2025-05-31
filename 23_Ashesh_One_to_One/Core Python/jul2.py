# Changing class variables

class Car:
    seating_capacity = 5    # class variable

    def __init__(self, model, price, fuel):
        self.model = model
        self.price = price
        self.fuel = fuel

    # Method
    def displayDetails(self):
        print(f"\n-----------Details of {self.model}-----------")
        print("Model:", self.model)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating Capacity:", self.seating_capacity)


c1 = Car("Baleno", 1000000, "Petrol")
"""
c1 = Car()
c1.model = "Baleno"
c1.price = 1000000
c1.fuel = "Petrol"
Car.seating_capacity = 7
"""
# print("Seating Capacity:", c1.seating_capacity)
c1.displayDetails()

c2 = Car("Tesla S", 5000000, "Electric")
"""
c2 = Car()
c2.model = "Tesla S"
c2.price = 5000000
c2.fuel = "Electric"
"""
c2.displayDetails()


c3 = Car("Corvette", 8000000, "Petrol")
"""
c3 = Car()
c3.model = "Corvette"
c3.price = 8000000
c3.fuel = "Petrol"
"""
c3.displayDetails()