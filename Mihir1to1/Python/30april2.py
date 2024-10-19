# strings: Ordered & immutable collection of characters.
str1 = "Mihir is a good boy."
#index: 0123456789........(19)
#-ve in:...........987654321

"""
a = 77
b = str(a)
print(str1)
print(type(str1))
l = len(str1)
print(l)

# Accessing through index:
print(str1[6])
print(str1[12])
# print(str1[300])
print(str1[2 : 13])
print(str1[2 : 300])
print(str1[3:])
print(str1[:12])
print(str1[:])

print(str1[2:18:2])	# skips 1 character
print(str1[2:18:3])	# skips 2 characters
# print(str1[2:18:n])	# skips (n-1) characters
print(str1[2:18:])
print(str1)		# slicing never changes the original.
"""
# Accessing through negative indices:
print(str1[-7])
print(str1[-7:-18]) 	# str1[13:2]
print(str1[-18:-7])
print(str1[-18:-7:2])

print(str1[::-1])
print(str1[-7:-18:-1])











