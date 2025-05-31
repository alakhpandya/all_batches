def factorial(number):
    fact = 1
    for x in range(1, number+1):
        fact *= x
    return fact

def arithmetic_progression(a, d, n):
    return a + (n-1)*d

def geometric_progression(a, r, n):
    return a*(r**(n-1))

def average(n, *args):
    return (sum(args)+n)/(len(args)+1)

if __name__ == "__main__":
    x = int(input("Enter any number: "))
    print(factorial(x))
    a = float(input("Enter a: "))
    d = float(input("Enter d: "))
    r = float(input("Enter r: "))
    n = float(input("Enter n: "))
    print(arithmetic_progression(a, d, n))
    print(geometric_progression(a, r, n))