"""
This library hosts important mathematical functions such as factorial, prime_check, perfect number check, armstrong number check etc.
"""

def fact(n):
    prod = 1
    for i in range(2, n+1):
        prod = prod * i
    return prod

def prime_check(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:        
            return False
    return True

def is_perfect(n):
    sum = 0
    # for i in range(1, n):
    for i in range(1, (n//2)+1):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    return False

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

print("Name of this file (important_function):", __name__)

if __name__ == "__main__":
    a = int(input("Test data: "))
    print(f"fact = {fact(a)}")
    print(f"prime = {prime_check(a)}")
    print(f"armstrong = {is_armstrong(a)}")
    print(f"perfect = {is_perfect(a)}")