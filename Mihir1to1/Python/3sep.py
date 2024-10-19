# 4 pillars of oop:
"""
1. Inheritance
2. Polymorphism
3. Abstraction
4. Encapsulation
"""
# Inheritance
# 1. Simple/Single inheritance
"""
class Parent():
    hobby = "Garba"
    education = "Masters"
    def printDetails(self):
        print("-----Details------")
        print(self.hobby)
        print(self.education)

class Child(Parent):
    education = "10+2"

c1 = Child()
print(c1.hobby)
print(c1.education)
# print(Child.mro())
# print(c1.profession)
c1.printDetails()
"""
# 2. Multi-level Inheritance: Parent class -> Child Class ->Grand Child Class
"""
class Parent():
    hobby = "Garba"
    education = "Masters"
    def printDetails(self):
        print("-----Details------")
        print(self.hobby)
        print(self.education)

class Child(Parent):
    education = "10+2"
    profession = "job"

class GrandChild(Child):
    pass

g1 = GrandChild()
print(g1.profession)
print(g1.hobby)
print(g1.education)
g1.printDetails()
"""
# 3. Hierarchical Inheritance
"""             -> Child Class 1
Parent Class    -> Child Class 2
                -> Child Class 3

class Parent():
    hobby = "Garba"
    education = "Masters"
    def printDetails(self):
        print("-----Details------")
        print(self.hobby)
        print(self.education)

class Child1(Parent):
    pass

class Child2(Parent):
    education = "10+2"
    profession = "job"

class Child3(Parent):
    pass
"""
# 4. Multiple Inheritance
"""
Parent1 class
Parent2 class   --> Child Class
Parent3 class

"""
"""
class Parent1():
    hobby = "Garba"
    education = "Masters"
    def printDetails(self):
        print("-----Details------")
        print(self.hobby)
        print(self.education)

class Parent2():
    profession = "Doctor"
    salary = 100000
    education = "MBBS"

class child(Parent2, Parent1):  # The class written first gets higher priority
    pass

c1 = child()
print(c1.profession)
print(c1.salary)
print(c1.education)
print(c1.hobby)
"""
# Diamond Problem
"""
class Parent1():
    hobby = "Garba"
    education = "Masters"
    def printDetails(self):
        print("-----Details------")
        print(self.hobby)
        print(self.education)

class Parent2():
    profession = "Doctor"
    salary = 100000
    education = "MBBS"

class Child1(Parent1, Parent2):  
    pass

class Child2(Parent2, Parent1):
    pass

class GrandChild(Child1, Child2):
    pass

c1 = Child1()
c2 = Child2()
print(c1.education)
print(c2.education)
g1 = GrandChild()
print(g1.education)
"""
# 5. Hybrid Inheritance
"""
More than one types of inheritance used in the same program is called Hybrid Inheritance.
"""
class Employee():
    no_of_leaves = 5
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printDetails(self):
        print(f"--------Details of {self.name}-------")
        print(f"Name:\t\t{self.name}")
        print(f"Age:\t\t{self.age}")
        print(f"Gender:\t\t{self.gender}")

class Manager(Employee):
    education = "MBA"
    def __init__(self, name, age, gender, team_size):
        super().__init__(name, age, gender)
        self.team_size = team_size

    def printDetails(self):
        super().printDetails()
        print(f"Education:\t{self.education}")
        print(f"Team Size:\t{self.team_size}")

e1 = Employee("Roshan", 22, "Male")
m1 = Manager("Roshani", 23, "Female", 10)
m1.printDetails()