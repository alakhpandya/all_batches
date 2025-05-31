
# def func1(x:int, y:float):
#     """Returns whatever operation between an integer x and float y"""
#     return x*y/2

# print(func1(5))
# print(func1("Hello"))
# print(func1([1,2,3]))
# print(func1((1,2,3)))
# print(func1({1,2,3}))
# print(func1(3.5, 10))

# def func2(y):
#     return y ** y

# print(func2(7))


# Scope of a variable-1:
# def func1(x):
#     y = x * 10
#     print(x ** 2)

# a = func1(5)
# print(x)
# print(y)


# Nesting functions:
"""
Write a program that takes 5 integers from user, finds factorial of each of them and prints average of their factorials.
"""
"""
def avg_of_factorials(p, q, r, s, t):
    def fact(x):
        f = 1
        for i in range(1, x+1):
            f = f * i
        return f
    result = fact(p)+fact(q)+fact(r)+fact(s)+fact(t)/5
    def func3(y):
        fact(y)
    return round(result, 4)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))

print("average of factorials =", avg_of_factorials(a, b, c, d, e))
f = int(input("f: "))
print(fact(f))
"""

# A better approach:
"""
def fact(x):
    f = 1
    for i in range(1, x+1):
        f = f * i
    return f

def avg_of_factorials(p, q, r, s, t):
    result = fact(p)+fact(q)+fact(r)+fact(s)+fact(t)/5
    return round(result, 4)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))

print("average of factorials =", avg_of_factorials(a, b, c, d, e))
f = int(input("f: "))
print(fact(f))
"""