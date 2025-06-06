"""
1. Write a Python function that determines whether the number given in its argument is an Armstrong number or not. Write a supporting main program that takes two numbers from user and prints all the numbers those are not armstrong numbers between them.

2. Write a Python function that determines whether the number given in its argument is a perfect number or not. Write a supporting main program that takes two numbers from user and prints all the Perfect numbers between them.

3. Write a Python function that determines whether the number given in its argument is a prime number or not. Write a supporting main program that takes two numbers from user and prints all the prime numbers between them.
"""
"""
def armstrong(n):
    if len(str(n)) == 1: return False
    return True if sum([int(x)**len(str(n)) for x in str(n)]) == n else False

print("Enter two integers:")
a = int(input())
b = int(input())
print(f"Armstrong numbers between {a} and {b} are:")
for x in range(a, b+1):
    if armstrong(x):
        print(x)
"""
"""
x = 15
print("Enter two integers:")
a = int(input())
b = int(input())
if a < b:
    print(x)
if not (a < b):
    print(x+10)
"""
"""
Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""
"""
input_dictionary = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# print(input_dictionary.items())
output_list = []
for z in range(len(list(input_dictionary.values())[0])):
    temp = {}
    for x, y in input_dictionary.items():
        # print(x, "and", y[z])
        temp[x] = y[z]
    output_list.append(temp)
print(output_list)
"""
# Misc Topics of functions
# Docstrings
def armstrong(n):
    """This function returns True if n is Armstrong number otherwise returns false.
        And this is
            created by
                Fri 6pm Club batch.
    """
    if len(str(n)) == 1: return False
    return True if sum([int(x)**len(str(n)) for x in str(n)]) == n else False

print(armstrong.__doc__)
# armstrong()