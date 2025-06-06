"""
restaurent = {
    "Priyansh":"Ras-Puri",
    "Dhiraj": ("Khichdi", "Kadi", "Buttermilk"),
    "Tejas": 13,
    "Samir": ["Soup", "Sabji-Roti", "Icecream"],
    "Alakh": {"Soup", "Sabji-Roti", "Icecream"},
    "Rahul": {"BF":"Maggie", "Lunch":"Punjabi", "Dinner":"Gujarati"}
}
name = input("Whose food do you want to see?")
if name == "Priyansh" or name == "Tejas":
    print(restaurent[name])
elif name == "Rahul":
    meal = input("Which meal do you want to see? BF/Lunch/Dinner?")
    print(restaurent[name][meal])
else:
    for x in restaurent[name]:
        print(x)
"""
"""
d1 = {"Physics":83, "Maths":88, "Python":99, "Computers":98, "Chemistry":84}
# print(d1.pop("Computers"))
# print(d1.popitem())
print(d1)
d2 = {"Ahmedabad":42, "Gandhinagar":37, "Dwarika":32}
# d1.update(d2)
# print(d1)
# d1["Python"] = 89
# print(d1)
# print(d1.setdefault("Python", 72))
# print(d1)
# d1["C"] = 94
# print(d1.setdefault("C", 94))
# print(d1)

subject = input("Enter new subject: ")      # C, Python
new_marks = int(input("Marks: "))           # 72, 88
old_marks = d1.setdefault(subject, new_marks)
if old_marks == new_marks:
    print(f"{subject} successfully added with {new_marks} marks")
else:
    print(f"{subject} already exists with marks {old_marks}")
    overwrite = input("Do you want to overwrite? Y/N?").lower()
    if overwrite == "y":
        d1[subject] = new_marks
        print(f"{subject} successfully overwritten with {new_marks} marks")
    else:
        print(f"key-value updation failed.")
print(d1)
"""
# Iterating through a dictionary using for loop
# d1 = {"Physics":83, "Maths":88, "Python":99, "Computers":98, "Chemistry":84}
# for x in d1:          # as good as: for x in d1.keys():
#     print(x)

# for x in d1.values():
#     print(x)

# for x in d1.items():
#     print(x)

# for x, y in d1.items():
#     print(f"I got {y} marks in {x}")
"""
Practice Examples:
1. Ask user to give name and marks of 10 different students. Store them in dictionary.

2. Create a Python program to generate user-defined set. Then ask user to enter any value & check if the given value is present in a set or not.

3. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.

5. Sort the dictionary in example-1 by the names of students.

7. Sort the dictionary in example-1 by the marks.

8. Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.

9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""