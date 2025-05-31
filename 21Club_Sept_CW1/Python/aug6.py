# s1 = "The largest democracy in the world is INDIA."
"""
print(s1.count("a"))
print(s1.count("is"))
print(s1.count("crac"))
print(s1.count("r"))
print(s1.count("r", 15))
print(s1.count("r", 15, 20))
print(s1.count("in", 15, 20))
"""

# print(s1.encode("utf-16"))
"""
print(s1.endswith("?"))
print(s1.endswith("."))
print(s1.endswith("INDIA"))
print(s1.endswith("INDIA."))
print(s1.endswith("IA."))

print(s1.endswith("y", 5, 21))
print(s1.endswith("y", 21))

print(s1.startswith("The"))
print(s1.startswith("T"))
print(s1.startswith("demo", 12))
print(s1.startswith("demo", 12, 30))
"""
"""
print("Subject\tMarks".expandtabs(15))
print("C\t93".expandtabs(15))
print("C++\t94".expandtabs(15))
print("Environment\t78".expandtabs(15))
print("java\t90".expandtabs(15))
print("python\t96".expandtabs(15))
"""
s1 = "The largest democracy in the world is India."
"""
print(s1.find("y"))
first = print(s1.find("i")) # = 20
print(s1.find("i", 23))
print(s1.find("i", 23, 50))
print(s1.find("g", 23, 50), end="\n\n")

print(s1.rfind("a"))
print(s1.rfind("i", 23, 50), end="\n\n")


print(s1.index("y"))
first = print(s1.index("i")) # = 20
print(s1.index("i", 23))
print(s1.index("i", 23, 50))
print(s1.index("g", 23, 50), end="\n\n")


print(s1.rindex("a"))
print(s1.rindex("i", 23, 50))
"""
# s2 = "94281 28473"
# s3= "9428128473"
# s4 = "AlakhPandya9428128473"
# s5 = "AlakhPandya"
# print(s1.isalpha())
# print(s2.isnumeric())
# print(s3.isnumeric())
# print(s4.isalnum())
# print(s5.isalnum())
# print(s5.isalpha())
# print(s3.isalnum())

s6 = "54.43"
s7 = "3415"
s8 = "5⁸"
# print(s8.isdecimal())   # considers strictly 0 to 9 as numbers
# print(s8.isdigit())     # considers subscript, superscript and also circled numbers as numbers
s9 = "②⓪②②"

# print(s9.isdecimal())
# print(s9.isdigit())
# print(s9.isnumeric())       # considers vulgar fractions, roman numerals and numbers from other languages

s10 = "½"

# print(s10.isdigit())
# print(s10.isnumeric())

s11 = "Ⅴ"
# print(s11.isdigit())
# print(s11.isnumeric())

s12 = "二千〇二十二"
# print(s12.isdigit())
# print(s12.isnumeric())

# print(s1.isascii())
# print(s10.isascii())

# print(s1.isprintable())
# s13 = "Hi\tThere!"
# print(s13.isprintable())

# print(s1.isidentifier())
# s14 = "isforinthisif"
# print(s14.isidentifier())


# print(s1.islower())
# print(s1.isupper())
# print(s1.istitle())

# print(s1.isspace())
# s15 = "    \t\t    \n   \t \n   \n\n  "
# print(s15.isspace())


s1.join()
# Next class: first learn .split(), .rsplit(), .splitlines(), .partition(), .rpartition() and then .join()