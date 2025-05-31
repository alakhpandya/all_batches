from employee import Employee

class Peon(Employee):
    designation = "Peon"

    
    def printDetails(self):
        super().printDetails()
        print("-" * 20 + "\n\n")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)