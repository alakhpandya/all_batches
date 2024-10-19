"""
s1 = 'Ritu is a '
s2 = "good girl."
# print(s1 + s2)      
print(s1.__add__(s2))
s3 = 5
s4 = 10
# print(s3 + s4)      # s3.__add__(s4)
print(s3.__add__(s4))
len(s1)
"""
s1 = "today is Tuesday & Dipavali has just ended in INDIA."
# s2 = s1.capitalize()
print(s1)
# print(s2)

# Case-related methods
# print("Capitalized -", s1.capitalize())
# print("Upper -", s1.upper())
# print("Title -", s1.title())
# print("Swapcase -", s1.swapcase())
# print("Lower -", s1.lower())
# print("Casefold -", s1.casefold())
"""
s2 = "What is ß"
print("Lower -", s2.lower())
print("Casefold -", s2.casefold())
"""

# Alignment related methods
"""
print(len(s1))
print(s1.center(100))
print(s1.center(100, "-"))

print(s1.ljust(100, "$"))
print(s1.rjust(100, "$"))
"""

# count
"""
print(s1.count("e"))
print(s1.count("da"))
print(s1.count("da", 10))
print(s1.count("da", 20, 40))
"""

# endswith & startswith
"""
print(s1.encode())
print(s1.encode("utf16"))

print(s1.endswith("?"))
print(s1.endswith("IA."))
print(s1.endswith("t", 20))
print(s1.endswith("t", 20, 40))

print(s1.startswith("today"))
print(s1.startswith("today", 20))
print(s1.startswith("t", 20, 30))
"""

# Next Class: s1.expandtabs()