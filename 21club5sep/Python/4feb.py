"""
HW:
Write a Python code that takes 5 integers from user (call them a, b, c, d & e) and print their average EXACTLY as below:
sample execution:
Enter 5 integers:
3
4
5
6
7
The average of 3, 4, 5, 6 and 7 is: 5.0
"""
"""
print("Enter 5 integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg = (a+b+c+d+e)/5

# f-string
print(f"The average of {a}, {b}, {c}, {d} and {e} is: {avg}")
"""
"""
Collections in Python:

Mutable		Ordered		list
Immutable	Ordered		tuple
Mutable		Unordered	set
Immutable	Unordered	frozenset

string: collection of characters	:	Immutable	Ordered
dictionary: collection of key:value pairs:	Mutable		Unordered
"""

# string: 

s1 = 		"this batch is going to ROCK the software industry."
# index no:	 0123456789.......................................49
# -ve index no:-50........................................987654321
print(len(s1))
print(s1)
print(type(s1))
print(s1[17])
# slicing
s2 = s1[5 : 45]	
print(s1)	# slicing never changes the original data
print(s2)
print(s1[15:35])
print(s1[23:49])
print(s1[13:])
print(s1[:13])
print(s1[:])
# print(s1[333])		# IndexError
print(s1[14:333])
print("****")
print(s1[35:15])
print("****")
print(s1[-8])
print(s1[-47:-5])
print(s1[5:-7])
print("****")
print(s1[-1:1:-1])
print("****")
print(s1[5:45:2])
print(s1[-45:-5:3])
print(s1[5:45:1])
print(s1[5:45:])
print(s1[::-1])
print(s1[-5:4:-4])
print(s1[3: : 444])

# Next class: string methods

