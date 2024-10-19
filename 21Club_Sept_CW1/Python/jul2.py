# this is how we do single line comments

'''
This is
multi line
comments
'''

"""
This is
another way 
to do multi
line comments
"""
# print("Alakh Pandya")
# print('9428128473')

# print("Alakh Pandya"     '9428128473')

# print("Alakh,Pandya",'9428128473')

"""
1. Across Python, we can replace pair of double quotes with pair of single quotes.
2. By default, Python print statement ends with "\n"
3. print statement gives a space between two arguments
"""

"""
Class work:

Print the following messages using Python:
1. Alpha said Beta "Gamma is teasing Delta".
2. Alpha said Beta "Gamma is teasing Delta but Gamma says that he didn't tease Delta."
3. The Python interpreter is at "C:\temp\new folder\Python315\"
4. In Python, "\t" is used to give 'tab' but if you want to "escape" it, you need to type "\\t".
"""
# print('Alpha said Beta "Gamma is teasing Delta".')
# print('The Python interpreter is at "C:\\temp\\new folder\\Python315\\"')

# Escape sequence characters:
"""
\	escape sequence character
\t	tab character
\n	new line character
\b	backspace
\r	carriage return
"""
# print("Python in Royal\b\b\b\b\bIndia")
# print("Python in Royal\rCoding")

# "end" statement:
# print("Welcome to Python.", end = "")
# print("Welcome to Python.", end = " ")
# print("Welcome to Python.", end = "\t")
# print("Welcome to Python.", end = "\b\b\b\b\b\b\b")
# print("Welcome to Python.", end = " Shubh ")
# print("The world of opportunities!")

# Creating variables
# a = 7
# a = 190489375140438957934876439802750931478069853701347889437984731985743098734098579238475098347268709578134591834709528734590875193847591459087149857439857981437589714305987349057984317589

# b = 5.5
# b = 542698723405987349786902570943759802734698724390857193874592087346092837459032479587235697029347589034759873245698072309467293475987342958732948057934278.02349857390487986792348750732495782394798679234759018374592734569873429875983247689342789574398758934279687349876983247597342702349875
# print("a")
# print(a)
# print("a =", a, "\nb =", b)
# print(type(a))
# print(type(b))

# c = 5 + 6j
# print("c =", c, "\nType of c =", type(c))

# Taking inputs:
print("Enter a number:")
a = int(input())
b = float(input("Enter another number: "))
print("a =", a)
print("b =", b)
print("a is:", type(a))
print("b is:", type(b))
# print("a + b =", int(a) + float(b))
print("a + b =", a + b)


"""
HW:

Write a Python program that exactly works as below:

Enter 5 integers:
1
2
3
4
5
The average of 1, 2, 3, 4 & 5 is: 3.0
"""