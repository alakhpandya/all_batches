# Implicit Memoization

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


t = int(input("Enter t: "))
print(f"Fibonacci sequence till {t}th term are:")
print(fibonacci(40))
print("Term No\tValue")
for x in range(1, t+1):
    print(f"{x}\t{fibonacci(x)}")
