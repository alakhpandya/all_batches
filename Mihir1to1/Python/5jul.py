# Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

# for example:
# list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
# input string = 'bug'
# output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']
"""
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'bug buggy bug bug buggy']
list2 = []
print(list1)
word = input("Enter any string: ")
for string1 in list1:
    ctr = string1.count(word)
    list2.append(str(ctr)+"_"+string1)
list2.sort()
list2.reverse()
list1.clear()
for string in list2:
    l3 = string.split("_")
    list1.append(l3[1])
print(list1)
"""
# Functions:
"""
1. without argument, without return --> 
2. with arguments, without return --> printing a matrix
3. without arguments, with return --> taking inputs in a matrix from user
4. with arguments, with return --> aria of a circle
# Defining a function:
def function_name(argument1, argument2, ...., argument n):
    code lines
    return 

# calling a function:
function_name(argument1, argument2, ...., argument n)
"""
# 1. without argument, without return
def good():
    print("Mihir & Jugal are good boys.")

good()
good()
good()

# Next Lecture: 2. with arguments, without return --> printing a matrix
