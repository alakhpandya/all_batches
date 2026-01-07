# Object Oriented Programming
"""
company1 = "Tata"
name1 = "Harrier"
price1 = 3000000
color1 = "Black"

comapny2 = "Maruti"
name2 = "Baleno"
price2 = 1000000
color2 = "Red"


print(f"I have a {name1} of {color2} color.")
"""
"""
class Car():
    def print_car_info(self):
        print("Company:", self.company)
        print("Name:", self.name)
        print("Price:", self.price)

c1 = Car()
c1.name = "Harrier"
c1.price = 30
# c1.color = "Black"
c1.company = "Tata"

c2 = Car()
c2.name = "Baleno"
c2.price = 10
# c2.color = "Red"
c2.company = "Maruti"

c1.print_car_info()
print("----------------------")
c2.print_car_info()
"""

class Car():
    def __init__(self, company, name, price):
        self.company = company
        self.name = name
        self.price = price
        self.color_options = []

    def print_car_info(self):
        print("Company:", self.company)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Colors:", self.color_options)

    def add_color(self, new_color):
        self.color_options.append(new_color)

# c1 = Car("Tata", "Harrier", 30)
# c2 = Car("Maruti", "Baleno", 10)

# c2.add_color("Blue")
# c2.add_color("White")

# c1.print_car_info()
# print("----------------------------------")
# c2.print_car_info()

# print(c1)
car_grid = []
for j in range(3):
    cars_list = []
    for i in range(3):  # i = 0, 1, 2
        new_car = Car("Tata", "Safari", 30)
        cars_list.append(new_car)
    car_grid.append(cars_list)

print(car_grid)