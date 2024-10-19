n = [12, 0, -23, 12, 45, 45, 33, 12, 98, 54, 12, -55, 67, 12, 100]

# print(n.append(500))
# n.append(500)
# n.append(500)

# n.clear()
# del n
# del n[5]
# n[5] = 205
# print(n)

# m = n.copy()
# l = n
# n.clear()
# print("n =", n)
# print("m =", m)
# print("l =", l)

# print(n.count(12))
# n.count(12, 1, 5)         not available in lists

# print(len(n))
# m = [1,2,3,4,5]
# # n.append(m)
# n.extend(m)
# print(len(n))
# print(n)

# n.append("Ritu")
# print(n)
# n.extend("Ritu")
# print(n)

# print(n.index(-55))
# print(n.index(45))
# print(n.index(12, 5, 10))

# n.insert(3, 3000)

# print(n.pop(7))
# n.remove(98)

# print(n.pop(40))
# del n[40]

# n.reverse()

# n.sort(reverse=True)

# print(n)

# Operators
"""
1. Arithmetic: +, -, *, /, %, **, //
2. Conditions/Coditional Operators/Relational Operators/Comparision Operators : <, >, <=, >=, ==, !=
3. Logical: and, or, not
4. Bitwise Operators: &, |, ~, ^, <<, >>

    0 1 1 1
    0 0 0 1
    -------
    0 0 0 1

    156 : 0 0 0 0 1 0 0 1  1 1 0 0
    <<  : 0 0 0 1 0 0 1 1  1 0 0 0
    <<  : 0 0 1 0 0 1 1 1  0 0 0 0
    <<  : 0 1 0 0 1 1 1 0  0 0 0 0 = 1248
5. Assignment Operators:
    a = 5
     <--
    shorthand assignments:
    a = a + b   =>  a += b
    a = a - b   =>  a -= b
    a = a * b   =>  a *= b
    a = a / b   =>  a /= b
    a = a % b   =>  a %= b
    a = a ** b   =>  a **= b
    a = a // b   =>  a //= b
    a = a & b   =>  a &= b
    a = a | b   =>  a |= b
    a = a ~ b   =>  a ~= b
    a = a ^ b   =>  a ^= b
    a = a << b   =>  a <<= b
    a = a >> b   =>  a >>= b

    Increment/decrement operators are not there in Python
6. membership operators: in, not in
7. identity operators: is, is not
"""
# print(10 ** 4)
# print(10 / 4)
# print(10 % 4)
# print(15 // 4)

# print(10 < 4)
# print(10 >= 4)

# print(10 >= 4 and 5 < 9)

# print(7 & 1)
# print(156 << 3)
# print(156 >> 3)

"""
Ternary operator in javascript: ?
marks >= 35 ? "pass" : "fail"

number > 0 ? "positive" : number < 0 ? "negative" : "zero"
"""

# print("r" in "Surat")
"""
a = [1,2,3,4]
b = a
c = a.copy()

# print(a is b)
# print(a == b)
print(a == c)
print(a is c)
"""

# health = input("Your health condition: ")
# if health == "ok":
#     print("Come to office")

# if health == "ok": print("Come to office")
# print("Good Bye!")


marks = int(input("Enter marks: "))
# if marks >= 35:
#     print("Pass")
# else:
#     print("Fail")

print("Pass") if marks >= 35 else print("Fail")


# number = float(input("Enter a number: "))
# if number < 0 :
#     print("Negative")

# elif number == 0:
#     print("Zero")

# else:
#     print("Positive")