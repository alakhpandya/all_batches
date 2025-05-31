from employee import Employee

class Developer(Employee):
    designation = "Developer"
    
    def __init__(self, name, age, gender, department):
        super().__init__(name, age, gender)
        self.department = department

    def printDetails(self):
        super().printDetails()
        print("Department:\t".expandtabs(16), self.department)
        print("-" * 20 + "\n\n")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        department = input("Department: ")
        return cls(name, age, gender, department)