"""
Write a function that returns 'nth term' of an arithmetic progression with 'a' as its first term and having common difference 'd'

What is an AP?
Let a (first term) = 11,
d (common difference) = 6
ap: 11, 17, 23, 29, 35,...
n = 5
5th term: 35

nth term of ap: a + (n-1)*d
"""
def ap(a, d, n):
    return a + (n - 1)*d

# print(ap(11, 6, 5))

# 6th term = 5th term + d
# 5th term = 4th term + d
# .....................
# .....................
# 1st term = a

# nth term = (n-1)th term + d

def rec_ap(a, d, n):
    if n == 1:
        return a
    else:
        return rec_ap(a, d, n-1) + d
    
# print(rec_ap(11, 6, 5))

"""
Write a function that returns 'nth term' of a geometric progression with 'a' as its first term and having common difference 'd'

What is a GP?
Let a (first term) = 3,
r (common ratio) = 4
gp : 3, 12, 48, 192, 768, ...
n = 5
5th term: 768

nth term of ap: a * r**(n-1)

print(ap(11, 6, 5))

1st term = a
2nd term = 1st term * r
3rd term = 2nd term * r
........................
nth term = (n-1)th term * r
"""

def rec_gp(a, r, n):
    if n == 1:
        return a
    else:
        return rec_gp(a, r, n-1) * r
    
# print(rec_gp(3, 4, 5))

"""
Write a Python function that will return nth term of fibonacci sequence

Fibonacci Sequence:
1, 1, 2, 3, 5, 8, 13, 21, 34, ...

fibo(7) -> 13
fibo(9) -> 34
"""
"""
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
"""

# Memoization - Explicit
"""
cache = {}
def fibo(n):
    if n in cache:
        return cache[n]
    if n == 1:
        cache[1] = 1
        return 1
    elif n == 2:
        cache[2] = 1
        return 1
    else:
        term = fibo(n-1) + fibo(n-2)
        cache[n] = term
        return term

n = int(input("n : "))
for i in range(1, n+1):
    print(f"{i}.", fibo(i))
    # fibo(i)
# print(cache)
"""

# Implicit Memoization
"""
from functools import lru_cache     # decorators = wrapper functions

@lru_cache
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input("n : "))
for i in range(1, n+1):
    print(f"{i}.", fibo(i))
"""

# Predict the output of the following code WITHOUT EXECUTING IT.

def bar(x, y):
    if y == 0:
        return 0
    return (x + bar(x, y-1))

def foo(x, y):
    if y == 0:
        return 1
    return bar(x, foo(x, y-1))

print(foo(3, 5))