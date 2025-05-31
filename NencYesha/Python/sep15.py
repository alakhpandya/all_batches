s1 = "Today is THURSDAY and it looks like it will not rain, but forecast says that it will be a light rain."

# methods vs functions
# print(s1)
# print(type(s1))
# print(len(s1))

# string methods
# case related methods
s2 = "HAPPY THURSDAY!"
print(s2.lower())
# print(s2)

print(s1.capitalize())
print(s1.upper())
print(s1.title())
print(s1.swapcase())

# alignment related methods

print(s2.center(100))
print(s2.ljust(100))
print(s2.rjust(100))

print(s2.center(100, '$'))
print(s2.ljust(100, '$'))
print(s2.rjust(100, '$'))

# index finding methods
print(s1.index('D'))
print(s1.index('i'))
print(s1.index('i', 7))
try:
    print(s1.index('i', 23, 28))
except:
    print("character not found in the string!")
print(s1.index("like"))
# print(s1.rindex('i'))

print()
print(s1.find('D'))
print(s1.find('i'))
print(s1.find('i', 7))
print(s1.find('i', 23, 28))

