# __name__
"""
# import important_functions as imp
# print(imp.primeCheck(1003))

def anyFunc():
    print("Hi, I am anyFunc from may17!")

from important_functions import primeCheck
if __name__ == "__main__":
    # print("name of the file i am running:", __name__)
    print(primeCheck(1003))
"""

# Packages: A folder that may have 1 or more modules but must have a file named "__init__.py"
# we cannot import a package
"""
import myPackage

myPackage.myModule.myFunc()
"""
"""
from myPackage import myModule
from myPackage import myModule as mm

myModule.myFunc()
"""

# from myPackage.myModule import myFunc as f1
# f1()

# Create a subPackage inside myPackage and also create a subModule in subPackage. Write a function 'subFunc' in the subModule and try to call it in may17.py

from myPackage.subPackage import subModule
subModule.subFunc()

from myPackage.subPackage import subModule as sm
sm.subFunc()

from myPackage.subPackage.subModule import subFunc
subFunc()

from myPackage.subPackage.subModule import subFunc as sf
sf()

import pandas as pd