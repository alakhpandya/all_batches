s1 = "Students of this batch are going to ROCK the software industry."

# Alignment related method
s2 = "Welcome to my Program!"
"""
s3 = s2.center(100)
print(s3)
print(len(s2))
print(len(s3))
print(s2.center(100, "$"))

s4 = s2.ljust(100, "#")
print(len(s4))
print(s4)

print(s2.rjust(100))
print(s2.rjust(100, "."))

print(" " + "="*100 + " ")
print("|" + s2.center(100) + "|")
print(" " + "="*100 + " ")
"""
"""
print(s1.count("y"))
print(s1.count("s", 9))
print(s1.count("s", 9, -5))
print(s1.count("are"))
print(s1.count("in", 20, 50))

print(s1.encode())

print(s1.endswith("try."))
print(s1.endswith("ing"))
print(s1.endswith("are", 10, -10))

print(s1.startswith("S"))
print(s1.startswith("this", 12))
"""
"""
print("Subject\tMarks".expandtabs(25))
print("Maths:\t95".expandtabs(25))
print("Environmental Science:\t89".expandtabs(25))
print("Python:\t98".expandtabs(25))
print("Chemistry:\t80".expandtabs(25))
print("C:\t96".expandtabs(25))
print("Computer Science:\t84".expandtabs(25))
print("C++:\t97".expandtabs(25))
"""
"""
print(s1.find("b"))
print(s1.find("o"))
print(s1.find("o", 10))
print(s1.find("o", 10, 30))
print(s1.find("oftw"))
print(s1.find("of", 10))
print(s1.find("z"))
print(s1.find("o", 10, 15))

print()
print(s1.index("b"))
print(s1.index("o"))
print(s1.index("o", 10))
print(s1.index("o", 10, 30))
print(s1.index("oftw"))
print(s1.index("of", 10))
print(s1.index("z"))

print(s1.rfind("o"))
print(s1.rfind("o", 10, 40))

print()
print(s1.rindex("o"))
print(s1.rindex("o", 10, 40))
"""
# Methods starting from 'is' : These all methods will always return either True or False
"""
s5 = "Welcome"
# print(s5.isalpha())
# print(s1.isalpha())
s6 = "2022"
print(s6.isnumeric())
s7 = "Welcome2022"
# print(s7.isalnum())
# print(s5.isalnum())
# print(s6.isalnum())
print(s6.isdecimal())   # considers strictly only digits 0 to 9. Nothing else.
print(s6.isdigit())     # Also recognise circled numbers, subscript, superscript

s8 = "5²"
s9 = "②⓪②②"
print(s8.isdecimal())
print(s8.isdigit())
print(s8.isnumeric())   # Also recognise roman numerals, vulgar fractions, numbers from other languages
print(s9.isdecimal())
print(s9.isdigit())
print(s9.isnumeric())

s10 = "Ⅷ"
print(s10.isdecimal())
print(s10.isdigit())
print(s10.isnumeric())

s11 = "½"
print(s11.isnumeric())

s12 = "二千二十二"
print(s12.isnumeric())

s13 = "२२२"
print(s13.isnumeric())
"""