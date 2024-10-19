# Recursion:
# factorial: Write a recursive Python function that returns factorial of the number given in its argument.
"""
4! = 4 x 3! = 24
3! = 3 x 2! = 6
2! = 2 x 1! = 2
1! = 1 x 0! = 1
0! = 1

Recursive part:
n! = n x (n-1)!
Non-recursive part:
0! = 1
"""
"""
def recursive_fc(n):
    if n == 0:
        return 1
    else:
        return n * recursive_fc(n-1)

print(recursive_fc(5))
"""
# Arithmetic Progression:
"""
first term (a)= 7
common difference (d)= 3
AP: 7, 10, 13, 16, 19, 22, 25, 28..........
100th term = 99th term + 3
1st term = 7

Recursive part:
nth term = (n-1)th term + d
Non-recursive part:
1st term = a

Direct Formula:
nth term = a + (n-1)*d
100th term = 7 + (99)*3 = 304
"""
# Write a recursive Python function that returns nth term of an AP
"""
def rec_AP(a, d, n):
    if n == 1:
        return a
    else:
        return rec_AP(a, d, n-1) + d

print(rec_AP(7, 3, 100))
"""
"""
def AP(a, d, n):
    return a + (n-1)*d
"""
# (e^x)log x + sin^2 x - 7 = 0
"""
trial & error methods
let x = 1
lhs = -6.9

let x = 2
lhs = 2.5

let x = 1.5
lhs
"""
# Write a recursive Python function that returns nth term of an GP
"""
first term (a)= 2
common ratio (r)= 3
GP: 2, 6, 18, 54, 162, 486.....
100th term = 99th term * 3
1st term = 2

Recursive part:
nth term = (n-1)th term * r
Non-recursive part:
1st term = a
"""