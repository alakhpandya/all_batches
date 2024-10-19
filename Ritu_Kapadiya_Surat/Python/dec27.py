"""
Recursive function to find nth term of a GP
a: 3
r: 4
n: 5
GP: 3, 12, 48, 192, 768
"""
# Memoization - Explicit
"""
term = int(input("enter value of n: "))
cache_memory = []                   # c = [] 
def fib(n):
    if n < len(cache_memory):       # n=4, false; n=3, false
        return cache_memory[n]
    if n == 0:                      # false
        cache_memory.append(0)
        return 0
    elif n==1:                      # false
        cache_memory.append(1)
        return 1
    else:                           # true
        t = fib(n-1) + fib(n-2)
        cache_memory.append(t)      # c = []
        return t

for i in range(term+1):
    print(f"term number {i} = {fib(i)}")    # i =4
"""
# Next Class: Implicit Memoization