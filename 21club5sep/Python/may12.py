"""
import important_functions

print(important_functions.factorial(5))
"""
"""
import important_functions as imp

print(imp.factorial(6))
"""
"""
import speech_recognition as sr
import numpy as np
import pandas as pd
"""
"""
from important_functions import factorial, prime

print(factorial(12))
print(prime(1717171))
"""
"""
from important_functions import factorial as fc, prime as pm

print(fc(8))
print(pm(23))
"""
"""
from important_functions import *

print(average(factorial(9), factorial(8)))
"""
"""
import important_functions as imp

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# print(average(factorial(a), factorial(b)))
print("may12.py:", __name__)
print("module's name: ", end ="") 
imp.printName()
"""
# will not work:
"""
import myPackage

myPackage.myModule.func1()
"""
"""
from myPackage import myModule

myModule.func1()
"""
"""
from myPackage.myModule import func1 as fc

fc()
"""
"""
import myPackage.subPackage.subModule as sm

sm.subFunc()
"""
"""
from myPackage.subPackage.subModule import subFunc

subFunc()
"""

# Next Class: External libraries