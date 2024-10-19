from employee import Employee

class Manager(Employee):
    designation = "Manager"

    def __init__(self, name, age, gender, education):
        super().__init__(name, age, gender)
        self.education = education

    def printDetails(self):
        super().printDetails()
        print("Education:\t".expandtabs(16), self.education)
        print("-" * 20 + "\n\n")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        education = input("education: ")
        return cls(name, age, gender, education)
    
