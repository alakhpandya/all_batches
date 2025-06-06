# Positional argument, Default argument, Variable length arguments, keyword arguments
"""
def func1(a, b = 20):
    print("a =", a)
    print("b =", b)

# func1(10)
func1(10, 15)
"""
"""
def avg(*args):
    # print(args)
    # print(type(args))
    return sum(args)/len(args)

print(avg(12, 13))
print(avg(12, 13, 15, 17, 19))
# print(avg())
"""
"""
def func1(a, b, c, d = 40, e = 50, f = 60, *args):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)
    print("e =", e)
    print("f =", f)
    print("args =", args)

# func1(10,20,30,70,80)
# func1(10,20,30,70,80,90,100,200,300)
"""
"""
def func1(*args):
    pass

func1(Computers = 95, Maths = 25, Physics = 40)
"""
"""
def func1(**kwargs):
    print(kwargs)

func1(Computers = 95, Maths = 25, Physics = 40)
# func1(1 = 88, 2 = 57, 3 = 79)
"""
# First comes all the positional arguments, then comes all the default arguments, then comes *args and at last comes **kwargs.

# Powerful Lambda Functions / In-line functions / Anonymous functions
"""
def avg(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5)/5
"""
"""
print("Enter 5 integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg = lambda n1, n2, n3, n4, n5 : (n1 + n2 + n3 + n4 + n5)/5
print(avg(a, b, c, d, e))
"""
n = int(input("Enter the number you want to check: "))
# armstrong = lambda n : False if len(str(n)) == 1 else (True if sum([int(x)**len(str(n)) for x in str(n)]) == n else False)
print(lambda n : False if len(str(n)) == 1 else (True if sum([int(x)**len(str(n)) for x in str(n)]) == n else False))