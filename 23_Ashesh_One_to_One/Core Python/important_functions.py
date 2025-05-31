def factorial(n):
    f = n
    for i in range(1, n):
        f *= i
    return f

def avg(*args):
    return sum(args)/len(args)

def primeCheck(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def armstrongCheck(n):
    # for digit in str(n):
    #     digits.append(digit)
    # print(digits)
    digits = [int(digit)**len(str(n)) for digit in str(n)]
    return True if n == sum(digits) else False
    # print(f"{n} is Armstrong.") if n == sum(digits) else print(f"{n} is not Armstrong.")
    # if n == sum(digits): print(n)
    # if n != sum(digits): print(n)


print("Name:", __name__)
if __name__ == "__main__":
    print(armstrongCheck(153))
    print(armstrongCheck(1634))
    print("Enter two numbers:")
    a = int(input())
    b = int(input())
    for x in range(a, b+1):
        if armstrongCheck(x) == False:
            print(x)

    print(f"{a} is an Armstrong number.") if armstrongCheck(a) == True else print(f"{a} is NOT an Armstrong number.")