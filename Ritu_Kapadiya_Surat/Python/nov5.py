"""
print("Sr.No.\t" + "Subject\t".expandtabs(25) + "Test1\tTest2")
print("1\t" + "C\t".expandtabs(25) + "20\t23")
print("2\t" + "Computers\t".expandtabs(25) + "20\t23")
print("3\t" + "Theory of Computation\t".expandtabs(25) + "20\t23")
print("4\t" + "java\t".expandtabs(25) + "21\t22")
print("5\t" + "Social Studies\t".expandtabs(25) + "21\t22")
print("6\t" + "html\t".expandtabs(25) + "24\t21")
"""
s1 = "today is Tuesday & Dipavali has just ended in INDIA."
"""
print(s1.find("D"))
print(s1.find("i"))
print(s1.find("i", 7))
print(s1.find("i", 21, 40))
print(s1.find("in"))
print(s1.find("z"))
print()

print(s1.index("D"))
print(s1.index("i"))
print(s1.index("i", 7))
print(s1.index("i", 21, 40))
print(s1.index("in"))
# print(s1.index("z"))

print(s1.rfind("i"))
print(s1.rfind("i", 10))
print(s1.rfind("i", 10, 40))
print()

print(s1.rindex("i"))
print(s1.rindex("i", 10))
print(s1.rindex("i", 10, 40))
"""

# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())

# print(s1.isalpha())
s2 = "RituKapadiya"
# print(s2.isalpha())
s3 = "987654321"
# print(s3.isnumeric())
s4 = "RituKapadiya987654321"
# print(s4.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())

# print(s3.isdecimal())
# print(s3.isdigit())
# print(s3.isnumeric())

s5 = "5²"
# print(s5.isdecimal())   # Recognizes only plain digits as numbers
# print(s5.isdigit())     # Also recognizes superscript, subscript, cirled numbers as numbers
# print(s5.isnumeric())   # Also recognizes roman numerals, vulgar fractions and numbers from other languages as numbers

# print(s1.isascii())
s6 = "forifisinTruewith"
# print(s6.isidentifier())

s7 = "Thank\tYou!"
# s1.isprintable()
# print(s7.isprintable())

s8 = "              \n\n\n\t         \t       \t\n       "
# print(s8.isspace())

s1 = "today is Tuesday & Dipavali has just ended in INDIA."
# print(s1.split())
# print(s1.split("a"))
# print(s1.split("a", 2))
# print(s1.rsplit("a", 2))
# print(s1.rsplit("a"))

# print(s1.split("Dipavali"))

s9 = """This is my first Python program! I don't feel afraid but
I am so much excited!
I have heard you can program "AI" using Python..."""
# print(s9.splitlines())

# print(s1.partition("Dipavali"))
# print(s1.partition("i"))
# print(s1.rpartition("i"))

myList = s1.split()
print(myList)
print("-".join(myList))
p = "#"
s10 = p.join(myList)
print(s10)

# Next Class: s1.strip