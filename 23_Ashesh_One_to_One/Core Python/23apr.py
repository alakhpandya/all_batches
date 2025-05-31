# strings: Ordered and Immutable collections of characters
"""
s1 =        "Python is fun @ Royal with all the faculties."
# index nos: 0123456789...................................
print(s1[16])
# print(s1[160])
print(len(s1))
print(s1)
print(type(s1))
a = 15
b = str(a)
print("a =", a, type(a))
print("b =", b, type(b))
print(len(b))
print(len(str(a)))
# slicing
s2 = s1[3 : 33]
print(s1)
print(s2)
print(s1[3 : 160])
print(s1[3 : ])
print(s1[ : 30])
print(s1[ : ])
print(s1[3 : 33 : 2])
print(s1[3 : 33 : 5])
print(s1[3 : 33 : 155])
print(s1[3 : 33 : ])
"""
# Negative indices
"""
s1 =        "Python is fun @ Royal with all the faculties."
# -ve index: ....................................987654321
# index nos: 0123456789...................................
print(s1[8])
print(s1[-5])
print(s1[0])
# print(s1[-55])
print(s1[-26 : -5])
print(s1[-2 : -11 : -1])
print(s1[33 : 3 : -2])
print(s1[3 : -3])
"""
s1 =        "Python is fun @ ROYAL with all the faculties."
# index nos: 0123456789...................................
# -ve index: ....................................987654321
# s1[10] = "F"
# string methods
len(s1)
# s1.len()
# Magical Mehtods/Dunder Methods
"""
s2 = "Especially early in the morning."
print(s1 + s2)
s1.__add__(s2)
s3 = 10
s4 = 20
print(s3 + s4)
s3.__add__(s4)
"""
# Case related methods
"""
print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.swapcase())
print(s1.casefold())
print(s1)
s2 = "ϐ"
print(s2)
print(s2.lower())
print(s2.casefold())
"""
# Allignment-related methods
"""
print(s1.center(100))
print(s1.center(51, "-"))
print(s1.ljust(60, "#"))
print(s1.rjust(60, "#"))
"""
print(s1.count("t"))
print(s1.count("t", 15))
print(s1.count("t", 15, 30))
print(s1.count("t", 15, 20))
print(s1.count("z"))
print(s1.count("the"))
print(s1.count("the", 10, 30))

# Next class: methods starting from 'e'
