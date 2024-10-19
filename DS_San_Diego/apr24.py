# Nesting of lists - Matrix
"""
m1 = [[1,2,3], [3,4,5], [9,8,4]]
m2 = [
    [1,2,3],
    [5,8,6],
    [9,7,4]
]
print(m1)
print(m2)
"""

# Write a code that takes two 3x3 matrices from user, print both of them in a 'matrix look', add them & store the result in a 'sum' matrix and finally also prints the sum matrix.

def scanMatrix(matrix_name, row, col):
    mat = []
    print(f"Enter {row*col} numbers for matrix {matrix_name}:")
    for i in range(row):
        print(f"Row-{i}:")
        rw = []
        for j in range(col):
            rw.append(float(input(f"{matrix_name}[{i}][{j}]: ")))
        mat.append(rw)
    return mat

def printMatrix(matrix_name, matrix):
    print(f"matrix {matrix_name}:")
    for row in matrix:
        for data in row:
            print(data, end="\t")
        print()

def addMatrix(m1, m2):
    rm1 = len(m1)
    cm1 = len(m1[0])
    rm2 = len(m2)
    cm2 = len(m2[0])
    if rm1 != rm2 or cm1 != cm2:
        return False
    else:
        total = []
        for x in range(rm1):
            rw = []
            for y in range(cm1):
                rw.append(m1[x][y] + m2[x][y])
            total.append(rw)
        return total


a = scanMatrix("a", 3, 3)
b = scanMatrix("b", 3, 3)

printMatrix("a", a)
printMatrix("b", b)
sum = addMatrix(a, b)

printMatrix("sum", sum)

