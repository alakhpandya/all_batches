"""
class Parent1():
    vehicle = "car"

class Parent2():
    profession = "grocery store"
    vehicle = "activa"

class Child1(Parent1, Parent2):
    pass

class Child2(Parent2, Parent1):
    pass

class GrandChild(Child1):
    pass

c1 = Child1()
print(c1.vehicle)
c2 = Child2()
print(c2.vehicle)
gc1 = GrandChild()
print(gc1.vehicle)
"""