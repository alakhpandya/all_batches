# Memoization

# cache = {1 : 1, 2 : 1, 3 : 2, 4 : 3, 5 : 5, 6: 8, 7 : 13}
# print(cache[6])
"""
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 1:
        cache[n] = 1
        return 1
    elif n == 2:
        cache[n] = 1
        return 1
    else:
        term = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = term
        return term

n = int(input("Enter n: "))
for i in range(1, n+1):
    print(f"{i}.\t{fibonacci(i)}")
"""
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter n: "))
for i in range(1, n+1):
    print(f"{i}.\t{fibonacci(i)}")


# Next class: Organizing our code in modules and packages, difference between tuples and lists