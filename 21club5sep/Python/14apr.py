# Nesting of functions
"""
Ask 5 integers from user and print average of their factorials.
"""
"""
def factorial(n):
    pass

def avg(n1, n2, n3, n4, n5):
    def fact(n):
        f = 1
        for x in range(1, n+1):
            f *= x
        return f
    return (fact(n1) + fact(n2) + fact(n3) + fact(n4) + fact(n5))/5

print("Enter 5 integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print("Average of their factorial is:", avg(a,b,c,d,e))
f = int(input("Enter the last number:"))
fact(f)
"""
# scope of a variable, local variables, global variables and global keyword
'''
a = 10          # global variable

def func1():
    global a, b
    a = 15
    a += 1
    print("a by func1 =", a)
    """
    c = 30      # local variable of func1
    def func3():        # local function
        print("c by func3 =", c)
    func3()
    """

# def func2():
#     print("b by func2 =", b)
    # print("c by func2 =", c)

print("a by main =", a)
func1()
b = 20          # global variable for all the functions which will be CALLED after this point.
# func2()
print("a by main =", a)
'''
# Deleting/Copying a function
"""
def func1(a, b):
    print("average =", (a+b)/2)

func2 = func1
del func1
# func1(5,6)
func2(5,6)
"""
# Passing collections to a function as argument
"""
def avg(x):
    return sum(x)/len(x)

numbers = [3,4,5,6,7]
print("Average =", avg(numbers))
t1 = 3,4,5,6,7
print("Average =", avg(t1))
s1 = {3,4,5,6,7}
print("Average =", avg(s1))
d1 = {5 : 20, 6 : 30, 7 : 40, 8 : 50}
print("Average =", avg(d1))
"""