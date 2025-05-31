"""
Ask 5 integers from user, print sum of their factorials on the screen. Use functions.
"""
'''
def factorial(n):
    """This function takes an integer and returns its factorial"""
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans
'''
# print("Enter 5 integers:")
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# final = factorial(a) + factorial(b) + factorial(c) + factorial(d) + factorial(e)
# print(f"{a}! + {b}! + {c}! + {d}! + {e}! = {final}")

# Docstrings:
# print(factorial.__doc__)

"""
we write () after a function if and only if we want to call it.
"""
# copying a function

"""
c_fact = factorial
# print(c_fact(5))

# deleting a function
del factorial
# factorial(5)
print(c_fact(5))
"""
'''
def factorial(n):
    """This function takes an integer and returns its factorial"""
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def avg(p, q, r):
    return (p + q + r)/3

print("Enter 3 integers:")
a = int(input())
b = int(input())
c = int(input())

aof = avg(factorial(a), factorial(b), factorial(c))
print(aof)
'''
# Nesting of functions:

def avg(p, q, r):
    def factorial(n):
        """This function takes an integer and returns its factorial"""
        ans = 1
        for i in range(1, n+1):
            ans *= i
        return ans
    return (factorial(p) + factorial(q) + factorial(r))/3

print("Enter 3 integers:")
a = int(input())
b = int(input())
c = int(input())

aof = avg(a, b, c)
print(aof)
# factorial(5)

# Next Class: Scope of a variable, local variables, global variables and global keyword.