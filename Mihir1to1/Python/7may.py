# myString = "Mihir Shah is the next tech-star from India"
"""
print(myString.encode())
print(myString.endswith("India"))
print(myString.endswith("ia"))
print(myString.endswith("a"))

print(myString.endswith("is the next ", 6, 23))
print(myString.startswith("Mihir"))
print(myString.startswith("Shah", 6, 23))

str1 = myString.replace(" ", "\t")
print(str1)
print(str1.expandtabs(16))

print(myString.find("S"))
print(myString.find("t"))
print(myString.find("t", 15))
print(myString.find("t", 22, 25))
print(myString.find("T"))

print()
print(myString.index("S"))
print(myString.index("t"))
print(myString.index("t", 15))
print(myString.index("t", 22, 25))
# print(myString.index("T"))

str2 = "MihirIsAGoodBoy"
str3 = "9428128473"
str4 = "Alakh9428128473"
print(myString.isalnum())
print(str4.isalnum())
print(str2.isalnum())
print()

print(myString.isalpha())
print(str4.isalpha())
print(str2.isalpha())
print()

print(str4.isnumeric())
print(str3.isnumeric())

str5 = "2021"
print(str5.isdecimal()) 
print(str5.isdigit())
print(str5.isnumeric())
print()
str6 = "5²"
print(str6.isdecimal())     # isdecimal => allows strictly 0 to 9 nothing else
print(str6.isdigit())
print(str6.isnumeric())
print()
str7 = "②⓪②①"
print(str7.isdigit())       # isdigit => 0 to 9, subscript, superscript, circled numbers
print(str7.isnumeric())
str8 = "二千〇二十一"
str9 = "Ⅶ"      # Taken from unicode table
str10 = "VII"      # Typed VII from keyboard
print(str8.isdigit())
print(str8.isnumeric())     # isnumeric => 0 to 9, subscript, superscript, circled numbers, vulger fractions, roman numbers, digits from other languages such as chinese, japanese, Hindi  etc
print(str9.isnumeric())
print(str10.isnumeric())
str11 = "२०२१"
print(str11.isnumeric())
"""
myString = "Mihir Shah is the next tech-star from India"

"""
print(myString.isascii())
str11 = "२०२१"
print(str11.isascii())
str12 = "for"
str13 = "Mihir studies Python for best career in Royal if it is Friday"
str14 = "iniffor"
print(str12.isidentifier())
print(str13.isidentifier())
print(str14.isidentifier())

print(myString.islower())
print(myString.isupper())
print(myString.istitle())
str15 = "Mihir\tShah\tis\tthe\tnext\ttech-star\tfrom\tIndia"
print(myString.isprintable())
print(str15.isprintable())

str16 = "\t\n    \t"
print(str16.isspace())
"""
str17 = "Mihir Shah is the next tech-star from India.\nHe is bright star of PDPU.\nHe also is one of the best students of Royal"

list1 = myString.split(" ")
print(list1)
print(myString.split(" ", 3))

print(str17.splitlines())
print(myString.rsplit(" ", 3))
print(myString.rsplit(" "))

str18 = ",".join(list1)
print(str18)

print(myString.ljust(150, "."))
print(myString.rjust(150, "."))

str19 = "...........Fill this blank....."
print(str19.lstrip("."))
print(str19.rstrip("."))
print(str19.rstrip("blank"))
