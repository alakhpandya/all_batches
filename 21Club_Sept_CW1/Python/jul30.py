b = 	   "We did not have class last week, so we had a practice session."
# index no: 0123456789...................................................61
# -ve index:.....................................................987654321
"""

print(b[3 : -5])
print(b[30 : 20])
print(b[30 : 19 : -1])

# b[5] = "p"
# print(b)

b = "We dip not have class last week, so we had a practice session."
print(b)
"""
# methods vs. functions
# functions: Can be applied on multiple datatypes
"""
type(b)
len(b)
print(b)
"""
# methods: are specific for one particular datatype
"""
# capitalize(b)	  wrong
b.capitalize()	# correct
"""
# string methods: can not change the original strings as they are immutable.
# b.capitalize()
# print(b)

s1 = "The largest democracy in the world is INDIA."
s2 = "you did it!"

# case-related methods
a = s1.capitalize()
print(s1)
print(a)
print(s2.capitalize())

print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())
print(s1.casefold())

s3 = "ß"
print(s3.lower())
print(s3.casefold())

# magical methods/dunder methods
"""
a = 5
b = 15
c = a + b   # c = a.__add__(b)
c = a.__add__(b)
print(c)
"""

# Alignment-related methods

# print(len(s1))
# b = s1.center(100)
# print(len(b))
# print(s1.center(100, "."))

# c = s1.ljust(100)
c = s1.ljust(100, "#")
# print(len(c))
print(c)
print(s1.rjust(100, "$"))

# Next Class: .count()