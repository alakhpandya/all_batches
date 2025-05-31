"""
sqrt 4 = ?
(+2)*(+2) = 4
(-2)*(-2) = 4

sqrt (-9)
(3)*(3) = 9*(-1)
= 3j
"""
# c = (3j + 5)
# d = (4j - 3)
# print(c)
# print(type(c))

# print(c + d)
# print(c * d)
# print(c / d)
"""
(3j + 5)*(4j - 3)
12j^2 - 9j + 20j - 15
-12 + 11j -15
11j - 27
"""

# Non-numeric datatypes:
# Strings:

# myStr = "abc"
# yourStr = 'pqr'

# print(myStr)
# print(type(myStr))

# print(len(myStr))
# a = 12345
# b = str(a)
# print(a)
# print(type(a))
# # print(len(a))

# print(b)
# print(type(b))
# print(len(b))

# print("No of digits in a:", len(str(a)))

"""
Try to print the following message exactly as it appears below:

1. Alpha says Beta "Gamma is teasing Delta".
2. Alpha says Beta "Gamma was teasing Delta and I told him don't do that".
"""
"""
print('Alpha says Beta "Gamma is teasing Delta".')
print('Alpha says Beta "Gamma was teasing Delta and I told him', "don't", 'do that".')

# Escape sequence character
print("Alpha says Beta \"Gamma was teasing Delta and I told him don't do that\".")
# \n = new line character
# \t = tab character
# \b = backspace character

# print("Hello\tWorld")
# print("Hello\nWorld")
# print("Hello\b\b\bWorld")
print("Hello\b\b\bW")
"""

# print("Hello", end="\n")
# print("Hello", end="")
# print("Hello", end=" ")
# print("Hello", end="\t")
# print("World")

# Taking inputs
print("Enter a:", end=" ")
a = input()
print("a =", a)
b = input("Enter b: ")

# Take two inputs from user, call them a & b, print them and also print their sum (a + b).
"""
Try to print the following message as it is:

I told my students: "In Python we use '\t' to give 'tab' but if we want to print \t, we need to type \\t"
"""