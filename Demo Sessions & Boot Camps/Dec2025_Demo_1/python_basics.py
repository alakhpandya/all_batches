# Procedure Oriented Programming
"""
mil = 15
col = "Golden"
engine = 2000
power = 200
seat = 7

if seat > 5:
    tax = 0.18
else:
    tax = 0.12
"""

# Object Oriented Programming
"""
class Car():
    wheels = 5
    def __init__(self, company, model, seats, color):
        self.company = company
        self.model = model
        self.seats = seats
        self.color = color
    
    def get_details(self):
        print("-------- Details of your car --------")
        print("Company =", self.company)
        print("Model =", self.model)
        print("Seats =", self.seats)
        print("Color =", self.color)
"""
"""
c1 = Car()
# print(c1.wheels)
c1.company = "Tata"
c1.model = "Safari"
c1.color = "Black"
c1.seats = 7

c2 = Car()
# print(c2.wheels)
c2.company = "Mahindra"
c2.model = "XUV 700"
c2.color = "Blue"
c2.seats = 7

# print("Color of c1:", c1.color)
c1.get_details()
c2.get_details()
"""
"""
c1 = Car("Tata", "Sierra", 5, "Yellow")
c1.get_details()

c2 = Car("Mahindra", "XEV 9E", 5, "Golden")
c2.get_details()
"""

for i in range(1, 7):  # i = 1,2,3,4,5,6
    for j in range(1, 7):   # j = 1,2,3,4,5,6
        print(i, j)