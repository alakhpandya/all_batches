# Functions: We put () after function name only if either we want to define them or to call them.
"""
def wish():
    print("Get well soon!")

wish()

def incrementor(n):
    print("Incremented number =", n + 1)

print(incrementor(10))

def average(a, b):
    return (a + b)/2

x = float(input("Enter two numbers:\n"))    # 5
y = float(input())                          # 7

print(average(x, y))


RANK = 3
def scanMatrix():
    m = []
    for i in range(RANK):
        print(f"Enter {RANK} numbers for Row-{i}"):
        ith_row = []
        for j in range(RANK):
            ith_row.append(float(input()))
        m.append(ith_row)
    return m
"""

# Misc topics around functions:
# 3rd way to create strings:
s1 = """Weekend is starting from today.
            My wife says "We should plan to go to a resort.\""""
# print(s1)


# Docstring:
'''
import random

def incrementor(n):
    # docstrings
    """This function increments & prints the number in the argument by 1"""
    print("Incremented number =", n + 1)

print(incrementor.__doc__)
# print(random.choice.__doc__)
# random.choices()
# print(random.paretovariate.__doc__)
'''


# Copying a function
"""
favourite_function = incrementor
favourite_function(13)
"""
# deleting a function
"""
del incrementor

# incrementor(10)
favourite_function(10)
"""
# functions returning some condition
average = 25

def above_average(x):
    return x > average

temp = float(input("Enter temperature of the sensor: "))

if above_average(temp):
    print("Above average...")
else:
    print("Safe")

"""
Advanced examples of List and Dictionary:
1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.

3. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
5. Ask user to give name and marks of 10 different students. Store them in dictionary.
6. Sort the above dictionary by the names of students.
7. Sort the dictionary in ex-5 by the marks.
8. Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.
9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""

"""
Functions Examples:
1. Write a Python function to find factorial of a number given in its argument. Develop a main program that takes five integers from user and print sum of their factorials using that function.
2. Write a Python function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.


3. Make a Python program that uses a function to find average of 5 given numbers and write Python main program that takes 5 integers from user, uses the factorial function that you have already written in ex-1 to find factorial of each one of them and using average function prints the average of factorials of them.

4. Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    ap:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d

5. Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.

6. Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

7. Write a Python function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.

8. Write a Python function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.

9. Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""

# Next Class
# Some useful built in functions, lamda functions, scope of a variable, local variables, global variables & global keyword, nesting of functions, Recursive functions