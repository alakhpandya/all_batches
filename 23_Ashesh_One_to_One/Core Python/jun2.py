"""
result = {"Mihir":88, "Muskan":92, "Gopi":94, "Nisha":97}
# print(result.pop("Muskan"))
# print(result.popitem())
grades = {"Anant" : "B", "Om" : "A", "Ved" : "A+"}
result.update(grades)
# print(result)

print("Enter new key:value pair in dictionary:")
name = input("Name: ")              # Neena
marks = int(input("Marks: "))       # 97
# result[name] = marks
old_marks = result.setdefault(name, marks)
if old_marks == marks:
    print("Success!")
else:
    overwrite = input(f"Student {name} already exists with {marks} marks. Do you want to overwrite? Y/N").lower()
    if overwrite == "y":
        result[name] = marks
        print("Successfully overwritten!")
    else:
        print("Failed to add/update key-value pair...")
print(result)
"""

# functions:
"""
def function_name(arguments if any):
    code to be executed
    return return_value
"""
# import section

# global definitions (global variables)

# functions section

# main program
"""
Four types of functions:
1. without arguments (raw materials), without return (processed output)     -   printing some fixed message statically
2. with arguments, without return   -   printing matrix
3. without arguments, with return   -   scanning of matrix
4. with arguments, with return      -   most general
"""

def average(a, b):
    avg = (a + b)/2
    # print(f"Average of {a} & {b} is: {avg}")
    return avg

# average(5, 6)
# x = int(input("x = "))      # 5
# y = int(input("y = "))      # 10
# average(x, y)

a = int(input("a = "))      # 10
b = int(input("b = "))      # 20
p = average(a, b)           # 15

c = int(input("c = "))      # 30
d = int(input("d = "))      # 40
q = average(c, d)

# print("p =", p)
# print("q =", q)
print("Total of averages =", p + q)

# Advanced examples of List and Dictionary:
"""
1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.

3. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

4. Use dictionary to store antonyms of words (minimum 5 words). E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.

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