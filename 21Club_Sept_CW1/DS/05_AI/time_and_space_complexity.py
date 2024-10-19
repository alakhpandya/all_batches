"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
ask = int(input("Enter the number of terms you want to print: "))
for i in range(ask):
    print(f"{i+1}.\t{fibonacci(i)}")
"""

# Recursive Definition of Fibonacci Numbers:
"""
Recursive Step:
nth fibonacci number = (n-1)th fibonacci number + (n-2)th fibonacci number
Non-recursive Step (Basis Step):
1st fibonacci number = 0
2nd fibonacci number = 1

if:
    non-recursive step
elif:
    non-recursive step
else:
    recursive step
"""
"""
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
ask = int(input("Enter the number of terms you want to print: "))
for i in range(1, ask+1):
    print(f"{i}.\t{fib(i)}")
"""

cache = {}
def fibo(n):
  if n in cache:
    return cache[n]
  if n == 1:
    cache[n] = 0
    return 0
  elif n == 2:
    cache[n] = 1
    return 1
  else:
    term = fibo(n - 1) + fibo(n - 2)
    cache[n] = term
    return term

ask = int(input("Enter the number of terms you want to print: "))
for i in range(1, ask+1):
    print(fibo(i))