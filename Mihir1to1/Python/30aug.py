class Car():
    seating_capacity = 5
    wheels = 5
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel

    def printDetails(self):
        print(f"-----------Details of {self.name}------------")
        print("Name :", self.name)
        print("Price :", self.price)
        print("Fuel :", self.fuel)
        print("Seating Capacity :", self.seating_capacity)
        print("------------X---------X----------X-------------")

    @classmethod
    def addNewCar(cls):
        print("Enter the following details of the car: ")
        name = input("Name: ")
        price = int(input("Price: "))
        fuel = input("Fuel Type: ")
        return cls(name, price, fuel)

    @staticmethod
    def displaySerial():
        print("Cars in stock:")
        print("Name\t\tSr.No.")
        for car in stock:
            print(f"{car.name}\t\t{stock.index(car)}")

stock = []
while True:
    print("Press 1 to add new car")
    print("Press 2 to print details of any car")
    print("Press 3 to change the details of an existing car")
    print("Press 4 to delete a car")
    print("Press 5 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        stock.append(Car.addNewCar())

    elif choice == 2:
        Car.displaySerial()
        sr_no = int(input("Enter the serial number of the car whose details you want to print: "))
        stock[sr_no].printDetails()

    elif choice == 3:
        # only specific detail should be changed.
        pass
    elif choice == 4:
        pass

    elif choice == 5:
        break

    else:
        print("This operation is not available presently, please try again...")