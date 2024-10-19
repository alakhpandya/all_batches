# Powerful Lambda Functions / In-line functions / Anonymous functions

# def avg(a, b, c):
#     return (a + b + c)/3

# avg = lambda a, b, c : (a + b + c)/3
# print(avg(5,6,10))

# lambda a, b, c : (a + b + c)/3

# avg = lambda a, b, c : print(f"Average of {a}, {b} & {c} is: {(a + b + c)/3}")
# avg(5,7,12)

# greet = lambda : "Hello!"
# print(greet())


# Some important builtin functions: sum(), zip(), round()

# abs, chr, eval, round

# x = float(input("x: "))
# print("Absolute value of x =", abs(x))

# print(chr(65))

# command = "print('Positive') if x > 0 else print('Not Positive')"
# print(command)
# eval(command)

# print("x (Rounded off) =", round(x))
# # print("x (Rounded off) =", round(x, 2))
# # print("x (Rounded off) =", round(x, 0))
# print("x (Rounded off) =", round(x, -1))
# print("x (Rounded off) =", round(x, -2))

"""
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
# print(zip(l1, l2))
zip_output = zip(l1, l2)
for x in zip_output:
    print(x)

zipped = list(zip(l1, l2))
print(zipped)

l3 = ["p", "q", "r"]
zipped3 = list(zip(l1, l2, l3))
print(zipped3)
"""


# map()
"""
def square(x):
    return x*x

myList = [3, 5, 6, 9, 10, 8, 4, 2]
# myTuple = (3, 5, 6, 9, 10, 8, 4, 2)

yourList = map(square, myList)
print(yourList)
# for x in yourList:
#     print(x)

# from sys import getsizeof
# print(getsizeof(myList))
# print(getsizeof(yourList))
# print(getsizeof(myTuple))

# for x in yourList:
#     print(x)
"""
"""
myList = [3, 5, 6, 9, 10, 8, 4, 2]
x = 3
"""
# yourList = list(map(x*x, myList))
# square = lambda x : x*x
# yourList = list(map(square, myList))

"""
yourList = list(map(lambda x: x*x, myList))
print(yourList)
"""