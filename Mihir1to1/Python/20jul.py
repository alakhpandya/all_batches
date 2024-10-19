# Recursive Functions:
"""
step 1 : Non recursive step
step 2 : recursive step

def function_name(arguments, var):
    if var == lhs of step 1:
        return rhs of step 1
    else:
        return rhs of step 2
"""
# Factorial function:
"""
Step 1: 0! = 1
Step 2: n! = n * (n-1)!
"""
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(7))
"""
find nth term of AP whose first term & common difference are given.
first term = a = 6
common diff = d= 4
6, 10, 14, 18, 22, 26, 30, 34
8th term = 7th term + d
nth term = (n-1)th term + d
a = 7
d = 14
5th term = ?
2nd term = 1st term + d
1st term = a

2. Make a Python program that finds nth term of a Geometric Progression whose first term (a)
and common ratio (r) are given by user.

3. Make a Python program that uses recursion to print multiplicative table of 12.
"""