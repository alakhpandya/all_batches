"""
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 1:
        cache[1] = 0
        return 0
    elif n == 2:
        cache[2] = 1
        return 1
    else:
        term = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = term
        return term
"""
from functools import lru_cache

@lru_cache          # decorators/wrapper function
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("n ="))
for i in range(n):
    print(i+1, ". ", fibonacci(i+1))


# What will be the output of the following code? 
# Solve it without running the code on the computer, use note-pen instead.

def bar(x, y):
    if y == 0:
        return 0
    return (x + bar(x, y-1))

def foo(x, y):
    if y == 0:
        return 1
    return bar(x, foo(x, y-1))

print(foo(3, 5))