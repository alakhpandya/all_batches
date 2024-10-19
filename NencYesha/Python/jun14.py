"""
Write a function that takes a string as input and returns another string that is obtained by changing every alternate character of the original string in upper case (Alternate means the characters lying at index 0, 2, 4, 6 etc)
"""
"""
def alternateCapitalize(word):  # word: "Python"
    # write your code here
    length = len(word)
    new_word = ""
    for i in range(length):  # i = "P", "y", "t"
        if i % 2 == 0:
            new_word = new_word + word[i].upper()
        else:
            new_word = new_word + word[i].lower()
    return new_word

s = input("Enter string: ")
print(alternateCapitalize(s))
# Output:
# PyThOn
"""

# Write a Python function that takes a string as input and returns True if the string is palindrom or False.

# reversing a string:
"""
s = "NencYesha"
s2 = s[ : : -1]
print(s2)
"""
def palin(s):
    s2 = s[ : : -1]
    return s == s2
    
# Ask a username & password from the user and if their username is a palindrome then print a message: "Wow! Your username is a palindrome!" using the above function.

username = input("Username: ")
password = input("Password: ")

if palin(username):
    print("Wow! Your username is a palindrome!")