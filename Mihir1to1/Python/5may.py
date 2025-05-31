# Difference between methods & functions
# functions
myString = "Mihir Shah is the next tech-star from India"
print(len(myString))
print(type(myString))
number1 = 15
print(type(number1))
# Methods
# str1 = myString.capitalize()
# print(myString)                   Strings are immutable so no method of string changes the original.
# print(str1)
print(myString.capitalize())
print(myString.upper())
print(myString.lower())
print(myString.casefold())

str1 = "miß"
print(str1.lower())
print(str1.casefold())
print(myString.swapcase())
print(myString.title())

yourString = "Welcome to well-being log program"
print("=".center(50, "="))
print("|", yourString.center(46, " "), "|")
print("=".center(50, "="))

print(myString.count("i") + myString.count("I"))
print(myString.count("I", 21))
print(myString.count("I", 15, 35))
