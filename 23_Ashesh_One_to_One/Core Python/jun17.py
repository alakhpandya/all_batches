# Organizing our code in modules and packages
"""
import important_functions

print(important_functions.avg(12, 15, 20))
"""
# changing name of a module while importing
"""
import important_functions as imp

print(imp.avg(11, 14, 19))
"""
# importing speicfic functions from a module
"""
from important_functions import factorial, armstrongCheck

print(factorial(6))
print(armstrongCheck(150))
"""
"""
from important_functions import factorial as fc, armstrongCheck as ac

print(fc(5))
print(ac(371))
"""
# importing all the functions of a module
"""
from important_functions import *

print(factorial(7))
print(avg(10,20,30))
print(armstrongCheck(370))
print(primeCheck(97))
"""
"""
import important_functions as imp
# from important_functions import primeCheck

print(imp.primeCheck(11))
# print(primeCheck(11))
print("Name of this program:", __name__)
"""
# Package
"""
# Wrong way:
import myPackage

myPackage.myModule.func1()
"""
# from myPackage import myModule
"""
from myPackage import myModule as mm

mm.func1()
"""
"""
from myPackage.myModule import func1 as fc

fc()
"""
"""
from myPackage.subPackage import subModule as sm

sm.subfunc1()
"""
"""
from myPackage.subPackage.subModule import subfunc1 as sf1

sf1()
"""
# Tomorrow's class: some useful built in modules, External libraries

# Next week: Object Oriented Programming in Python