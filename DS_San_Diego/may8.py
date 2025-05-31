# Scope of a varibale-2: Global variables, local variables & global keyword
"""
v1 = 10     # Global variable

def func1():
    global v1       # a function cannot change any global variable without using 'global' keyword
    v2 = 20     # local variable
    # print("Hey, I am func1!")
    v1 = 11     
    v1 += 1
    # print("v1 through func1 =", v1)
    # print("v2 through func1 =", v2)
    # v3 += 1     # Error
    print("v3 through func1 =", v3)

# print("v1 from main =", v1)
v3 = 30     # Global variable for the code that comes after this point
func1()
# print("v2 through func1 =", v2)       Error
# print("v1 from main =", v1)
print("v3 from main =", v3)
"""

# Deleting and copying a function
"""
We use () after the function only in two cases: 
1. At the time of defining the function & 
2. When we want to call the function.

Practical rule: Do not use () after the function name if you don't want to call it.
"""

def func1(x):
    y = x ** 2
    print("Hi! I am func1!")
    print("y =", y)
    return y

"""
func1(6)
del func1
print("Function is deleted...")
func1(5)
"""
"""
func2 = func1
func2() = func1()
func2() = func1
func2 = func1()
"""
# Copying func1 into func2
func2 = func1
del func1
del func2
func2(3)