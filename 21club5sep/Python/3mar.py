"""
l1 = [54, 22, 44, 37, 96, 22, 83, 22, 65, 100, 22, 301]
l2 = l1
l3 = l1.copy()
l1.clear()
print("l1 =", l1)
print("l2 =", l2)
print("l3 =", l3)
"""
"""
3. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
Example:
input string: Keep yourself mute while not speaking.
output: Keep_yourself mute while not#speaking.
"""
"""
s1 = input("Enter any string: ")
output = s1.replace(" ", "_", 1)[::-1].replace(" ", "#", 1)[::-1]
print("Output String: ", output)
"""
# 3. Write a program to print average of all numbers of a list given by user.
"""
l1 = [54, 22, 44, 37, 96, 22, 83, 22, 65, 100, 22, 301]
avg = sum(l1)/len(l1)
"""
# Operators in Python
"""
1. Arithmetic
    +
    -
    *
    /
    %
    //  Floor Division/Integer Division
    **  Exponent/Power

2. Conditional/Relational/Comparision
    <
    >
    <=
    >=
    ==
    !=

3. Logical
    and
    or
    not

4. Bitwise 
    &   Bitwise and
        3 : 0 0 1 1
        5 : 0 1 0 1
        -----------
            0 0 0 1 = 1

    |   Bitwise or
        3 : 0 0 1 1
        5 : 0 1 0 1
        -----------
            0 1 1 1 = 7
    
    ^   Bitwise xor
        3 : 0 0 1 1
        5 : 0 1 0 1
        -----------
            0 1 1 0 = 6

    ~   Bitwise not
        3 : 0 0 1 1
        ~3: 1 1 0 0 = -4

    <<  Bitwise left shift
    20 : 0 0 0 1  0 1 0 0
    << : 0 0 1 0  1 0 0 0
    << : 0 1 0 1  0 0 0 0 

    >>  Bitwise right shift

5. Assignment
    =

    shorthand operators:
    a = a + b   =>  a += b
    a = a - b   =>  a -= b
    a = a * b   =>  a *= b
    a = a / b   =>  a /= b
    a = a % b   =>  a %= b
    a = a // b   =>  a //= b
    a = a ** b   =>  a **= b
    a = a & b   =>  a &= b
    a = a | b   =>  a |= b
    a = a ^ b   =>  a ^= b
    a = a << b   =>  a <<= b
    a = a >> b   =>  a >>= b

    *There is nothing such as: a++, a--, ++a, --a in Python. We need to use a += 1 or a -= 1 instead.
"""

# print(11/4)
# print(11//4)
# print(round(22/7))
# print(round(22/7, 3))
# print(10 ** 4)

# print(10 < 4)
# print(4 < 10 and 4 <= 20)
# a = 4 < 10
# print(4 <= 5 < 10)
# print(3 | 5)

# print(20 << 2)

# Multiple Assignment:
a, b, c, d = 10, 20, 30, 40
a, b, c, d = d, c, a, b