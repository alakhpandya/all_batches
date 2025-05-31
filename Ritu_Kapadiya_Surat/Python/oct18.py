# taking inputs:
"""
print("Enter two numbers:")
a = int(input())
b = float(input())
print(int(a) + float(b))
print(type(a))
print(type(b))

a = int(input("Enter two numbers:"))	# 5
b = int(input())			# 10
# f-string/formatted string
print(f'{a} + {b} = {a + b}')

for(i=0; i<5; i++){
	printf("Enter number-%d", i);
	input("Enter number-", i)
}

i = 0
a = int(input(f"Enter number-{i}"))
"""
"""
Collections in Python:
strings: Ordered and Immutable collection of characters
"""
"""
# s1 = input()
s1 = 	   'Ritu is a good girl.'
# index no: 0123456789..........
# -ve index:...........987654321
s2 = "She is from Surat."
print(s1[6])
# print(s1[300])

print(len(s1))
# slicing
print(s1[5 : 15])
print(s1[5 : 300])
print(s1[5 : ])
print(s1[ : 15])
print(s1[ : ])

print(s1[-9])
print(s1[11])

print(s1[-17 : -6])
print(s1[-6 : -17])
print("End of the code...")

print(s1[3 : -6])

print(s1[1 : 19 : 2])
print(s1[1 : 19 : 300])

print(s1[1 : 19 : -2])
print("End of the code...")
print(s1[19 : 1 : -2])

# defaults:
print(s1[0 : len(s1) : 1])

# reversing a string:
print(s1[ : : -1])
"""
# string methods:
s1 = 'Ritu is a '
s2 = "good girl."
# Magical Methods/Magical Variable or Dunder Methods
# print(s1 + s2)		# is same as writing: s1.__add__(s2)
print(s1.__add__(s2))