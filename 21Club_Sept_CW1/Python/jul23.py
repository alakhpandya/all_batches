'''
a = "p"
print(a)
print(type(a))

b = "We did not have class last week."
print(b)
print(type(b))

# strings: Ordered and Immutable collections of characters.
b = 	   "We did not have class last week, so we had a practice session."
# index no: 0123456789...................................................61
# -ve index:.....................................................987654321
# ordered:
w1 = "and"
w2 = "dna"
print(len(b))
# accessing through index numbers:
print(b[7])
# print(b[530])
# slicing
c = b[5 : 50]
# print(b)
# print(c)
# print(b[50])

print(b[11 : 58])
# accessing through -ve index:
print(b[-7])
print(b[55])
print(b[-58 : -7])

print(b[-58 : 58])
print(b[7 : 530])
print(b[7 : ])
print(b[ : 30])
print(b[ : ])
'''
b = 	   "We did not have class last week, so we had a practice session."
# index no: 0123456789...................................................61
# -ve index:.....................................................987654321

# step
print(b[11 : 58 : 2])
print(b[3 : 25 : 3])	# d ta a 
print(b[-58 : 58 : 4])

print(b[-6 : -30 : -1])
