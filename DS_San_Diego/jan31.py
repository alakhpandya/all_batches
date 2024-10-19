s1 =    "Today is Wednesday in India and in San Diego it must be running Tuesday and it's a nice day!"
# index: 0123456789...............................................................................89
# -ve:                                                                                  ..987654321
# print(len(s1))

# print(s1.encode(encoding="utf-16"))

# startswith() & endswith()
# print(s1.endswith("day!"))
# print(s1.endswith("!"))
# print(s1.endswith("y!"))
# print(s1.endswith("ay!"))
# print(s1.endswith("y !"))

# print(s1.endswith("day", 5, 71))
# print(s1[70])

# print(s1.startswith("Tod"))
# print(s1.startswith("tod"))
# print(s1.startswith("Wed", 9))
# print(s1.startswith("Wed", 9, 29))

# s2 = "Hellosss\tWorld"
# print(s2)
"""
Sub     Test-1  Test-2
C       24      23
C++     21      22
Java    23      21
Python  25      25

print("Sub\tTest-1\tTest-2".expandtabs(25))
print("C\t24\t23".expandtabs(25))
print("Mathematics\t20\t19".expandtabs(25))
print("C++\t21\t22".expandtabs(25))
print("Machine Learning\t24\t25".expandtabs(25))
print("Java\t23\t21".expandtabs(25))
print("Artificial Inelligence\t25\t24".expandtabs(25))
print("Python\t25\t25".expandtabs(25))
"""
s1 =    "Today is Wednesday in India and in San Diego it must be running Tuesday and it's a nice day!"
# index: 0123456789...............................................................................89
# -ve:                                                                                  ..987654321
"""
print(s1.find("D"))
print(s1.find("must"))
print(s1.find("d"))
print(s1.find("dia"))
print(s1.find("d", 3))
print(s1.find("d", 12, 25))
print(s1.find("D", 2, 20))
print()

print(s1.index("D"))
print(s1.index("must"))
print(s1.index("d"))
print(s1.index("dia"))
print(s1.index("d", 3))
print(s1.index("d", 12, 25))
print(s1.index("D", 2, 20))
"""

# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())
# print(s1.isalpha())
"""
A string is called 'alpha' if:
1. It is not empty string. AND
2. It must not contain anything other than alphabets.
"""
s2 = "2024"
# print(s2.isalpha())
# print(s2.isnumeric())
"""
A string is numeric if:
1. It is not empty string. AND
2. It must not contain anything other than numbers.
"""
# HW: Find out the difference between isnumeric, isdecimal & isdigit
# print(s2.isdecimal())
# print(s2.isdigit())

s3 = "Feb2024"
# print(s3.isnumeric())
# print(s3.isalpha())
# print(s3.isalnum())
"""
A string is alpha-numeric if:
1. It is not empty string. AND
2. It must not contain anything other than numbers or alphabets.
"""
# print(s2.isalnum())
s4 = "February"
# print(s4.isalnum())
# print(s1.isascii())

s5 = "₹\n5000"
# print(s5.isascii())

# print(s1.isprintable())
# print(s5.isprintable())
s6 = "           \t\t\t          \n\n          \t\n           "
# print(s6.isspace())

# print("ifelseforisNoneinwhile".isidentifier())
# s1.isidentifier()

# print(s1.split())
# print(s1.split("i"))
# print(s1.split(" ", 3))
# print(s1.split(sep=" ", maxsplit=3))
# print(s1.split(maxsplit=3))

s1 =    "Today is Wednesday in India and in San Diego it must be running Tuesday and it's a nice day!"
# index: 0123456789...............................................................................89
# -ve:                                                                                  ..987654321

# print(s1.rsplit(" ", 3))
# print(s1.split("i"))    # ["Today ", "s Wednesday ", "n Ind", ... , "t's a n", "ce day!"]
# print(s1.rsplit("i"))   # ["Today ", "s Wednesday ", "n Ind",...., "t's a n", "ce day!"]

arr = ["Krushy", "is", "still", "a", "good", "girl"]
# char = "-"
# char = "-$-"
# print(char.join(arr))

# print("_".join(arr))

# print(s1.partition("San Diego"))        # only puts one cut and make 3 peices
# print(s1.rpartition("u"))

# print(s1.ljust(120, "~"))
# print(s1.rjust(120, "~"))
# print(s1.center(120, "~"))

s7 = "                      Happy Birthday               "
# print(s7)
# print(s7.lstrip())
# print(s7.rstrip())
# print(len(s7))
# print(len(s7.rstrip()))
# print(s7.strip())
# print(len(s7.strip()))

s8 = "$2$$$$$$$$$$$$$$$$$$$$$$$Happy$Birthday$$$$$$$$$$$$$$"
print(s8.strip("$"))