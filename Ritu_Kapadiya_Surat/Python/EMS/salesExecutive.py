from employee import Employee

class SalesExecutive(Employee):
    designation = "Sales Executive"

    def __init__(self, name, age, gender, target):
        super().__init__(name, age, gender)
        self.target = target

    def printDetails(self):
        super().printDetails()
        print("Target:\t".expandtabs(16), self.target)
        print("-" * 20 + "\n\n")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        target = int(input("Target: "))
        return cls(name, age, gender, target)

if __name__ == "__main__":
    s1 = SalesExecutive("Vikas", 32, "M", 500000)
    s1.printDetails()