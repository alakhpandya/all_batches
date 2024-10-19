"""
Car Name, Model Name, Seating capacity, fuel, price
"""
stock = []
def addCar():
    print("-----------Add New Car-----------")
    print("Enter the following details:")
    c_name = input("Car Name:")
    m_name = input("Model Name:")
    seating_capacity = int(input("Seating Capacity:"))
    fuel = input("Fuel Type:")
    price = int(input("Price:"))
    car = [c_name, m_name, seating_capacity, fuel, price]
    stock.extend(car)

def printDetails():
    choice = input("Enter the name of the car whose details you want to print: ")
    print(f"------------------Details of {choice}------------------")
    print(f"Car Name: {choice}")
    print(f"Model Name: {stock[stock.index(choice)+1]}")
    print(f"Seating Capacity: {stock[stock.index(choice)+2]}")
    print(f"Fuel Type: {stock[stock.index(choice)+3]}")
    print(f"Price: {stock[stock.index(choice)+4]}")

print("-----------Welcome to Car Management System---------------")
while True:
    print()
    print("Press 1 to Add new car")
    print("Press 2 to Print Details of an existing car")
    print("Press 3 to Change Details of a car")
    print("Press 4 to Delete a car")
    print("Press 5 to Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addCar()

    elif choice == 2:
        printDetails()

    elif choice == 5:
        break
print("Thanks for using Car Management System! See you again soon...")