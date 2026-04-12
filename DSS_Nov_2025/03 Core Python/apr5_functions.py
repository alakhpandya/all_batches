x = """
without arguments, without return
with arguments, without return
without arguments, with return
with arguments, with return
"""
'''
def func1():
    print("Hey, I am func1!")

func1()

def whole_square(x, y):     # Positional Arguments
    """
    This function will give you whole square of x + y.
    x & y must be numbers (floats or int).
    """
    t = (x + y)**2
    print(f"({x} + {y})^2 = {t}")
    print(f"{a} + {b} = {a + b}")           # work
    # print(f"{a} + {b} + {d} = {a + b + d}")         # won't work
    return t

def func2():
    d = 20
    print("The value of d is:", d)
    d = d + 1
    print("The new value of d is:", d)

def func3():
    global d
    d += 1

whole_square(3, 4)
# a = int(input("first no: "))    # 5
# b = int(input("second no: "))   # 7
# c = int(input("third no: "))    # 6

# f = whole_square(a, b)
# f + c
# print("f =", f)

d = 10

# func2()
# print("The value of global d is:", d)

# func3()
# print("The new value of global d is:", d)

# print(whole_square.__doc__)
'''
"""
1. Write a Python function that determines whether the number given in its argument is an Armstrong number or not. Write a supporting main program that takes two numbers from user and prints all the armstrong numbers between them.

def is_armstrong(x):
    temp_x = x
    digits = []
    power = 0
    while temp_x > 0:
        digits.append(temp_x % 10)
        temp_x = temp_x//10
        power = power + 1

    sum = 0
    for digit in digits:
        sum = sum + digit**power
    
    if sum == x:
        return True
    else:
        return False

a = int(input("a = "))
b = int(input("b = "))
for x in range(a, b+1):
    if is_armstrong(x):
        print(x)


2. Write a Python function that determines whether the number given in its argument is a Prime number or not. Write a supporting main program that takes two numbers from user and prints all the Prime numbers between them.

def prime_check(x):
    for i in range(2, x):
        if x % i == 0:        
            return False
    return True

a = int(input("a = "))
b = int(input("b = "))
for i in range(a, b+1):
    if prime_check(i):
        print(i)


3. Write a Python function that determines whether the number given in its argument is a perfect number or not. Write a supporting main program that takes two numbers from user and prints all the Perfect numbers between them.


def is_perfect(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    if sum(factors) == n:
        return True
    return False

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    return False

def is_perfect(n):
    # return True if sum([i for i in range(1, n) if n % i == 0]) == n else False
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_perfect(n):
    sum = 0
    # for i in range(1, n):
    for i in range(1, (n//2)+1):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    return False

x = int(input("First no: "))
y = int(input("Second no: "))
for i in range(x, y+1):
    if is_perfect(i):
        print(i)
"""
"""
def prime_check(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:        
            return False
    return True

a = int(input("a = "))
b = int(input("b = "))
for i in range(a, b+1):
    if prime_check(i):
        print(i)
"""