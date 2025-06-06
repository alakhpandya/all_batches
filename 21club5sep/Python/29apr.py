"""
from functools import lru_cache
from time import time
# @lru_cache(maxsize=1000)
# print(help(time))

# n = int(input("Enter n: "))
n = 35
t1 = time()
# without cache
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, n+1):
    print(f"{i}.\t{fibonacci(i)}")
t2 = time()
# with cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, n+1):
    print(f"{i}.\t{fibonacci(i)}")
t3 = time()
print("Without Cache: ", t2 - t1)
print("With Cache: ", t3 - t2)
"""
# print(dir(list))
# print(dir(tuple))
# l1 = [1,2,3, 4.4, 5.5, 6.6, "Pizza", (4 - 2j)]
"""
from timeit import timeit

t_list = timeit(stmt='l1 = [1,2,3, 4.4, 5.5, 6.6, "Pizza", (4 - 2j)]', number=10000000)
t_tuple = timeit(stmt='t1 = (1,2,3, 4.4, 5.5, 6.6, "Pizza", (4 - 2j))', number=10000000)
print("Time to create 10 mn lists:", t_list)
print("Time to create 10 mn tuples:", t_tuple)
"""
"""
from sys import getsizeof

l1 = [1,2,3, 4.4, 5.5, 6.6, "Pizza", (4 - 2j)]
t1 = (1,2,3, 4.4, 5.5, 6.6, "Pizza", (4 - 2j))
print("size of list:", getsizeof(l1))
print("size of tuple:", getsizeof(t1))
"""
# import sys

# sys.getsizeof(l1)
# Datetime Module

import datetime

print(dir(datetime))

tomorrow = datetime.date(2022, 4, 30)
print(tomorrow)
print(type(tomorrow))
print(tomorrow.day)
print(tomorrow.month)
print(tomorrow.year)
viral = datetime.date(2022, 8, 22)
print(viral - tomorrow)

interval = datetime.timedelta(97)
print(viral + interval)
print(interval)

time1 = datetime.time(18, 30, 45)
print(time1)

sample_date_time = datetime.datetime(2022, 4, 29, 18, 30, 45)
print(sample_date_time)
print(sample_date_time.minute)

now = datetime.datetime.today()
print(now)

# Next Class: how to change format of date in datetime, random module