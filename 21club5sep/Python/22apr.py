# Example:
"""
from statistics import mean

fuel_readings = [23, 5, 12, 10, 4, -1, 6, 45, 30]
avg = mean(fuel_readings)
print(avg)
print(list(filter(lambda x : x < avg, fuel_readings)))
print(list(filter(lambda x : x > avg, fuel_readings)))
"""
# reduce()
"""
from functools import reduce

def product(a, b):
    return a * b
numbers = [1,3,5,7,9,11,13,15,17,19]
print(reduce(product, numbers))
"""
# p = 1
# for i in numbers:
#     p *= i
# print(p)
"""
let 
f = product
f(f(f(f(1, 3), 5), 7), 9)
"""
# Recursive functions
"""
recursive definition of factorial:
recursive step:
n! = n * (n-1)!
non-recursive step:
0! = 1
"""
"""
def recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n * recursive_fact(n-1)

print(recursive_fact(5))
"""
# (e^xlogx) + sinx = 0
"""


y = 1       # +ve
x = 0.1     # -ve
root = lambda x : (e ** x) * log10(x) + sin(x)

z = (x + y)/2   # +ve
print(root(z))

y = z           # +ve
z = (x + y)/2   # -ve
print(root(z))

x = z           # -ve
z = (x + y)/2   # -ve
print(root(z))

x = z           # -ve
z = (x + y)/2   # 
print(root(z))
"""
from math import e, log10, sin

def bisect(x, y, root):
    z = (x + y)/2
    if root(x) > root(y):
        x, y = y, x
    if root(z) < 0:
        return bisect(z, y, root)
    elif abs(round(root(z), 10)) == 0:
        return z
    else:
        return bisect(x, z, root)

equation = lambda n : (e ** n) * log10(n) + sin(n)
while True:
    print("Enter two initial guess:")
    a = float(input())
    b = float(input())
    if equation(a) * equation(b) < 0:
        print("root approximated to 10 decimal places =", bisect(1, 0.1, equation))
        break
    else:
        print("Wrong choices of initial guesses, please try again...")
    loop = input("Press 'q' to quit or any other key to continue").lower()
    if loop == "q":
        break
# print(equation(0.5093505859374999))
# 0.5093368462432408