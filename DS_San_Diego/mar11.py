# Prime number program:
from math import floor
"""
n = int(input("n: "))

# for i in range(2, (n//2)+1):
for i in range(2, floor(n ** 0.5)+1):
    if n % i == 0:
        print(f"Composite, it is divisible by {i}.")
        break
else:
    print("Prime.")

"""
print("Enter two positive integers:")
a = int(input("a: "))
b = int(input("b: "))

for n in range(a, b+1):
    if n == 1:
        print("1 is neither Prime nor Composite.")
        continue
    for i in range(2, floor(n ** 0.5)+1):
        if n % i == 0:
            print(f"{n} is Composite, it is divisible by {i}.")
            break
    else:
        print(f"{n} is Prime.")