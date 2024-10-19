# s1 = "2024"
# print(s1.isdecimal())     # Strictly recognize only 0-9 digits
# print(s1.isdigit())       # Recognizes 0-9, subscript, superscript, circled numbers
# print(s1.isnumeric())     # Recognizes 0-9, subscript, superscript, circled numbers, roman numerals, vulgur fractions, numbers from other languages

# s2="२०२४"
# print(s2.isdecimal())
# print(s2.isdigit())
# print(s2.isnumeric())

# s3 = "Ⅰ"
# print(s3.isdecimal())
# print(s3.isdigit())
# print(s3.isnumeric())

# s4 = "⅖"
# print(s4.isdecimal())
# print(s4.isdigit())
# print(s4.isnumeric())

# s5 = "5²"
# print(s5.isdecimal())
# print(s5.isdigit())
# print(s5.isnumeric())

# s6 = "二千二十四"
# print(s6.isdecimal())
# print(s6.isdigit())
# print(s6.isnumeric())

s1 = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum, consequatur vero quae et totam soluta delectus adipisci!"
# print(s1.removeprefix("Lorem "))
# print(s1.removesuffix("adipisci!"))

s2 = "Today is Wednesday in India and in San Diego it must be running Tuesday and it's a nice day!"
# print(s2.replace("day", "night"))
# print(s2.replace("day", "night", 2))

s3 = "Today is Wednesday in India.\nIn San Diego it must be running Tuesday.\nIt's a nice day!"
# print(s3.splitlines())

# date = input("Your date of birth(dd): ")
# month = input("Month of your birthday(mm): ")
# year = "2024"
# print(f"Your upcoming birthday is on: {date.zfill(2)}/{month.zfill(2)}/{year}")

# Collections in Python:
"""
ordered     mutable     list        []
ordered     immutable   tuple       ()
unordered   mutable     set         {}
unordered   immutable   frozenset   frozenset()

string: ordered & immutable collection of characters    " "/' '
dictionaries: unordered & mutable collection of key:value pairs     {}
"""
# List: Ordered & Mutable collection of members
l1 = [12, 15, 11, 26, 33, 45, 59]
# ind: 0,  1,  2,  3,  4,  5,  6
# -ve:-7, -6, -5, -4, -3, -2, -1
# print(len(l1))
l2 = [12, 15.43, 11.22, -26.4, 0, 33, 45, 59]
# print(l1)
# print(l2)
l3 = [12, 15.43, ["Mumbai", 10, -0.75], "San Diego", 11.22, "Ahmedabad", -26.4, 0, "USA", 33, "India", 45, 59]
# print(l3)
# print(len(l3))
# print(l3[2])
# print(len(l3[2]))

# print(l3[2][0])
# print(l3[2][0][3])

# myString = "This is February going on. I like this month."

# print(myString.split())
# print(myString.split()[2])

# print(l3[2][0].upper().center(50, "-").lstrip("-"))
