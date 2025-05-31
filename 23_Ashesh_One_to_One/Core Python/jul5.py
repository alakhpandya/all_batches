# 4 pillars of OOP: Inheritance, Polymorphism, Abstraction, Encapsulation
# Inheritance:
# Single level/Single/Simple inheritance
# Multi level inheritance
"""
class Father():
    vehicle = "Motorbike"

class Son(Father):
    education = "Bachelors"
    # vehicle = "Skateboard"

    def displayDetails(self):
        print("Education:", self.education)
        print("Vehicle:", self.vehicle)

class GrandSon(Son):
    pass

s1 = Son()
s1.vehicle = "Bicycle"
print(s1.vehicle)
print(s1.education)
s2 = Son()
print(s2.vehicle)

# MRO: Method Resolution Order

g1 = GrandSon()
print(g1.education)
print(g1.vehicle)
# print(g1.hobby)
"""
# Hierarchical inheritance
"""
class Manager():
    education = "MBA"

class SalesManager(Manager):
    pass

class ProjectManger(Manager):
    education = "BE Computers"

class ProductManager(Manager):
    pass
"""
# Multiple Inheritance
"""
class Parent1():
    education = "BE"

class Parent2():
    vehicle = "Car"
    education = "MBBS"

class ChildClass1(Parent1, Parent2):
    pass

class ChildClass2(Parent2, Parent1):
    pass

class ChildClass3(ChildClass1, ChildClass2):
    pass

d1 = ChildClass1()
print(d1.education)
print(d1.vehicle)

c2 = ChildClass2()
print(c2.education)
print(c2.vehicle)

c3 = ChildClass3()
print(c3.education)
"""
# Hybrid Inheritance
"""
        --> C1
Parent  --> C2
        --> C3 --> GC3
        --> C4
"""