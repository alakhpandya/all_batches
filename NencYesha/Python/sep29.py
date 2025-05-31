myString = 'Nency has got her feet injured and Yesha does not like to play Garba that much and I am fond of Garba but I don\'t know how to play!'

# print(myString.count('e'))
# print(myString.count('Garba'))
# print(myString.count('as'))
# print(myString.count('es'))
'''
print(myString.count('e', 12))
print(myString.count('e', 22, 32))
print(myString.count('e', 2, 12))

# yourString = myString.replace('Garba', 'Cricket')
# print(yourString)

print(myString.replace('e', 'E', 3))
newString = myString.replace(" ", "_", 1)
revString = newString[ : : -1]
finalString = revString.replace(" ", "#", 1)
'''
"""
2. Write a program to find the number of vowels, consonents and white space characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13

3. Write a program to make a new string with the word "the" deleted in the given string.
eg:
input string: This is the lion in the cage.
output: This is lion in cage.

4. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
Example:
input string: Keep yourself mute while not speaking.
output: Keep_yourself mute while not#speaking.

"""
s1 = "NencYesha"
s2 = '987654321'
s3 = "NencYesha987654321"
# print(s1.isalpha())
# print(s2.isnumeric())
# print(s3.isalpha())
# print(s3.isnumeric())
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())


# print(myString.split())
# print(myString.split('and'))
# print(myString.split(" ", 5))
print(myString.rsplit(" ", 5))


# Next Class: partition, rpartition, join