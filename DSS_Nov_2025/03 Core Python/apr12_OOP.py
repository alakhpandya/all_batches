"""
company = "Tata"

c1_name = "punch"
c1_color = "grey"
c1_fuel = "petrol"
c1_seats = 5
c1_quantity = 3

c2_name = "punch"
c2_color = "white"
c2_fuel = "petrol"
c2_seats = 5
c2_quantity = 4

c3_name = "punch"
c3_color = "grey"
c3_fuel = "electric"
c3_seats = 5
c3_quantity = 5
"""

class Car():
    company = "Tata"        # class variable
    safety = "5 Star"
    airbags = 6

    @staticmethod
    def emi_calculator(amount, duration, rate):
        roi = rate/(1200)
        emi = (amount * roi * ((1 + roi)**duration))/(((1 + roi)**duration) - 1)
        return emi

# c1 = Car()
# print(c1.company)

class Punch(Car):
    seats = 5

class Punch_acomplished(Punch):
    airbags = 7
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


# p1 = Punch()
# print(p1.company)
"""
p2 = Punch_acomplished()
p2.color = "White"
# print(p2.airbags)
p2.print_details()

p3 = Punch_acomplished()
p3.color = "Grey"
p3.print_details()

p1 = Punch_acomplished("White", 7)
p2 = Punch_acomplished("Grey", 5, "Electric")
print("---- Details of P1 ----")
p1.print_details()

print()
print("---- Details of P2 ----")
p2.print_details()

"""
p3 = Punch_acomplished(fuel="Diesel", quantity=10, color="Silver", price=10.5)
# print("---- Details of P3 ----")
# p3.print_details()

print("EMI =", Car.emi_calculator(500000, 60, 12))