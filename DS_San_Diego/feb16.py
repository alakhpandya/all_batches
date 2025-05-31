
# 1. Arithmetic Operators: +, -, *, /, %, // (floor division), ** (power)

# Write a program that takes days from the user and converts it into year, month & days (consider each month to be of exactly 30 days for sack of simplicity)
# Sample execution:
"""
Case-1:
Enter days: 1200
Output:
3 Years 3 Months 15 days

Case-2:
Enter days: 1100
Output:
3 Years 0 Months 5 days


days = int(input("Enter days: "))   # 1200

years = int(days / 365)
remaining_days = days % 365
months = remaining_days // 30       # same as int(remaining_days / 30) in this case
final_days = remaining_days % 30

print(f"{years} Years, {months} Months, {final_days} Days")


print(5 / 2)        # 2.5
print(5 // 2)       # 2
print(int(5 / 2))   # 2

print("Negative operand:")
print(-5 / 2)        # 2.5
print(-5 // 2)       # Q = -2.5 => floor(Q) = -3
print(int(-5 / 2))   # Q = -2.5 => int(Q) = -2

import math

print(math.floor(3.7))
print(math.ceil(3.7))
print(round(3.7))
print("5 * 7 =", 5 * 7)
print("5 ** 7 = 5^7 =", 5 ** 7)

((((a * 3)**2)/3.5) < 10)

a ** (3 / 12)
(a ** 3) / 12

Priority:
()
**
*, /, %
+, -
"""

# 2. Conditional Operators/Relational Operators/Conditions/Comparison Operators: <, >, <=, >=, ==, !=
# Conditions always return either True or False
"""
a = 5   # Command: Store '5' in 'a'

print(a == 5)  # Question: Is there '5' in 'a'?
print(a < 5)
"""

# 3. Logical Operators: and, or, not
# Order of precedence: not, and, or
"""
x = 5
y = 10
z = 7

print(x < 10 and y < 20 and z < 5)
print(x < 10 or y < 20 or z < 5)
print(not z < 5)

# Write a code that asks attendance, number of memos and marks of a student and print if the student is qualified for the field trip or not. He/she is qualified if either their attendance is atleast 70% or they have got above 90 marks in the finals but in both the cases, they must not have received more than 3 memos.

Case-1:
Enter the following details:
Attendance % : 75
Memos received: 5
Marks in fianls: 93

Output:
True
False

What is False & what is True?
"""
# 4. Bitwise Operators: &, |, ~, ^ (xor), << (left shift), >> (right shift)
# print(3 & 5)
# print(3 | 5)
# print(~3)
# print(3 ^ 5)
# print(9 << 4)
# print(bin(9354 << 3))
"""
3: 0 0 1 1
   & & & &
5: 0 1 0 1
----------
   0 0 0 1 => 1

3: 0 0 1 1
   | | | |
5: 0 1 0 1
----------
   0 1 1 1 => 7

3 : 0 0 1 1
~3: 1 1 0 0 => 12
# 2's complement
0 1 0 0 => (-4)

# For a successful signup user must enter either their email address or mobile number.
OR
email    mobile   Signup
F        F        F
T        F        T
F        T        T
T        T        T

# What would you like to have? Tea or coffee?
Exclusive OR = xor
Tea   Coffee   OK?
F     F        F
T     F        T
F     T        T
T     T        F

3 ^ 5

3: 0 0 1 1
   ^ ^ ^ ^
5: 0 1 0 1
----------
   0 1 1 0 => 6

9 : 0 0 0 0  1 0 0 1
<<: 0 0 0 1  0 0 1 0
<<: 0 0 1 0  0 1 0 0
<<: 0 1 0 0  1 0 0 0


166 : 1 0 1 0  0 1 1 0
>>  : 0 1 0 1  0 0 1 1 => 83
>>  : 0 0 1 0  1 0 0 1 => 41
>>  : 0 0 0 1  0 1 0 0 => 20
"""

# 5. Assignment Operators:
"""
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
"""
"""
a = 5
 <--

5 = a
 <--

b = ((((a * 3)**2)/3.5) < 10) and ((((a * 2)**3.5)/3) > 8)

a = 10
a = a + 5
a += 5
"""

# 6. Identity Operators: is, is not
"""
a = [11, 12, 13, 14]
b = a             # Shallow copy
c = [20, 30, 40]
d = a.copy()      # Deep copy
e = [11, 12, 13, 14]
# print(a == b)
# print(a == c)
# print(a == d)
# print(a is d)
# print(a == e)
print(a is e)
"""

# 7. Membership Operators: in, not in
# a = [11, 12, 13, 14]
# b = "Hello is world"
# c = (101, 120, 113, 514)

# print(12 in a)
# print('z' in b)
# print('orld' in b)
# print('old' in b)
# print(1000 in c)
# print(113 in c)

# IMP: There is nothing like a++ or a-- in Python! For those operations, we need to type a += 1 or a -= 1