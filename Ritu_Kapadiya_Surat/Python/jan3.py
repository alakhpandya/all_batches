"""
from functools import lru_cache     # lru : least recently used

@lru_cache(maxsize=3)          # decorators = wrapper functions
def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

term = int(input("enter value of n: "))
# fib(n) #for print nth element of fib series
for i in range(term+1):
    print(f"term number {i} = {fib(i)}")
"""
# Passing collections to a function


# Types of arguments: postional, default, variable, keyword arguments
"""
def func1(a, b, c = 30, d = 40):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)

func1(10, 20, 25)
"""
# Variable length arguments
"""
def avg(a, *args):
    # pass
    print("a =", a)
    print(args)
    return sum(args, a)/(len(args)+1)

print(avg(10, 20, 30, 40, 50))
# avg()
"""

def percentage(**kwargs):
    print(kwargs)

percentage(Maths = 88, Computers = 99, Physics = 94)