# Some useful builtin functions
import math

# sum
"""
n = [5, 8, 11, 13.4, 15, 20, 34]
print(sum(n))
print(sum(n, 10))
"""
# eval
"""
n = [5, 8, 11, 13.4, 15, 20, 34]
e = "sum(n)"
print(eval(e))
"""
# abs
"""
a = float(input("Enter any number: "))
print(f"Absolute of a = {abs(a)}")
"""
# round
"""
a = float(input("Enter any number: "))
print(f"rounded off a = {round(a)}")
print(f"rounded off a = {round(a, 0)}")
print(f"rounded off a after 2 decimal places = {round(a, 2)}")
print(f"rounded off a after 2 decimal places = {round(a, -2)}")
"""
# floor: int & ceiling
"""
a = float(input("Enter any number: "))
print(f"floored a = {int(a)}")
print(f"floored a = {math.floor(a)}")
print(f"ceiling of a = {math.ceil(a)}")
"""
# pow
"""
a = 5
b = 3
print(pow(a, b))
"""
# zip
"""
l1 = [1, 2, 3]
l2 = ("a", "b", "c")
l3 = ["A", "B", "C"]
# print(list(zip(l1, l2, l3)))
for triplet in zip(l1, l2, l3):
    print(triplet)
"""
# map
"""
def root(equation):
    a, b, c = equation
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return None
    root1 = (-b + d ** 0.5)/(2*a)
    root2 = (-b - d ** 0.5)/(2*a)
    return (root1, root2)

data = [
    (2, 5, 3),
    (1, 2, 1),
    (4, 3, 1),
    (2, 18, 9)
]
roots = list(map(root, data))
print(roots)
"""
"""
def cube(n):
    return n ** 3

n = [5, 8, 11, 13.4, 15, 20, 34]
cubes = list(map(cube, n))
print(n)
print(cubes)
"""
# filter
"""
def above_average(x):
    return x > average

sensor_data = [0.5, 12, 6, -3, 18, 57, 23, 104, 13, 20, 98, 110]
average = sum(sensor_data)/len(sensor_data)
print("Average Temperature: ", average)
# unsafe_data = list(map(above_average, sensor_data))
unsafe_data = list(filter(above_average, sensor_data))
print(unsafe_data)
"""
# reduce
"""
import functools

def multiply(a, b):
    return a * b

n = [5, 8, 11, 13.4, 15, 20, 34]
mul = functools.reduce(multiply, n)
print(mul)

# n = [5, 8, 11, 13.4, 15, 20, 34]
# mul = 1
# for i in range(len(n)):
#     mul = mul * n[i]
# print(mul)
"""

# Next Class: lambda functions