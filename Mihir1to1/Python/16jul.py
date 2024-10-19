# Golden Rule: We put paranthesis after function only when we want to call that function. If don't want to call that function, we will not put paranthesis after it.


# Misc Topics of Functions
# Lambda Functions
"""
def average(a, b):
        return (a+b)/2
def sqrt(n):
    return n ** 0.5

print("Enter three numbers: ")
x = int(input())
y = int(input())
z = int(input())
# sqrt(x)
sq = lambda n : n ** 0.5
print(sq(x))
avg = lambda a, b : (a + b)/2
print(avg(y, z))
"""
"""
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print("Enter 5 numbers: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg_of_fact = lambda a, b, c, d, e : (fact(a)+fact(b)+fact(c)+fact(d)+fact(e))/5
print(avg_of_fact(a,b,c,d,e))
"""
# Copying a function & deleting a function
def func1():
    print("Hi I am funcy!")
    return 3

func1()
# del func1
# func1()
func2 = func1
# print(func2, type(func2))
# print(type(func1))
del func1
func2()

# function returning another function
# def secret(n):
#     if n > 3:
#         return print