# Some important built in modules
# Write a recursive function that returns nth term of Fibonacci Sequence:

def fibb(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)

print(fibb(50))
# term numbers: 1  2  3  4  5  6  7  8,  9   10  11  12   13
# terms:        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144