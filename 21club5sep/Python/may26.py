# Inheritance
"""
class Father:
    hobby = "cooking"
    education = "Master's"
    profession = "Lawyer"

    def printDetails(self):
        print(f"Hobby:", self.hobby)

class Mother:
    profession = "Doctor"
    family_members = 4
    hobby = "Swimming"

class Son(Mother, Father):
    hobby = "Cricket"

    def printDetails(self):
        pass

class Daughter(Father, Mother):
    # profession = "Student"
    profession = "Doctor"
    pass

s1 = Son()
s1.hobby = "Gardening"
print(s1.hobby)
s2 = Son()
print(s2.hobby)
print(s2.education)

d1 = Daughter()
print(d1.education)
print(d1.hobby)
print(d1.profession)
print(d1.family_members)
"""
# print(d1.salary)

# Types of inheritance
"""
Simple/Single Level
    Parent Class --> Child Class

Multi Level Inheritance
    Parent Class --> Child Class --> Grand Child Class --> .....

Hierarchical Inheritance
                 --> Child Class 1
    Parent Class --> Child Class 2
                 --> Child Class 3

Multiple Inheritance
    Parent Class 1
                    --> Child Class
    Parent Class 2

Hybrid Inheritance
    Parent Class 1
                    --> Child Class --> Grand Child Class
    Parent Class 2

                 --> Child Class 1 --> Grand Child Class
    Parent Class --> Child Class 2
                 --> Child Class 3
"""
"""
class P1():
    hobby = "cooking"
    education = "Master's"
    profession = "Lawyer"

class P2():
    profession = "Doctor"
    family_members = 4
    hobby = "Swimming"

class Derived1(P1, P2):
    pass

class Derived2(P2, P1):
    hobby = "Singing"

class Final(Derived1, Derived2):
    pass

f1 = Final()
print(f1.hobby)
"""
