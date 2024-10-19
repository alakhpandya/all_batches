def factorial(n):
    f = 1
    for x in range(1, n+1):
        f *= x
    return f

def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def average(*args):
    return sum(args)/len(args)

def printName():
    print(__name__)

if __name__ == "__main__":
    n1 = int(input("Enter a number: "))
    print(factorial(n1))
    n2 = int(input("Enter a number: "))
    print(average(n1, n2))
    print(prime(n2))
    print("module's name: ", end ="") 
    printName()