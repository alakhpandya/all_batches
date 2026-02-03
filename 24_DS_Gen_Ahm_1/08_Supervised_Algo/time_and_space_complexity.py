"""
cache = []
def fib(n):
    if n <= 1:
        cache.append(n)
        return n
    term = fib(n-1) + fib(n-2)
    cache.append(term)
    return term

n = int(input("Enter number of terms: "))

print("Fibonacci Series:", end=" ")
for i in range(n):
    print(i, "\t", fib(i), end="\n")
"""

# Memoization (Explicit)
"""
cache = {}
def fibonacci(num):
    if num in cache:
        return cache[num]
    if num==0:
        cache[0] = 0
        return 0
    elif num==1:
        cache[1] = 1
        return 1
    else:
        term = fibonacci(num-1) + fibonacci(num-2)
        cache[num] = term
        return term
    
num = int(input("Enter a number: "))
for i in range(num):
    # print(cache," ", end=" ")
    print(f"{i+1}.\t", fibonacci(i))
"""

# Implicit Memozation
from functools import lru_cache

@lru_cache(maxsize=5)       # decorators or wrapper functions
def fib(n):
    if n <= 0:
        return "Input should be positive"
    elif n == 1 or n == 2:
        return n - 1
    else:
        return fib(n - 1) + fib(n - 2)
    
userInput = int(input("Enter your number : "))
print(fib(userInput))