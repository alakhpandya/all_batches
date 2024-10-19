# Methods starting with 'is': These all methods always return True or False

# s2 = "AsheshThakor"
# s3 = "987654321"
# s4 = "AsheshThakor987654321"
# print(s1.isalpha())
# print(s2.isalpha())
# print(s3.isnumeric())
# print(s4.isnumeric())
# print(s4.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
"""
s5 = "2022"
print(s5.isdecimal())   # considers strictly plain digits from 0 to 9 only, nothing else
print(s5.isdigit())     # considers subscripts, superscripts and circled numbers also as numbers
print(s5.isnumeric())   # considers vulgar fractions, roman numerals, numbers from other languages
s6 = "2⁸"
print(s6)
print(s6.isdecimal())
print(s6.isdigit())
print(s6.isnumeric())
s7 = "②⓪②②"
print(s7)
print(s7.isdecimal())
print(s7.isdigit())
print(s7.isnumeric())
s8 = "¼"
print(s8)
print(s8.isdecimal())
print(s8.isdigit())
print(s8.isnumeric())
s9 = "二千二十二"
print(s9)
print(s9.isdecimal())
print(s9.isdigit())
print(s9.isnumeric())
s10 = "IV"
s11 = "Ⅵ"
print(s10)
print(s10.isnumeric())
print(s11)
print(s11.isnumeric())
"""
# s1 = "Python is fun at ROYAL\nwith all the faculties"
"""
print(s1.islower())
print(s1.isupper())
print(s1.istitle())
s12 = "forifiswhile"
print(s12.isidentifier())

print(s1.isprintable())
s13 = "            \n\t      \n        \t\t       \n"
print(s13.isspace())
"""
s1 = "Python is fun @ ROYAL with all the faculties."
"""
print(s1.split())
s2 = "Ashesh,Thakor,987654321,asheshthakor@gmail.com,Fremont,US"
print(s2.split(","))
print(s2.split(",", 3))
print(s2.rsplit(",", 3))
print(s2.rsplit(","))
"""
contact = ["Ashesh", "Thakor", "987654321", "asheshthakor@gmail.com", "Fremont", "US"]
"""
s14 = "_"
s15 = s14.join(contact)
print(s15)

print("#".join(contact))
"""
# cousines of split: partition(), rpartition()
s16 = "!!!!!!!!!!!!!!!!!!!!!!Happy Birthday!!!!!!!!!!!!!!!!!"
s17 = "$$$$$$$$$$$$$$$$$$$$$$$$$$Bumper Discount$$$$$$$$$$$$$$$$$$$$$"
s18 = "                Happy Independence Day                "
print(s16.lstrip("!"))
print(s16.rstrip("!"))
print(s16.strip("!"))
print(s18.strip())
# Next class: methods from partition()