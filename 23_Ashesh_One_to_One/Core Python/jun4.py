# Scope of a variable, local variables, global variables and global keyword.
"""
v1 = 10                                 # Global Variable

def func1():
    print("v1 through func1 =", v1)
    # print("v2 through func1 =", v2)
    v3 = 30                                 # Local variable of func1 available through the scope of func1
    print("v3 through func1 =", v3)
    def subFunc():                              # Local function/function with local scope
        print("v3 through subFunc =", v3)
    subFunc()

def func2():
    global v1, v2
    v2 += 1
    print("v2 through func2 =", v2)
    # subFunc()
    v1 = 100
    v1 += 1
    print("v1 through func2 =", v1)

print("v1 through main =", v1)
func1()
v2 = 20                                 # Global variable only for all those functions which are CALLED after this point.
# func1()
func2()
# print("v3 through main =", v3)
# subFunc()
print("v1 through main =", v1)
print("v2 through main =", v2)
# y = 100
# y += 1
"""
"""
import section

global section

function definition section

main program section
"""
# Lambda functions/Anonymous functions/Inline functions
from functools import reduce
from sys import getsizeof


def cube(n):
    return n ** 3

# cube = lambda n : n ** 3
# print(cube(5))


# Some built-in functions in Python

n = [2,2,3,4,5,6,7,8,9,10]
cubes = list(map(cube, n))
cubes_obj = map(cube, n)
print(cubes)
# for x in cubes_obj:
#     print(x)
# print(getsizeof(cubes))
# print(getsizeof(cubes_obj))

# trial = map(lambda x : x**3, n)

even = list(filter(lambda n : True if n%2 == 0 else False, n))
print(even)

ans = reduce(lambda a, b : a * b, n)
print(ans)

# Practice Examples of functions:
"""
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
"""
""" 5. Ask user to give name and marks of 10 different students. Store them in dictionary. """  
# Problem @ duplication
"""
result = {}

for n in range(1, 6):
    # tempResult = {}
    name = input("Name:")           # abc,  abc
    marks = int(input("Marks:"))    # 47,   82
    # tempResult[name] = marks
    oldResult = result.setdefault(name, marks)  # result = {"abc":47}
    if oldResult == marks:
        # result.update(tempResult)
        print("Success!")
    else:
        print(
            f"This {name} already exists with {oldResult} would you be overwriting? Y/N")
        ans = input().upper()
        if ans == 'Y':
            result[name] = marks
            print("Updated!")
        else:
            print("Kept same!")
print(result)
"""
"""
9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""
# input_dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
key_list = ["science", "language"]
value_list = [[88,89,62,95], [77,78,84,80]]
list_of_dictionaries = []
for j in range(len(value_list[0])):
    temp_dict = {}
    for i in range(len(key_list)):
        temp_dict[key_list[i]] = value_list[i][j]
    list_of_dictionaries.append(temp_dict)
print(list_of_dictionaries)