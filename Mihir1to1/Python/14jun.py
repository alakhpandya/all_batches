# Class work:
"""
1. Ask user to give name and marks of 10 different students. Store them in dictionary.
2. Sort the above dictionary in ascending order of Marks.
"""
marks = {}
sorted_marks = {}
temp = []
print("Enter names & marks of 5 students:")
for i in range(5):
    print(f"student{i+1}:")
    name = input("Name: ")
    mark = int(input("Marks:"))
    marks[name] = mark
print(marks)
for key, value in marks.items():
    temp.append(str(value) + "_" + key)
temp.sort()
for string in temp:             
    temp2 = string.split("_")   # "5_a".split("_") => temp2 = ["5", "a"]
    sorted_marks[temp2[1]] = temp2[0]

print(sorted_marks)