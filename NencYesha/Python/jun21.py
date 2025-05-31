def func1():
    """This will do ______ things"""
    pass

# Some useful built-in function

# sum
"""
l1 = [12, 13, 15, 21, 32, -50, 20]
print(sum(l1))
"""
# abs
"""
x = -5
print(abs(x))
y = 10
print(abs(y))
"""
# any & all
"""
l1 = [3 < 5, 4 >= 6, 12 > 10, 11 < 8]
print(l1)
print(any(l1))
print(all(l1))
"""
# chr - returns character corresponding to the ascii code
'''
s = """
print(chr(98))
print(chr(66))
print(s.upper())
"""
'''
# eval
"""
s = 'print("Hello World!")'
print(s)
eval(s)
"""

# round
"""
a = 25.3
print(round(a))
b = 33.8
print(round(b))
pi = 3.141596
print(round(pi, 2))
"""

# zip
"""
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
l3 = ["p", "q", "r"]
a = zip(l1, l2, l3)
print(list(a))
"""

# lambda functions
'''
def python():
    print("""Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.""")
'''
'''
python = lambda : print("""Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.""")

python()
'''
"""
def power5(x):
    return x ** 5

power5 = lambda x : x ** 5
y = power5(4)
print(y)
"""
"""
def avg(a, b):
    return (a + b)/2

avg = lambda a, b : (a + b)/2
print(avg(10, 20))
"""

# We can convert a function to a lambda function only if it is a 'one-liner' function

# map
"""
from sys import getsizeof

def factorial(a):
    f = 1
    for i in range(1, a+1):
        f = f * i
    return f

# print(factorial(5))
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

num_fact = []
for i in num:
    num_fact.append(factorial(i))

# print(num_fact)
print(getsizeof(num_fact))

num_fact_object = map(factorial, num)
# print(num_fact_object)
print(getsizeof(num_fact_object))
"""

# filter
'''
def avg(n):
    return sum(n)/len(n)

temperatures = [-20, -18, -13, -15, 0, 4, -12, -15, -16, 3, -2, 0, 5]
avg_temp = round(avg(temperatures))
# print(avg_temp)

def aboveAvgTemp(x):
    return x > avg_temp

# print(aboveAvgTemp(0))
# Write a program that creates a new list of all temperature points which are above avg_temp using 'aboveAvgTemp()' function

# Your code goes here
"""
high_temp_points = []
for i in temperatures:  # i = -20, -18, -13, -15, 0, 4, -12, -15, -16, 3, -2, 0, 5
    if aboveAvgTemp(i):
        high_temp_points.append(i)
"""

high_temp_points = list(filter(aboveAvgTemp, temperatures))
print(high_temp_points)
'''

# reduce
'''
from functools import reduce

transactions = [250, -25, -500, 100, -300, 650, 775, -200, -150, 350]
"""
sum = 0
for i in transactions:
    sum = sum + abs(i)
print(sum)
"""

def absoluteAddition(a, b):
    return abs(a) + abs(b)
"""
sum = absoluteAddition(transactions[0], transactions[1])
for i in range(2, len(transactions)):
    sum = absoluteAddition(sum, transactions[i])
"""
sum = reduce(absoluteAddition, transactions)
print(sum)
'''

# Organizing our code in modules & packages