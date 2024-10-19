# Some important built-in functions: sum(), zip(), map(), round(), filter()
# sum()
"""
numbers = (2,3,4,5,1)
print(sum(numbers))
print(sum(numbers, 10))
"""
# zip()
"""
n1 = ["a", "b", "c"]
n2 = (1, 2, 3)
n3 = ["A", "B", "C"]
print(set(zip(n1, n2, n3)))

d1 = {"A":1, "B":2, "C":3}
d2 = {10:"x", 20:"y", 30:"z"}
print(set(zip(d1, d2)))
print(set(zip(d1, n2)))
"""
# map()
"""
def cube(n):
    return n ** 3

numbers = [2, 5, 6, 9, 8, 12, 11, 4, 15]
# cubes = []
# for x in numbers:
#     cubes.append(cube(x))
print(tuple(map(cube, numbers)))
# for result in map(cube, numbers):
#     print(result)
"""
"""
cities = ["Ahmedabad", "Manali", "Dibrugarh", "Ooty", "Maldives"]
temperatures_in_c = [42, 12, 25, 18, 27]
temperatures_in_f = list(map(lambda celcius : (celcius * 9/5) + 32, temperatures_in_c))
print(temperatures_in_f)
"""
"""
x2 - 2x - 1
x2 - 3x + 9
4x2 + 9x - 4
39x2 + 18x - 2000
"""
"""
def quadratic(coefficients):
    a, b, c = coefficients
    return ((-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a)) if b**2 - 4*a*c >= 0 and a != 0 else None
equations = [
    (1, -2, -1),
    (1, -3, 9),
    (4, 9, -4),
    (39, 18, -2000)
]
roots = list(map(quadratic, equations))
print(roots)
"""
# round()
"""
print(2500/365)
print(round(2500/365, 3))
print(round(2500/365, 2))
"""
# filter()
def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

numbers = [11, 23, 24, 27, 29, 32, 33, 35, 37, 39, 44, 49, 53, 57, 89, 92, 91, 97, 99]
print(list(filter(prime, numbers)))
"""
False for Python:
False, 0, 0.0, "", [], (), {}, set()
Everything else is True.
"""
# Next Class: Example of temperatures from different ocean bouys with filter function, reduce()