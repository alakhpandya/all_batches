"""
Write a program that prints "Prime" if the number given by the user is prime, otherwise prints "Composite."
"""
# n = int(input("Enter any integer: "))

"""
1003%2 = 1
1003%3 != 0
1003%4 == 0 => break
.
.
.
.
1003/1002
"""
"""
# flag variable
flag = 1
i = 2
while i < n:
    if n % i == 0:
        # print("Composite.")
        # print("1st factor: ", i)
        flag = 0
        break
    i += 1
# print("Over with i =", i)
if flag == 0:
    print("Composite.")
else:
    print("Prime.")
"""

# while - else: break - else
"""
i = 2
while i < n:
    if n % i == 0:
        print("Composite.")
        break
    i += 1
else:
    print("Prime.")
"""
"""
Given list: fruits = ["blueberries", "orange", "apple", "strawberries", "banana", "guava"]
ask user for any fruit name and print whether that fruit is in the list or not.
"""
fruits = ["blueberries", "orange", "apple", "strawberries", "banana", "guava"]