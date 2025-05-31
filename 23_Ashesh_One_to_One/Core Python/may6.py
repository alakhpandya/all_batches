"""
1. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. 
"""
# full_name = input("Enter your full name (First name + middle name + surname): ")
# print(full_name[0] + "." + full_name[full_name.index(" ") + 1] + "." + full_name[full_name.rindex(" ") + 1 : ])
# part1 = full_name[0]
# first_space_index = full_name.index(" ")
# part2 = full_name[first_space_index + 1]
# last_space_index = full_name.rindex(" ")
# part3 = full_name[last_space_index + 1 : ]
# print(part1 + "." + part2 + "." + part3)
"""
2. Write a program to find the number of vowels, consonents and white space characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13
"""
input_string = "Python Programming"
vowels = input_string.count("a") + input_string.count("e") + input_string.count("i") + input_string.count("o") + input_string.count("u")
print("vowels:", vowels)
len(input_string)

"""
word 'the' will be ______________ by the null character.
"""