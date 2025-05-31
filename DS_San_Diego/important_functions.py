def armstrong(x):
    sum=0
    tmp=x
    while tmp>0:
        sum+=(tmp%10)**len(str(x))
        tmp=tmp//10
    if sum==x:
        return True
    else:
        return False

def primeCheck(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def avg(a, *args):
    if len(args) == 0:
        return a
    return sum(args, a)/(len(args)+1)

def triangleTest(a1, a2, a3):
    if a1+a2+a3 == 180:
        return True
    return False

def factorial(n):
    if n < 0:
        return False
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n+1):
            f *= i
        return f
    

# print("name of the module:", __name__)
# print("Hello there!")
import may17

if __name__ == "__main__":
    may17.anyFunc()
    # print("They make a triangle...") if triangleTest(60, 30, 90) else print("They don't make a triangle...")
    # print(f"Average of 4, 10 and 20 is: f{avg(4, 10, 20)}")
    # a = int(input("a: "))
    # print(factorial(a))