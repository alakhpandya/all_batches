# List Comprehension

# Ask an integer from the user and create a list of all the natural numbers till that integer.
"""
n = int(input("n: "))

# l1 = []
# for i in range(1, n+1):
#     l1.append(i)

l1 = [i for i in range(1, n+1)]

# Create a list of squares of all the natural numbers till that integer:
l1 = [i*i for i in range(1, n+1)]

print(l1)
"""

# Create a user-defined list using list comprehension:
"""
n = int(input("No. of elements: "))

# l1 = []
# for i in range(n):
#     l1.append(input(f"member-{i+1}: "))

l1 = [input(f"member-{i+1}: ") for i in range(n)]

print(l1)
"""
# 12 : 1, 2, 3, 4, 6 = 16 => Not a perfect number
# 6 : 1, 2, 3 = 6 => Perfect number

# sum of cubes of every digit comes to that number
# 153 = 1^3 + 5^3 + 3^3  => Armstrong number