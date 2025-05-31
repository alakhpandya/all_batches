"""
Operators:
1. Arithmetic Operators:
+, -, *, /, %, **, //

2. Conditions/Conditional Operators/Relational Operators/Comparision Operators
<, <=, >, >=, ==, !=

3. Logical Operators
and, or, not

4. Bitwise Operators
    &, |, ~, ^ (xor), <<, >>

        5: 0 1 0 1
        3: 0 0 1 1  =>  1 1 0 0 = -4
        ----------
        0 0 0 1 = 1
        0 1 1 1 = 7


        5: 0 1 0 1  
        3: 0 0 1 1 
        ----------
        0 1 1 0 = 6


        743:    0  0 0 1 0  1 1 1 0  0 1 1 1
        <<      0  0 1 0 1  1 1 0 0  1 1 1 0
        <<      0  1 0 1 1  1 0 0 1  1 1 0 0
        <<      1  0 1 1 1  0 0 1 1  1 0 0 0
5. Assignment Operators
    =
    a = a + b   =>  a += b
    a = a - b   =>  a -= b
    a = a * b   =>  a *= b
    a = a / b   =>  a /= b
    a = a % b   =>  a %= b
    a = a ** b   =>  a **= b
    a = a // b   =>  a //= b
    a = a & b   =>  a &= b
    a = a | b   =>  a |= b
    a = a ^ b   =>  a ^= b
    a = a << b   =>  a <<= b
    a = a >> b   =>  a >>= b

    There's no such thing as a++ or a-- in Python so, we have to write a += 1 or a -= 1 instead.

6. Membership Operators
    in, not in

7. Identity Operators
    is, is not
"""
# print(10 ** 3)
# print(10 / 4)
# print(10 // 4)
# print(10 < 4)
# print(10 > 4)

# x = float(input("Enter two numbers:\n"))
# y = float(input())
# print(x < 10 and y < 10)
# print(x < 10 or y < 10)
# print(not x < 10)

# print(5 & 7)
# print(5 & 3)
# print(5 | 3)
# print(~3)
# print(5 ^ 3)

# print(743 << 3)

# print("n" in "Nency")
# print("Yesha" not in "NencYesha")
"""
print("Enter 3 integers:")
x = int(input())
y = int(input())
z = int(input())

a = [1,2,3]
b = [x, y, z]

print(a == b)
"""
"""
a = [1,2,3]
b = a
c = a.copy()
print(c)
# print(b)
print(a is b)
print(a is c)
print(a == c)
"""
"""
if (a < 0){
    printf("Negative.");
}
else if(a == 0){
    printf();
}
printf("Thanks");
"""
"""
marks = int(input("Enter marks: "))
if marks > 35:
    print("Pass :)")
    print("if over..")
else:
    print("Fail :(")
print("Thanks!")
"""
"""
n = int(input("Enter a number: "))
if n > 0:
    print("Positive.")
elif n == 0:
    print("Zero.")
else:
    print("Negative.")
"""
"""
n = int(input("Enter a number: "))
'''
if n < 5:
    n += 1
'''
if n < 5: n += 1
print("final n =", n)
"""
marks = int(input("Enter marks: "))
if marks > 35:
    print("Pass :)")
else:
    print("Fail :(")

print("Pass :)") if marks > 35 else print("Fail :(")