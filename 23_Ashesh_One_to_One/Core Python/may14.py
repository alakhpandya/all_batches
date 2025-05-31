# numbers = [11, 22, 33, 44, 11, 9, 13, 11, -56, 7.56, -15.87, 11, 37, 11]
# print(numbers.pop())
# print(numbers.pop(5))       # always write index number in pop() argument
# print(numbers.pop(15))
# print(numbers)

# print(numbers.remove(-15.87))      # always write member itself in remove()
# print(numbers)

# numbers.reverse()
# numbers.sort(reverse=True)
# print(numbers)

"""
Operators in Python
1. Arithmetic Operators
    +
    -
    *
    /
    %
    //
    **

2. Logical Operators
    and: True if and only if all the conditions involved are True
    or: True if any of the conditions involved are True
    not: True if the condition involved is False

3. Conditional Operators/Conditions/Relational Operators
    <
    >
    <=
    >=
    ==
    !=
    They will always return either True or False

    False in Python: False, 0, "", [], {}, (), set(), 0.0
    Everything else: True

4. Bitwise operators
    &
        3 : 0 0 1 1
        5 : 0 1 0 1
        -----------
            0 0 0 1 = 1
    |
        3 : 0 0 1 1
        5 : 0 1 0 1
        -----------
            0 1 1 1 = 7
    ~
        3 : 0 0 1 1
        -----------
            1 1 0 0 = -4
    ^
        3 : 0 0 1 1
        5 : 0 1 0 1
        -----------
            0 1 1 0 = 6
    <<
        19 : 0 0 0 1  0 0 1 1
        << : 0 0 1 0  0 1 1 0
        << : 0 1 0 0  1 1 0 0

    >>

5. Assignement Operators
    =
        a = 5
         <--
        7 = x       Wrong in programming
        
        Multiple assignment
        swapping two variables

    shorthand operators: icrement/decrement operators like a++ or a-- are not available in Python

    a = a + b   :   a += b
    a = a - b   :   a -= b
    a = a * b   :   a *= b
    a = a / b   :   a /= b
    a = a % b   :   a %= b
    a = a ** b   :   a **= b
    a = a // b   :   a //= b
    a = a & b   :   a &= b
    a = a | b   :   a |= b
    a = a ^ b   :   a ^= b
    a = a << b   :   a <<= b
    a = a >> b   :   a >>= b

6. Membership Operators
    in
    not in

7. Identity Operators
    is
    is not
"""
"""
print(3 & 5)
print(19 << 2)
# a = 10
# b = 20
a, b, c, d = 10, 20, 30, 40
print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
# a, b = b, a
# print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
print()
a, b, c, d = c, d, a, b
print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
"""
"""
numbers = [11, 22, 33, 44, 11, 9, 13, 11, -56, 7.56, -15.87, 11, 37, 11]
test = float(input("Enter any number: "))
if test in numbers:
    print("Yes")
else:
    print("No")
"""
"""
n1 = [1,2,3,4]
n2 = n1
n3 = n1.copy()
n4 = [1,2,3,4]
# n1.pop()
# print("n1 =", n1)
# print("n2 =", n2)
# print("n3 =", n3)
# print("n4 =", n4)
print(n1 == n3)
print(n1 is n3)
print(n1 is n2)
"""
n = int(input("Enter n: "))
# if n > 0: print("Positive.")
# print("Thanks!")

"""
if n > 0:
    print("Positive.")
else:
    print("Negative.")
"""
print("Positive.") if n > 0 else print("Negative.")

# There is no shorthand for elif
"""
if....

if...


if

elif

elif
"""
# No switch case in Python
# Loops: while, for. There is no do-while loop in Python.