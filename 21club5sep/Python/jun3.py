"""
from abc import ABC, abstractmethod     

staff = []
class Employee(ABC):
    _leaves = 5                 # protected variable
    
    @abstractmethod
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self._salary = salary       # protected variable

    @abstractmethod
    def printDetails(self):
        print(f"--------------Details of {self.name}--------------")
        print(f"Name:\t{self.name}".expandtabs(15))
        print(f"Age:\t{self.age}".expandtabs(15))
        print(f"Gender:\t{self.gender}".expandtabs(15))
        print(f"Salary:\t{self.salary}".expandtabs(15))
        print(f"Department:\t{self.department}".expandtabs(15))

    @staticmethod
    def displayStaff():
        i = 0
        print("Presently working employees:")
        print(f"Sr.No.\tName")
        for member in staff:
            print(f"{i}.\t{member.name}")
            i += 1
    
    @staticmethod
    def _protectedMethod():         # protected method
        print("I am protected method...")

    @staticmethod
    def __privateMethod():
        print("I am a private method...")

    @staticmethod
    def deleteEmployee():
        Employee.displayStaff()
        emp = int(input("Enter Sr.No. of the employee you want to delete: "))
        staff.pop(emp)
        print(f"Employee with Sr.No. {emp} deleted successfully!")

    @staticmethod
    @abstractmethod
    def addNewEmployee():
        print("Enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        salary = int(input("Salary: "))
        return (name, age, gender, salary)

class Teacher(Employee):
    department = "Teaching"
    __feedback = 0                # private variable
    
    def __init__(self, name, age, gender, salary, subjects):
        super().__init__(name, age, gender, salary)
        self.subjects = subjects

    def printDetails(self):
        super().printDetails()
        print(f"Subjects:\t{self.subjects}".expandtabs(15))

    @classmethod
    def addNewEmployee(cls):
        name, age, gender, salary = super().addNewEmployee()
        no_of_subjcets = int(input("No of Subjects taught: "))
        print(f"Enter name(s) of {no_of_subjcets} subjects one by one:")
        subjects = [input() for i in range(no_of_subjcets)]
        return cls(name, age, gender, salary, subjects)

class Coordinator(Teacher):
    def __init__(self, name, age, gender, salary, subjects):
        super().__init__(name, age, gender, salary, subjects)

    @classmethod
    def addNewEmployee(cls):
        return super().addNewEmployee()

    def printDetails(self):
        return super().printDetails()


class Admin(Employee):
    department = "Admin"
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender, salary)

    def printDetails(self):
        super().printDetails()

    @classmethod
    def addNewEmployee(cls):
        name, age, gender, salary = super().addNewEmployee()
        return cls(name, age, gender, salary)

# class Peon(Employee):
#     def __init__(self, name, age, gender, salary):
#         super().__init__(name, age, gender, salary)

#     def printDetails(self):
#         super().printDetails()

#     @classmethod
#     def addNewEmployee(cls):
#         name, age, gender, salary = super().addNewEmployee()
#         return cls(name, age, gender, salary)
    
t1 = Teacher("A", 21, "female", 50000, ["C", "C++"])
a1 = Admin("B", 24, "female", 25000)
staff.append(t1)
staff.append(a1)
# p1 = Peon("Suketu", 22, "Male", 18000)
# p1.department = "General"
# p1.printDetails()
c1 = Coordinator("Chhagan", 36, "Male", 36000, ["OS", "Discrete Maths", "Astrophysics"])

print("No. of leaves of teacher:", t1._leaves)
print("No. of leaves of Admin:", a1._leaves)
# print("No. of leaves of Peon:", p1._leaves)
print("No. of leaves of Coordinator:", c1._leaves)

# Name mangling to access private variables and methods
print("Feedback of Teacher:", t1._Teacher__feedback)
c1._Teacher__feedback = 5
print("Feedback of Coordinator:", c1._Teacher__feedback)
c1._Employee__privateMethod()
# e1 = Employee("Krishna", 24, "Male", 35000)
# e1.department = "Maintenance"
# e1.printDetails()
# while True:
#     print("\nEnter 1 to add new employee")
#     print("Enter 2 to print details of an existing employee")
#     print("Enter 3 to change details of an existing employee")
#     print("Enter 4 to delete an employee")
#     print("Enter 5 to exit")
#     choice = int(input())
#     if choice == 1:
#         print("Enter 1 to add new teacher")
#         print("Enter 2 to add new admin")
#         emp_type = int(input())
#         if emp_type == 1:
#             staff.append(Teacher.addNewEmployee())
#         elif emp_type == 2:
#             staff.append(Admin.addNewEmployee())
#     elif choice == 2:
#         Employee.displayStaff()
#         emp = int(input("Enter Sr.No. of the employee you want to see details of: "))
#         staff[emp].printDetails()
#     elif choice == 3:
#         pass
#     elif choice == 4:
#         Employee.deleteEmployee()
#     elif choice == 5:
#         break
#     else:
#         print("Invalid option, please try again...")
"""

# Exception Handling
print("Enter two numbers:")
while True:
    try:
        a = float(input())
        b = float(input())
        c = a/b
        if c < 0:
            # raise Exception
            raise NameError
        
    except ZeroDivisionError:
        print("Oops! Seems you're trying to divide by zero! Please try again...")
    except ValueError:
        print("Please enter numbers only... Try again.")
    # except:
    #     print("Oops! Something went wrong, please try again...")
    # except Exception:
    #     print("Oops! Something went wrong, please try again...")
    # except Exception as e:
    #     print(e)


    else:
        print("Division =", c)
        d = int(input("Enter power: "))
        e = c ** d
        print("Final answer =", e)

    finally:
        choice = input("Press 'q' to quit or 'Enter' to enter two new numbers: ").lower()
        if choice == 'q':
            break
        print("Enter two new numbers:")

# Next Class: File Handling, Resource Handling/Management