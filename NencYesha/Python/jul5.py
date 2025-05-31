"""
import math
import cmath

# l = [1,2,3,4,5,6,7,8]
# print(sum(l))
# abs()
t = 45
t = math.radians(t)
print(t)
# print(dir(math))
print(math.tan(t))
"""
"""
import important_function

print(important_function.factorial(6))
"""

"""
import important_function as imp

print(imp.avg([23, 22, 45, 33, 44, 67]))
"""
"""
from important_function import palindrom, avg, sum_of_squares

print(palindrom("malayalam"))
"""
"""
from important_function import palindrom as pal, avg, sum_of_squares as sos

print(pal("manam"))
print(avg([23, 22, 45, 33, 44, 67]))
print(sos(5,7))
"""
"""
from important_function import *

print(evenCapitalize("Hello Nancy & Yesha!"))
"""
"""
from math import tan, radians

print(tan(radians(45)))
"""

# Packages

# Wrong way:
"""
import myPackage
myPackage.myModule.myFunc()
"""
# Correct ways
"""
from myPackage import myModule
myModule.myFunc()
"""
"""
from myPackage import myModule as mm
mm.myFunc()
"""
"""
from myPackage.myModule import myFunc
myFunc()
"""
"""
from myPackage.myModule import myFunc as fn
fn()
"""

"""
Create another package inside myPackage and call it 'subPackage'. Create a module inside subPackage and name it 'subModule'. Finally, create a function with name 'subFunc()' inside that sumModule and call it in your main file using different ways.
"""
# Next Class: Installing & Importing external packages/mdoules, Some useful built in modules of python