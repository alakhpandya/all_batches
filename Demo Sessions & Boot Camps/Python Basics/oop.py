# Object Oriented Programming
class Car():
    wheels = 5      # class variable
    # company_name = None
    # model_name = None
    def __init__(self, comapny, model):
        self.company = comapny
        self.model = model

    def printDetails(self):
        print(f"Details of {self.model}")
        print("Company Name:", self.company)
        print("Wheels:", self.wheels)

"""
myCar = Car()
# print(myCar.wheels)
myCar.wheel_size = 19       # object variable
myCar.company_name = "Tata"
myCar.model_name = "Safari"

yourCar = Car()
# print(yourCar.wheels)
yourCar.company_name = "Mahindra"
yourCar.model_name = "XUV700"
"""
"""
print("Details of myCar:")
print("No. of wheels:", myCar.wheels)
print("Wheel size:", myCar.wheel_size)

print("Details of yourCar:")
print("No. of wheels:", yourCar.wheels)
print("Wheel size:", yourCar.wheel_size)
"""

# myCar.printDetails()
# yourCar.printDetails()

myCar = Car("Tata", "Safari")
myCar.printDetails()

yourCar = Car("Mahindra", "XUV700")
yourCar.printDetails()