"""
s1 = "Students of this batch are going to ROCK the software industry and are also going to become most famous and richest programmars."
s2 = "ifiswhiletryforTrue"
print(s2.isidentifier())
print(s1.islower())
print(s1.isupper())
print(s1.istitle())
s3 = "Students\tof\tthis\tbatch"
print(s3.isprintable())
print(s1.isprintable())
# print("Harshil is a good boy.", end="\n")
s4 = "        \t\n\t\n        \n\n  "
print(s4.isspace())
print(s1.split())
print(s1.split("s"))
print(s1.split("are"))
print(s1.split(" ", 3))

print(s1.rsplit(" ", 2))
print(s1.rsplit(" "))
s5 = "Today is Thursday.\nIt's a sunny day today.\nWe will go for hiking if it is not raining."
print(s5)
print(s5.splitlines())

print(s1.partition("are"))
print(s1.rpartition("are"))
s1 = "Students of this batch are going to ROCK the software industry and are also going to become most famous and richest programmars."
first = s1.index("are")
second = s1.index("are", first+1)
string1 = s1[:second]
string2 = s1[second:second+3]
string3 = s1[second+3:]

l1 = s1.split()
s6 = "_"
s7 = "Harshil"
print(s6.join(s7))
print("@".join(l1))
"""
contact = ["Priyansh", "9898912123", "30-02-1998", "priyansh@pmail.com"]
print(",".join(contact))
s1 = "Students of this batch are going to ROCK the software industry and are also going to become most famous and richest programmars."
# Next Class: Methods starting from "l"