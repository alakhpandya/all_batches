# Recursive Functions

"""
Arithmetic Progression (AP):
first term (a) = 12
common difference (d) = 5
AP: 12, 17, 22, 27, ....., (n-1), n
nth term = (n-1)th term + d

5th term = 4th term + d
4th term = 3rd term + d
3rd term = 2nd term + d
2nd term = 1st term + d

1st term = a
"""
"""
def rec_ap(a, d, n):
    print(f"New call for n={n}")
    if n == 1:
        print("n=1, ret:", a)
        return a
    else:
        ret = rec_ap(a, d, n-1) + d
        print(f"n={n}, ret:", ret)
        return ret
    
print(rec_ap(5, 3, 4))
"""
"""
def incrementor(x, inc):
    return x + inc

# print(incrementor(5, 17))
incrementor(2, 5) + incrementor(3, 2)
"""
# Final code for AP:
def rec_ap(a, d, n):
    if n == 1:
        return a
    else:
        return rec_ap(a, d, (n-1)) + d

# Geometric Progression
"""
first term (a) = 3
common ratio (r) = 4
gp: 3, 12, 48, 192, ... (n-1), n
nth term = (n-1)th term * r
1st term = a
"""
def rec_gp(a, r, n):
    if n == 1:
        return a
    else:
        return rec_gp(a, r, n-1) * r
    
# print(rec_gp(3, 4, 4))

# Write a recursive function to find nth term of Fibonacci Sequence
# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

# Memoization (Explicit)
terms = {}      # cache
def fib(n):
    if n in terms:
        return terms[n]
    if n == 1:
        terms[n] = 1
        return 1
    elif n == 2:
        terms[n] = 1
        return 1
    else:
        value = fib(n-1) + fib(n-2)
        terms[n] = value
        return value

# Implicit Memoization
from functools import lru_cache     # decorator
@lru_cache(maxsize=128)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


n = int(input("n = "))
for i in range(1, n+1):
    print(f"{i}.\t{fib(i)}")
# print(terms)


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