# Docstrings
'''
import random

def average(a, b, c):
    # """This function returns the average of 3 integers"""
    print("This is good function")
    return (a + b + c)/3
'''
"""
def func1():
    '''This is trial function'''
    pass

def func2():
    # This is another trial function
    pass

# print(average(4,5,6))
print(average.__doc__)
print(func1.__doc__)
print(func2.__doc__)
"""
# function returning condition
"""
def greater5(n):
    return n > 5

# myList = []
# for i in range(1, 101):
#     myList.append(i)
myList = [i for i in range(1, 11)]
# print(myList)
for x in myList:
    if greater5(x):
        print(x)
"""
# function returning another function/built in function
"""
def average_of_factorial(a, b, c):
    def fact(n):
        f = 1
        for x in range(1, n+1):
            f *= x
        return f
    return (fact(a)+fact(b)+fact(c))/3

def secret():
    return average_of_factorial

def topSecret():
    return print

secret()(3,4,5)
# average_of_factorial(3,4,5)
topSecret()("Mihir is a good boy")
"""
# function returning a class
"""
def func1():
    return int

print(func1()(15.4))
"""
# Passing function as an argument to another function
"""
def fact(n):
    f = 1
    for x in range(1, n+1):
        f *= x
    return f

def avg(a, b, c):
    return (a + b + c)/3

print(avg(fact(3), fact(4), fact(5)))
"""
# Nested functions
"""
def average_of_factorial(a, b, c):
    def fact(n):
        f = 1
        for x in range(1, n+1):
            f *= x
        return f
    return (fact(a)+fact(b)+fact(c))/3
"""
