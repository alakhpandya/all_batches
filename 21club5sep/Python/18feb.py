"""s1 = "Students of this batch are going to ROCK the software industry and are also going to become most famous and richest programmars."
s2 = "$$$$$$$$$$$$$$$$$$$$$$$Holi ki dher sari shubhkamnaye...$$$$$$$$$$$$$$$$$"
print(s2.lstrip("$"))
print(s2.rstrip("$"))
print(s2.strip("$"))
s3 = "                        Holi ki dher sari shubhkamnaye...                             "
print(len(s3.strip()))
print(s3.strip() + "!")
print(s1.replace("i", "I"))
print(s1.replace("i", "I", 2))
"""
# Write a Python code that takes date & month number of 2022 from user and print them in dd-mm-yyyy format.
date = input("Enter date: ")
month = input("Enter month number: ")
print(f"The date you entered is: {date.zfill(2)}-{month.zfill(2)}-2022")
