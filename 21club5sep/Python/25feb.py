l1 = [54, 22, 44, 37, 96, 22, 83, 22, 65, 100, 22, 301]
"""
l1.clear()
print(l1)
del l1
print(l1)
"""
"""l2 = l1.copy()
print("l1 =", l1)
print("l2 =", l2)
l3 = l1
print("l3 =", l3)
"""
print(l1.count(22))
# print(l1.count(22, 4, 10))
l4 = (100,200,300)
# print(len(l1))
# l1.append(l4)
# l1.extend(l4)
# print(len(l1))
# print("l1 =", l1)
# print(l1.count(100))
# print(l1 + l4)    this will not work in case of two different collections
# l1.extend(l4)
# l1.extend("Harshil")
print("l1 =", l1)
print(l1.index(83))
print(l1.index(22))     # return index number of first occurance
print(l1.index(22, 4))
print(l1.index(22, 6, 10))

l1.insert(6, "Python")
print("l1 =", l1)

print(l1.pop())
print("l1 =", l1)
print(l1.pop(6))
print("l1 =", l1)

l1.remove(22)
print("l1 =", l1)

"""
Classwork:
Write a Python code to remove third occurrence of 22 from the above list
"""

# l1.reverse()
# print("l1 =", l1)

# l1.sort(reverse=True)
# l1.sort(key=sorting())
# print("Sorted l1 =", l1)
# l1.reverse()
# print("l1 =", l1)

"""
HW:
1. diff between .copy() and simple assignment

2. diff between .find() and .index()


# String Examples:

3. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
Example:
input string: Keep yourself mute while not speaking.
output: Keep_yourself mute while not#speaking.

4. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. 
Example:
input: Alakh Janakkumar Pandya
output: A.J.Pandya

5. Write a program to find the number of vowels, consonents and white space characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13

6. Write a Python code that prints the index numbers of all the occurrences of "o" in a given string of length 5.

7. Write a program to make a new string with the word "the" deleted in the given string.
eg:
input string: This is the lion in the cage.
output: This is lion in cage.

8. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.

List Examples:

1. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order. Now print both the lists.

2. Ask 10 numbers from the user and store them in a list. Now, ask user to enter a number between 1 to 10. Delete the element present at that index number and print the list. Now aks user to enter the number that he/she wants to delete. Delete that number itself from the list and print the resultant list.

3. Write a program to print average of all numbers of a list given by user.

4. Ask user for 10 numbers, store them in a list. Now :
    1. Print largest and smallest elements of a list.
    2. Split it into middle and store the elements in two dfferent lists.

"""
# Next Class: Operators in Python, Decision making, loops