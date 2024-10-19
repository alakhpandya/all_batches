# Write a program that takes two numbers in the argument and print thier average.

# def avg(x, y):
#     print(f"Average of {x} & {y} is {(x + y)/2}")
#     return None
    
# avg(10, 20)
# a = float(input("a: "))     # 10
# b = float(input("b: "))     # 20
# avg(a, b)
# x = float(input("x: "))     # 10
# y = float(input("y: "))     # 20
# z = float(input("z: "))     # 30
# avg(y, z)


# Ask 4 numbers from user, call them a, b, c & d. Now find average of a & b as well as average of c & d using avg() function that takes two arguments. Finally, add both the averages and only print the final answer.
"""
a = float(input("a: "))     # 10
b = float(input("b: "))     # 20
c = float(input("c: "))     # 30
d = float(input("d: "))     # 40

# def avg(x, y):
#     average = (x + y)/2
#     print(f"Average of {x} & {y} is {average}")
#     return average

def avg(x, y):
    return (x + y)/2

ans = avg(a, b) + avg(c, d)     # ans = None + None
print("Sum of averages =", ans)
"""
"""
a = 2
b = 3
a! + b! = 2 + 6 = 8
c = 4
d = 5
c! + d! = 24 + 120 = 144
avg. of fact = (8 + 144)/2 = 76
e = 6
avg.of fact + 6! = 76 + 720 = 796
"""

# Write a function that determines whether the integer given in its argument is prime or not. Use this function in the main program that takes an integer from user and prints whether it is prime or composite.

def checkPrime(x):
    end_point = int(x**0.5)+1
    for i in range(2, end_point):
        if x % i == 0:
            return False
    return True
"""
n = int(input("number: "))
if not checkPrime(n):
    print("Composite")
else:
    print("Prime")
"""

# Write a code that takes two integers from user and prints only prime numbers between them.
"""
def checkPrime2(x):
    end_point = int(x**0.5)+1
    for i in range(2, end_point):
        if x % i == 0:
            print("Composite")
            break
    else:
        print("Prime")
"""
a = int(input("a: "))
b = int(input("b: "))
for i in range(a, b+1):
    if checkPrime(i):
        print(i)