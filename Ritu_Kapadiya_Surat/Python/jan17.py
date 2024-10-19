"""
# import time

# print(dir(time))

from time import time
t = 0
for i in range(1000):
    t1 = time()
    # print(t1)
    # epoch: 1st Jan, 1970

    from functools import lru_cache
    @lru_cache
    def fib(n):
        if n == 0:
            return 0
        elif n==1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    # term = int(input("enter value of n: "))
    term = 10000
    for i in range(term+1):
        # print(f"term number {i} = {fib(i)}")
        fib(i)

    t2 = time()
    t += (t2 - t1)
print(t/1000)
"""
from timeit import timeit

list_time = timeit("l1 = [0,1,2,3,4,5,6,7,8,9,10]", number=100000000)
tuple_time = timeit("l1 = (0,1,2,3,4,5,6,7,8,9,10)", number=100000000)

print(list_time)
print(tuple_time)
print(list_time - tuple_time)

# Next Class: random module