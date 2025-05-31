# Lambada Functions/Anonymous Functions/In-line Functions
"""
# def cube(n):
#     return n ** 3

cube = lambda n : n ** 3
print(cube(7))

# wish = lambda : "All the best!"
wish = lambda : print("All the best!")

# print(wish())

# average = lambda a,b,c,d,e : (a + b + c + d + e)/5
average = lambda a,b,c,d,e : print((a + b + c + d + e)/5)

print(average(3,4,5,6,7))
"""

# Creating A Function Anonymously
# (lambda a,b,c,d,e : (a + b + c + d + e)/5)(5,6,7,8,9)
"""
n = [5, 8, 11, 13.4, 15, 20, 34]
cubes = list(map(lambda n: n ** 3, n))
print(n)
print(cubes)
"""
# scope of a variable, local variables, global variables & global keyword, nesting of functions 
"""
v1 = 10                     # global

def func1():
    global v1
    v1 = 15
    v1 += 1
    print(f"v1 by func1 = {v1}")
    print(f"v2 by func1 = {v2}")
    # print(f"v3 by func1 = {v3}")
    v4 = 40         # local variable of func1 that can be accessible by func1 & all its child functions
    print(f"v4 by func1 = {v4}")
    def subFunc():      # local function
        print(f"v4 by subFunc = {v4}")
        v5 = 50     # local variable of subFunc which can be accessible only inside subFunc
        print(f"v5 by subFunc = {v5}")

    subFunc()
    # print(f"v5 by func1 = {v5}")

def func2():
    pass
    # print(f"v4 by func2 = {v4}")
    # subFunc()
    func1()

print(f"v1 by main = {v1}")
v2 = 20             # global for all the functions CALLED after this point
func1()
v3 = 30             # global for all the functions CALLED after this point
print(f"v1 by main = {v1}")

# print(f"v4 by main = {v4}")
# func2()

# subFunc()
"""

# Recursive functions
"""

Recursive Definition(step): n*(n-1)!
n = 5 => 5! = 5 * 4!

Non-Recursive Definition(step): 0! = 1

def rec_func():
    if (lhs of non-recursive step):
        return (rhs of non-recursive step)
    else:
        return (rhs of recursive step)
"""
def rec_fact(n):
    if n == 0:
        return 1
    else:
        return n * rec_fact(n-1)

# (e^x * log x) - (sin x)^2 = 0


# Next Class: fibonacci sequence recursion, memoization, postional, default, variable, keyword arguments