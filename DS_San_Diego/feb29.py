# Loops in Python: while, for
fruits = ["apple", "banana", "kiwi", "grapes", "mangoes", "berries"]

# iterator/loop control variable
"""
i = 0
while i < len(fruits):	# i = 0, 1, 2, 3, 4, 5, 6
	print(fruits[i])
	i += 1
print("i =", i)
"""
# write a program that prints multiplicative table of 7 using while loop.
"""
7 x 1 = 7
7 x 2 = 14
...........
7 x 10 = 70
"""
# write a program that takes an integer from user and prints multiplicative table of it using while loop.
"""
a = int(input("a : "))
i = 1
while i <= 10:
	print(f"{a} X {i} = {a*i}")
	i += 1
"""
# One more application of multiple assignment:
"""
# a, b = 5, 10
a, b, c = 5, 10, 15
print(f"a = {a}")
print(f"b = {b}")
# print(f"c = {c}")
# c = b
# b = a
# a = c

a, b = b, a
print(f"a = {a}")
print(f"b = {b}")
a, b, c = c, a, b
"""
# Ask an integer from the user and print all the even numbers till that integer (including it).
# Ask two integers from the user and print all the odd numbers between them (including both).
# a = int(input("smaller number: "))
# b = int(input("bigger number: "))

a = int(input("a: "))
b = int(input("b: "))
a, b = min(a, b), max(a, b)
i = a
print(f"Odd numbers between {a} and {b} are:")
while i <= b:
    if i % 2 == 1:
        print(i)
    i += 1