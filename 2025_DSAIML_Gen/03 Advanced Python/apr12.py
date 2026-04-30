# Packages & Libraries
"""
# import important_functions
import important_functions as imp

a = int(input("a = "))
# print("Prime check:", important_functions.prime_check(a))
print("Prime check:", imp.prime_check(a))
"""
"""
from important_functions import prime_check as pc, is_perfect

a = int(input("a = "))
# print(prime_check(a))
print("Prime Check:", pc(a))
print("Perfect Check:", is_perfect(a))
"""

from important_functions import *

a = int(input("a = "))
print("Prime Check:", prime_check(a))
print("Perfect Check:", is_perfect(a))


# import apr24

# print("Name of current file is:", __name__)