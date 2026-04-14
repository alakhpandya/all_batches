class Car():
    company = "Tata"        # class variable
    safety = "5 Star"
    airbags = 6

    @staticmethod
    def emi_calculator(amount, duration, rate):
        roi = rate/(1200)
        emi = (amount * roi * ((1 + roi)**duration))/(((1 + roi)**duration) - 1)
        return emi

class Punch(Car):
    name = "Punch Pure"
    seats = 5
    def __init__(self, color, price, quantity=5, fuel="Petrol"):
        self.color = color
        self.quantity = quantity
        self.fuel = fuel
        self.price = price

    def print_details(self):
        print(f"Company: {self.company}")
        print(f"Satety: {self.safety}")
        print(f"Airbags: {self.airbags}")
        print(f"Seats: {self.seats}")
        print(f"Fuel: {self.fuel}")
        print(f"Color: {self.color}")
        print(f"Quantity: {self.quantity}")

class Punch_acomplished(Punch):
    airbags = 7
    name = "Punch Acomplished"

inventory = []
while True:
    print("""Enter:
- 1 to create a new car object
- 2 to view details of an object
- 3 to delete an object
""")
    main_menu_opt = int(input())
    if main_menu_opt == 1:
        print("Choose a model:")
        print("""Enter:
    1 for Punch Pure
    2 for Punch Acomplished
    """)
        sub_menu_opt = int(input())
        print("Enter the following details:")
        color = input("Color: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))
        fuel = input("Fuel: ")
        if sub_menu_opt == 1:
            inventory.append(Punch(color, price, quantity, fuel))
        elif sub_menu_opt == 2:
            inventory.append(Punch_acomplished(color, price, quantity, fuel))

    elif main_menu_opt == 2:
        print("Enter the sr_no of the car you want to see details of:")
        print("Sr_No.\tName")
        sr_no = 1
        for car in inventory:
            print(f"{sr_no}\t{car.name}")
            sr_no += 1
        ind = int(input())-1
        inventory[ind].print_details()
    elif main_menu_opt == 3:
        pass
    elif main_menu_opt == 4:
        break
    else:
        print("Invalid input, please try again...")

print(inventory)