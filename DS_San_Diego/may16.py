# Modules & Packages in Python
# OR
# Organizing your code in modules & packages

"""
import important_functions

print(important_functions.avg(15, 20))
"""
"""
import important_functions as imp

print(imp.primeCheck(1003)) 
print(imp.primeCheck(641))
"""
"""
import speech_recognition as sr
import numpy as np
import pandas as pd
"""
"""
from important_functions import triangleTest, armstrong

print(triangleTest(45, 60, 75))
print(armstrong(371))
"""
"""
from important_functions import primeCheck as pc, avg, triangleTest as tt

print(pc(29))
print(avg(20, 30, 40))
"""
"""
from important_functions import *
from test_module import *

# print(primeCheck(641))
avg(5, 10)
"""

# Packages: A folder that contains multiple modules