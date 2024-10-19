# Employee management system
staff = []
class Employee():
    leaves = 5
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

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
    def deleteEmployee():
        Employee.displayStaff()
        emp = int(input("Enter Sr.No. of the employee you want to delete: "))
        staff.pop(emp)
        print(f"Employee with Sr.No. {emp} deleted successfully!")

    @staticmethod
    def addNewEmployee():
        print("Enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        salary = int(input("Salary: "))
        return (name, age, gender, salary)

class Teacher(Employee):
    department = "Teaching"
    
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


class Admin(Employee):
    department = "Admin"

    def printDetails(self):
        super().printDetails()

    @classmethod
    def addNewEmployee(cls):
        name, age, gender, salary = super().addNewEmployee()
        return cls(name, age, gender, salary)


t1 = Teacher("A", 21, "female", 50000, ["C", "C++"])
a1 = Admin("B", 24, "female", 25000)
staff.append(t1)
staff.append(a1)
while True:
    print("\nEnter 1 to add new employee")
    print("Enter 2 to print details of an existing employee")
    print("Enter 3 to change details of an existing employee")
    print("Enter 4 to delete an employee")
    print("Enter 5 to exit")
    choice = int(input())
    if choice == 1:
        print("Enter 1 to add new teacher")
        print("Enter 2 to add new admin")
        emp_type = int(input())
        if emp_type == 1:
            staff.append(Teacher.addNewEmployee())
        elif emp_type == 2:
            staff.append(Admin.addNewEmployee())
    elif choice == 2:
        Employee.displayStaff()
        emp = int(input("Enter Sr.No. of the employee you want to see details of: "))
        staff[emp].printDetails()
    elif choice == 3:
        pass
    elif choice == 4:
        Employee.deleteEmployee()
    elif choice == 5:
        break
    else:
        print("Invalid option, please try again...")
