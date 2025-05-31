from functools import lru_cache

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def geometric_progression(a, r, n):
    if n == 1:
        return a
    else:
        return r * geometric_progression(a, r, n-1)


def arithmetic_progression(a, d, n):
    if n == 1:
        return a
    else:
        return d + arithmetic_progression(a, d, n-1)


@lru_cache(maxsize=3)
def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print("Name of recursion module:", __name__)
if __name__ == "__main__":
    a = int(input())
    d = int(input())
    n = int(input())

    print(fact(a))
    print(AP(a, d, n))
    print(GP(a, d, n))
    print(fib(a))