"""
from math import floor, ceil, modf
def func1():
    A = -650
    div = A / 200
    # print(div)        -3.25
    r = abs(modf(div)[0])
    print(r)
    if A < 0:
        if r >= 0.5:
            return floor(div)
        else:
            return ceil(div)
    else:
        if r >= 0.5:
            return ceil(A/200)
        else:
            return floor(A/200)
        
print(func1())
"""
# a = float("inf")
# print(10000000000000000000000000000000 < a)

# myList = [x for x in range(1, 101)]
# squareList = [x**2 for x in range(1, 101)]
# evenList = [x for x in range(1, 101) if x % 2 == 0]
# inputList = [int(input(f"Enter no-{i}: ")) for i in range(5)]
# matrix3x3 = [[float(input(f"a[{j}][{i}]")) for i in range(3)] for j in range(3)]

# print(myList)
# print(squareList)
# print(evenList)
# print(inputList)
# print(matrix3x3)

# num = {x : "Hello" for x in range(1, 6)}
# print(num)

# inputDict = {x : input(f"value-{x}: ") for x in range(1, 6)}
# print(inputDict)

fullyInputDict = {input(f"Key-{x}: ") : input(f"Value-{x}: ") for x in range(5)}
print(fullyInputDict)