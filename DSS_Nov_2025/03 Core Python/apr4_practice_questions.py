# Write a program to print factors of an integer (user input)
# 12: 1, 2, 3, 4, 6, 12
"""
x = int(input("x = "))
x_temp = abs(x)
factors = []
for i in range(1, x_temp+1):     # i = 1,2,3,4,5 ..., x
    if x_temp % i == 0:
        factors.append(i)
        if x < 0:
            factors.append(-i)
    
print(f"factors of {x} are:", factors)
"""

# Write a program to check if the +ve integer given in the input is prime or not
"""
x = int(input("x = "))
is_prime = 1
for i in range(2, x):
    if x % i == 0:
        print("Not Prime.")
        is_prime = 0
        break
# if is_prime:
    print("Prime.")
"""
# False in Python: False, 0, [], empty dictionary- {}, empty set- set(), empty string- "", empty tuple- tuple()
# True for Python: every thing else 

# for-else, while-else: break-else
"""
x = int(input("x = "))
for i in range(2, x):
    if x % i == 0:        
        print("Not Prime.")
        break
else:
    print("Prime.")
"""
"""
x = int(input("x = "))      # 153
str_x = str(x)              # "153"
power = len(str_x)          # power=3
sum = 0
for n in str_x:     # n = "1", "5", "3"
    sum = sum + int(n)**power
if sum == x:
    print("Armstrong")
else:
    print("Not Armstrong.")
"""
"""
x = int(input("x = "))
temp_x = x
digits = []
power = 0
while temp_x > 0:
    digits.append(temp_x % 10)
    temp_x = temp_x//10
    power = power + 1

print(digits)
sum = 0
for digit in digits:
    sum = sum + digit**power
print(sum)
if sum == x:
    print("Armstrong.")
else:
    print("Not Armstrong.")
"""

# Ask two integers from the user & print all the prime numbers between those two integers
"""
a = int(input("a = "))
b = int(input("b = "))
prime_nos = []
for x in range(a, b+1): # x = a, a+1, a+2, ..., b
    for i in range(2, x):
        if x % i == 0:        
            break
    else:
        prime_nos.append(x)
print(f"Prime number between {a} and {b} (including both) are:", prime_nos)
"""
# Ask two integers from the user & print all the Armstrong numbers between those two integers
"""
a = int(input("a = "))
b = int(input("b = "))
arm = []
for x in range(a, b+1):
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
        arm.append(x)
print(arm)
"""

# shorthend if-else
'''
marks = int(input("Marks = "))
"""
if marks >= 60:
    print("Qualified")
"""
# OR
# if marks >= 60: print("Qualified")
marks = int(input("Marks = "))
"""
if marks >= 60:
    print("Qualified")
else:
    print("Not Qualified")
"""
print("Qualified") if marks >= 60 else print("Not Qualified")
'''

# list comprehension
"""
myList = []
for i in range(10):
    myList.append(i)
print(myList)
"""

# myList = [i for i in range(10)]
# print(myList)

# Creating user-defined list using list comprehension
# n = int(input("n : "))
"""
myList = []
for i in range(n):
    myList.append(input())
"""
"""
myList = [input() for i in range(n)]
print(myList)
"""

# nested lists:
"""
l1 = [
    [1, 2, 3],
    [4, 5, 6],
    [12, 13, 14, 15, 16, 17, 18]
]
# print(len(l1))
# print(l1[0])
# print(l1[1][2])
print(l1[2][1:6:2])
"""
# Write a program to create a user-defined 4x3 list
yourList = []
for i in range(4):
    temp = []
    for j in range(3):
        temp.append(input(f"a[{i}][{j}] = "))
    yourList.append(temp)
print(yourList)