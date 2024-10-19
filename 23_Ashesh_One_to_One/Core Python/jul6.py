# Staff Management System
from datetime import datetime

staff = []

class Employee():
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def determineEmployeeType():
        print("Press 1 to add a manager")
        print("Press 2 to add a general manager")
        print("Press 3 to add a sales executive")
        print("Press 4 to add a peon")
        emp_type = int(input())
        return emp_type

    @staticmethod
    def generateID():
        # sample id: 202207M002
        year = datetime.now().year
        month = datetime.now().month
        if emp_type == 1:
            emp_code = "M"
        elif emp_type == 2:
            emp_code = "G"
        elif emp_type == 3:
            emp_code = "S"
        elif emp_type == 4:
            emp_code = "P"
        emp_index = len(staff)
        emp_id = str(year) + str(month).zfill(2) + emp_code + str(emp_index).zfill(3)
        return emp_id

    @staticmethod
    def addEmployee():
        print("Please enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return (name, age, gender)

    def displayDetails(self):
        print(f"-----------Details of Employee id - {self.id}-----------")
        print(f"Name:\t{self.name}")
        print(f"Age:\t{self.age}")
        print(f"Gender:\t{self.gender}")
        print(f"Designation:\t{self.designation}")

class Manager(Employee):
    designation = "Manager" 
    team_size = 10

    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience

    @classmethod
    def addManager(cls):
        name, age, gender = super().addEmployee()
        experience = float(input("Experience: "))
        return cls(name, age, gender, experience)

    def displayDetails(self):
        # call Parent's displayDetails
        super().displayDetails()
        print(f"Experience:\t{self.experience}")
        print(f"Team Size:\t{self.team_size}")

class SalesExecutive(Employee):
    designation = "Sales Executive"                         # example of polymorphism
    target = 150000

    def __init__(self, name, age, gender, territory):       # example of polymorphism
        super().__init__(name, age, gender)
        self.territory = territory

    @classmethod
    def addSalesExecutive(cls):
        name, age, gender = super().addEmployee()
        territory = input("Territory: ")
        return cls(name, age, gender, territory)

    def displayDetails(self):
        super().displayDetails()
        print(f"Territory:\t{self.territory}")
        print(f"Target:\t{self.target}")

class Peon(Employee):
    designation = "Peon"

    @classmethod
    def addPeon(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

class GeneralManager(Manager):
    designation = "General Manager"
    team_size = 120

    @classmethod
    def addGeneralManager(cls):
        name, age, gender = super().addEmployee()
        experience = float(input("Experience: "))
        return cls(name, age, gender, experience)

class Accountants(Employee):
    designation = "Accountant"
    education = "CPA"

# Main program
"""
a = Employee("Ashesh", 25, "Male")
staff.append(a)
"""

while True:
    print("Press 1 to add an employee")
    print("Press 2 to view details of an existing employee")
    print("Press 3 to delete an employee")
    print("Press 9 to exit")
    choice = int(input())
    if choice == 1:
        print("---------Welcome to add an employee menu---------")
        
        emp_type = Employee.determineEmployeeType()
        if emp_type == 1:
            new_employee = Manager.addManager()
        
        elif emp_type == 2:
            new_employee = GeneralManager.addGeneralManager()
        
        elif emp_type == 3:
            new_employee = SalesExecutive.addSalesExecutive()
        
        elif emp_type == 4:
            new_employee = Peon.addPeon()
        
        else:
            print("Invalid employee type, please try again...")
            new_employee = None

        new_employee.id = Employee.generateID()
        staff.append(new_employee)

    elif choice == 2:
        # Code to print details of an existing employee
        print("---------Welcome to display details menu---------")
        emp_id = input("Enter employee id: ")
        emp_index = int(emp_id[-3 : ])
        staff[emp_index].displayDetails()

    elif choice == 3:
        # Code to delete an employee
        emp_id = input("Enter employee id: ")
        emp_index = int(emp_id[-3 : ])
        deleted_emp = staff.pop(emp_index)
        print(f"Employee id: {deleted_emp.id} deleted successfully!")
        pass

    elif choice == 9:
        break

    else:
        print("Invalid input, please try again...")

print(staff)

"""
2 Requirements:
1. Do not allow creating objects in Employee() class
2. All the child classes of Employee() must have their own displayDetails() method
"""