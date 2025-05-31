"""
print("In Python we use '\\t' to give 'tab'")
print("\\n")
"""
"""
print("Enter an integer:", end=" ")
a = int(input())
print("a =", a)
b = float(input("Enter b: "))
# print(a + b)
print(a)
print(type(a))
print(b)
print(type(b))
# c = int(a) + int(b)
c = a + b
print(c)

"""
"""
a = int(input("a: "))
b = int(input("b: "))

print((a + b)/2)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""
"""
Suppose user enters 10 as a and 20 as b in the above code.
Get me the following output:
10 + 20 = 30
10 - 20 = -10
10 * 20 = 200
10 / 20 = 0.5
"""

"""
Sample execution:
Enter 5 integers:
1
2
3
4
5
The average of 1, 2, 3, 4 and 5 is: 3.0
"""
print("Enter 5 integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(f"The average of {a}, {b}, {c}, {d} and {e} is:", (a + b + c + d + e)/5)