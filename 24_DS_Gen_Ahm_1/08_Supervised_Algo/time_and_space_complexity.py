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
from time import time

# print(time())
num = int(input("Enter a number: "))

t1 = time()
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
    
for i in range(num):
    # print(cache," ", end=" ")
    print(f"{i+1}.\t", fibonacci(i))
t2 = time()
print("Actual Execution Time =", t2 - t1)
"""
# Implicit Memozation
"""
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
"""

# p-1: 753 computations
# p-2: 538 computations

# Time Complexity (Big O): How efficient our algorithm performs as the size of the input tends to infinite.
"""
O(1)        Constant
O(log n)    Logarithmic
O(n)        Linear
O(nlog n)   Linearithmic
O(n^2)      Quadratic
O(n^3)      Cubic
O(2^n)      Exponential
O(n!)       Factorial
"""

def constant(n):
    print("Hello World!")   # O(1)
    a = 98724               # O(1)
    b = 91                  # O(1)
    print(a ** b)           # O(1)
    for i in range(1000):
        a+b                 # O(1000)  

    # Entire Algo Time Complexity = O(1000) = constant = O(1) 

# constant(100000)

# Linear
def linear(n):
    print("Hello World!")   # O(1)
    a = 98724               # O(1)
    b = 91                  # O(1)
    c = a ** b              # O(1)
    for i in range(n):
        print(a)            # O(n)
        print(b)            # O(n)
        print(c)            # O(n)

        # Total             # O(3n + 4) = linear = O(n)

# linear(100000000000000000)

# Quadratic

def quadratic(n):
    k = 1                       # O(1)
    print("Hello World!")       # O(1)
    for i in range(n):          
        print(i)                # O(n)
        for j in range(n):
            print("\t", k)      # O(n^2)
            k += 1              # O(n^2)

# quadratic(6)

def cubic(n):
    a = 1                               # O(1)
    b = 5
    for i in range(15):
        c = a + b                       # O(15)
    for i in range(n):
        print(i)                        # O(n)
        for j in range(n):      
            print("\t", j)              # O(n^2)
            for k in range(n):
                print("\t\t", a)        # O(n^3)
                a += 1                  # O(n^3)

                # Total = O(2*n^3 + n^2 + n + 16) = cubic = O(n^3)

# cubic(4)

# logarithmic
def logarithmic(n):
    i = 1               # O(1)
    n = n // 2          # O(1)
    while n > 0:        # n = 8, 4, 2, 1, 0
        print(i)        # O(log2 (n))
        i += 1
        n = n//2    

# logarithmic(160)        # log2 (160) = 7.32 = 7


# Linearithmic
def linearithmic(n):
    pass


# Exponential
def exponential(n):
    # fibonacci sequence program that we did without memoization
    pass

# Practicing recursion:
# What will be the output of the following code?
def bar(x, y):
    if y == 0:
        return 0
    return (x + bar(x, y-1))

def foo(x, y):
    if y == 0:
        return 1
    return bar(x, foo(x, y-1))

# print(foo(3, 5))


# Factorial
def factorial(n):
    if n <= 0:
        print("*", end=",")          # O(1)
        return
    for i in range(n):
        factorial(n-1)      # O(n)

# factorial(15)

# Space Complexity:

def countDown(n):
    print(n)
    if n == 0:
        return 1
    return countDown(n-1) * 1

# Space Complexity: O(n)

# countDown(5)

# Function - 1

def twoLoops(n):
    for i in range(n):
        pass
    for j in range(n):
        pass

# Time complexity = O(2n) = linear = O(n)

# Function - 2

def twoInputs(a, b):
    for i in range(a):
        pass             
    for j in range(b):
        pass             
        
# O(a + b) or
# O(n)

# Function - 3

def twoInputs(a, b):
    for i in range(a):
        pass
        for j in range(b):
            pass

# O(a * b) or O(n^2)