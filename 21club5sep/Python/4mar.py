"""
6. Identity Operators:
    is
    is not

7. Membership Operators:
    in
    not in
"""

# x = [1,2,3,4]
# y = x.copy()
# z = x
# print(x is y)
# print(x == y)
# print(x is not z)

# s1 = "Priyansh Ranpura"
# print("y" in s1)

# Decision Making (if - else)
"""
if (condition)
{
    code line 1
    code line 2
    code line 3
}
code line 4
"""
"""
n = float(input("Enter any number: "))
if n > 0:
    print("Positive.")
    print("Thanks!")
    print("Have a nice day!")
    if n % 2 == 0:
        print("Positive even number.")
    else:
        print("Positive odd number.")
elif n == 0:
    print("Neither Positive, Nor Negative.")
else:
    print("Negative.")
print("Good Bye!")
"""
# n = float(input("Enter any number: "))
# shorthand if:
# if n % 2 == 0: print("Even.")
# shorthand if-else:
"""
if n % 2 == 0:
    print("Even.")
else:
    print("Odd.")
"""
# print("Even.") if n % 2 == 0 else print("Odd.")

# if n > 0: print("Positive Even.") if n % 2 == 0 else print("Odd.")

# There is no short hand notation for if - elif - else in Python
# There is nothing like switch-case in Python.

# Loops in Python:
"""
while loop
for loop
"""
# n = float(input("Enter any number: "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i += 1
# print("Thanks & Goodbye!")

fruits = ["Apple", "Banana", "Kiwi", "Mango", "Grapes", "Orange"]
i = -1
while i < len(fruits)-1:
    i += 1
    if fruits[i] == "Mango":
        # break
        # pass
        continue
    print(fruits[i])
