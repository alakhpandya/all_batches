# Creating & using packages & libraries
# import apr8

# apr8.open_ac()
"""
a = input("Enter your state: ")
b = input("Enter capital of your state: ")
print(f"Ohh, you leave in {b} city of {a}?")
"""

'''
import important_functions as imp

# a = int(input("Enter a number to find its factorial: "))
# print(important_functions.fact(a))

a = int(input("Enter a number: "))
# print(important_functions.prime_check(a))
if imp.is_armstrong(a):
    print(f"{a} is Armstrong number")
else:
    print(f"{a} is not an Armstrong number")
'''
"""
from important_functions import prime_check as pc, is_armstrong as arm

# print(prime_check(153))
# print(is_armstrong(153))

# print("Name of this file (apr12):", __name__)
print("153 prime:", pc(153))
print("153 armstrong:", arm(153))
"""
"""
from important_functions import *

prime_check(153)
is_armstrong(153)
"""

# Won't work:
# import my_package
# my_package.library_1.func1()

# from my_package import library_1 as l1
# l1.func1()

# from my_package.library_1 import func1
# func1()