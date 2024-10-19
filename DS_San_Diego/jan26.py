s1 =    "Today is Friday in India and in San Diego it must be running Thursday and it's a nice day!"
# index: 0123456789...............................................................................89
# -ve:                                                                                  ..987654321
# print(len(s1))

# Accessing through index
char = s1[9]
# print(char)

# print(s1[89])
# print(s1[-1])
# print(s1[0])
# print(s1[1])
# print(s1[-89])

# Slicing never changes the original. It returns a sliced copy of original.
# print(s1[4 : 40])       # first included, last excluded
# print(s1[39])
# print(s1)

# print(s1[300])
# print(s1[4 : 300])
# print(s1[4 : ])
# print(s1[ : 77])
# print(s1[ : ])

# print(s1[4 : 80 : 2])       # step/jump function/stride
# print(s1[4 : 10 : 2])
# print(s1[4 : 80 : 5])
# print(s1[4 : 80 : ])
# print(s1[4 : 80 : 1])

s1 =    "Today is Friday in India and in San Diego it must be running Thursday and it's a nice day!"
# index: 0123456789...............................................................................89
# -ve:                                                                                  ..987654321

# print(s1[81 : 3 : -1])
# print(s1[81])

# print(s1[-15 : -5])
# print(s1[-6 : -36 : -2])
# print(s1[-6 : -156 : -255])
# print(s1[-76 : 75 : 2])

# Get me the string after cutting off first 3 and last 5 characters.
# s1[3 : -5]

# Coming back to methods:
# Magical Methods/Dunder Methods
a = 5
b = 10
print(a + b)
# print(a.__add__(b))
print(type(a))

c = "5"
d = "15"
print(c + d)
# print(c.__add__(d))

# Next Class: Methods starting with 'd'