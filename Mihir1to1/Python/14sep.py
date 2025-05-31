# Abstraction
"""
1. To restrict a class to create object in it.
2. To make it compulsary for every child classes to have some method(s).

from abc import ABC, abstractmethod

class Employee(ABC):
    no_of_leaves = 5
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # @abstractmethod
    def printDetails(self):
        print(f"--------Details of {self.name}-------")
        print(f"Name:\t\t{self.name}")
        print(f"Age:\t\t{self.age}")
        print(f"Gender:\t\t{self.gender}")

    @staticmethod
    @abstractmethod
    def addEmployee():
        print("Enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return (name, age, gender)

class Manager(Employee):
    education = "MBA"
    def __init__(self, name, age, gender, team_size):
        super().__init__(name, age, gender)
        self.team_size = team_size

    def printDetails(self):
        super().printDetails()
        print(f"Education:\t{self.education}")
        print(f"Team Size:\t{self.team_size}")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()   # ("Mihir", 19, "Male")
        team_size = int(input("Team Size: "))
        return cls(name, age, gender, team_size)

class Peon(Employee):
    pass

class Clerk(Employee):
    pass

# e1 = Employee("R", 22, "F")
# m1 = Manager("N", 18, "F", 10)
# p1 = Peon("Z", 23, "M")
m1 = Manager.addEmployee()
m1.printDetails()
"""

# Encapsulation
"""
1. Public
2. Protected
3. Private
"""
class Royal():
    pass

class Student(Royal):
    def __init__(self, name, age, gender, mobile):
        self.name = name
        self.age = age
        self.gender = gender
        self._mobile = mobile       # protected variable

class Faculty(Royal):
    pass

class Admin(Royal):
    __fees = 500000

    def __changeFees(self):
        newFees = int(input("Enter new fees: "))
        self.__fees = newFees

class SuperAdmin(Royal):
    pass

a1 = Admin()
# a1.__changeFees()
# print(a1.__fees)
print(a1._Admin__fees)      # Name Mangling
a1._Admin__changeFees()

s1 = Student("Khushi", 10, "female", 9923223458)
print(s1._mobile)

# Upcoming Lectures: Exception Handling, File Handling, Resource Management, Database Connection