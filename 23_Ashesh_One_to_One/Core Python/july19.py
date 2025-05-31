"""
string examples:
1. Write a Python program to get a string from a given string where all occurrences of its first character have been changed to '$', except the first character itself.

Sample String : 'restart your computer'
Expected Result : 'resta$t you$ compute$'

2. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Print the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'


3. Write a Python function that takes a list of words and return the longest word and the length of the longest one

Sample:
input list = ["you", "should", "do", "exercise", "daily"]
Longest word: Exercise
Length of the longest word: 8

4. Write a Python program to remove the nth index character from a nonempty string.


5. Write a Python program to remove the characters which have odd index values of a given string.

6. Write a Python program to count the occurrences of each word in a given sentence.

7. Write a Python program that accepts a comma separated sequence of words (all in lower case, without any special character) as input and prints the unique words in sorted alphanumerically.

Sample Words : red,white,black,red,green,black
Expected Result : 
green
white

8. Write a Python function to create the HTML string with tags around the word(s).

Sample function and result :
add_tags('h1', 'Python') -> '<h1>Python</h1>'
add_tags('p', 'Python Tutorial') -> '<p>Python Tutorial </p>'

9. Write a Python function to insert a string in the middle of a string.

Sample function and result :
insert_sting_middle('[[]]', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

10. Write a Python program to create a Caesar encryption.

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

sample:
input string: Meet me in the park
shift: 3
output string: phhw ph lq wkh sdun

sample-2:
input string: Meet me in the park
shift: -7
output string: fxxm fx bg max itkd
"""

# Encapsulation:

from abc import ABC, abstractmethod                      # abc = abstract base classes, ABC = Abstract Base Class
from datetime import datetime

staff = []

class Employee(ABC):
    
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
    # @abstractmethod
    def addEmployee():
        print("Please enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return (name, age, gender)

    @abstractmethod
    def displayDetails(self):
        print(f"-----------Details of Employee id - {self.id}-----------")
        print(f"Name:\t{self.name}")
        print(f"Age:\t{self.age}")
        print(f"Gender:\t{self.gender}")
        print(f"Designation:\t{self.designation}")

class Manager(Employee):
    designation = "Manager" 
    team_size = 10
    _salary = 40000          # protected variable
    __performance = 1             # private variable

    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience

    def __updateSalary(self):           # private method
        self.salary = int(input("Enter new salary: "))

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


m1 = Manager("Raman", 24, "Male", 3.5)
print(m1._salary)
m1._salary = 50000
print(m1._salary)
# print(m1.__performance)
# Name mangling
print(m1._Manager__performance)


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
"""