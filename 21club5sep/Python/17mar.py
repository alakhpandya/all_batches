# Armstrong number program
"""
n = int(input("Enter any integer: "))
power = len(str(n))
# digits = []
# for digit in str(n):
#     digits.append(int(digit) ** power)
digits = [int(digit) ** power for digit in str(n)]
# print(digits)
print("Armstrong!") if sum(digits) == n else print("Not Armstrong!")
"""    
"""
153
[1, 5, 3]
[1, 125, 27]
"""
# digits = []
# for x in str(n):
#     digits.append(x)
# digits = [x for x in str(n)]
# print(digits)
"""
s1 = {x / x E N; 0 < x <= 10}
s1 = {1,2,3,4,5,6,7,8,9,10}
"""
# Write a Python code that takes two integers from user and prints all the Prime numbers between them.
"""
Collections in Python:

Mutable		Ordered		list        []
Immutable	Ordered		tuple       ()
Mutable		Unordered	set         {}
Immutable	Unordered	frozenset

string: collection of characters	:	Immutable	Ordered             " "  or  ' '
dictionary: collection of key:value pairs:	Mutable		Unordered       {}
"""
# tuple: Ordered and Immutable collection of members
t1 = (54, 22, 44, 37, 96, 22, 83, 22, 65, 100, 22, 301)
print(t1)
print(type(t1))
"""
Ordered means:
index numbers of each member
-ve index numbers
can access members through +ve/-ve index number
slicing is possible
"""
print(t1[5])
print(t1[-4])
# t1[3] = 307       tuples are immutable
print(t1[1 : -1 : 2])
print(t1[-1 : 1 : -2])

print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))

# Modifyig a tuple anyhow
temp = list(t1)
temp.append(1000)
t1 = tuple(temp)
print(t1)