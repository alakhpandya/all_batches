# Operators in Python
"""
1.  Arithmetic Operators
    +
    -
    *
    /   11/4 = 2.75 
    %   Modulo: returns remainder: 11 % 4 = 3
    //  Floor Division: 11 // 4 = 2
    **  Power or Exponent: 10 ** 4 = 10000

2.  Conditional Operators/ Comparision Operators:
    These will always return either True or False:
    <
    >
    <=
    >=
    ==
    !=

3.  Logical Operators:
    and
    or
    not
    xor

4.  Bitwise Operators:
    Bitwise And: &
        3: 0 0 1 1
        5: 0 1 0 1
        ----------
           0 0 0 1 : 1
    
    Bitwise OR: |
        3: 0 0 1 1
        5: 0 1 0 1
        ----------
           0 1 1 1 : 7

    Bitwise XOR: ^
        3: 0 0 1 1
        5: 0 1 0 1
        ----------
           0 1 1 0 : 6

    Bitwise Left Shift: <<
    5 << 2
        5: 0 0 0 0 0 1 0 1
       10: 0 0 0 0 1 0 1 0
       20: 0 0 0 1 0 1 0 0

    Bitwise Right Shift: >>
    10 >> 2
        10: 1 0 1 0
        5:  0 1 0 1
        2:  0 0 1 0 

5.  Assignment Operators:
    Equals to: =
    a = b
     <--
    3 + 2 = x   WRONG
    x = 3 + 2   Right
    a += b => a = a + b
    a -= b => a = a - b
    a *= b => a = a * b
    a /= b => a = a / b
    a %= b => a = a % b
    a //= b => a = a // b
    a **= b => a = a ** b
    a &= b => a = a & b
    a |= b => a = a | b
    a ^= b => a = a ^ b
    a << b => a = a << b
    a >> b => a = a >> b

    # Swapping two variables using assignment operator
    a = 10
    b = 12
    a, b = b, a

6.  Identity Operators:
    is
    is not

7.  Membership Operators:
    in
    not in
"""
print(3 > 7)
print(3 < 7)
print(3 & 5)
print(3 | 5)
print(3 ^ 5)
print(5 << 2)
print(10 >> 2)
a = 10
b = 12
print(a, b)
a, b = b, a
print(a, b)
list1 = [1, 2, 3, 4]
list2 = list1
list3 = list1.copy()
print(list1)
print(list2)
print(list3)
print(list1 == list3)
print(list1 is list3)
print(list1 is list2)
print(3 in list1)
print(4 not in list1)