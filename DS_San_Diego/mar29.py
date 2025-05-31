d = {"Physics":83, "Maths":88, "Python":99, "Computers":98, "Chemistry":84, "Maths":92}
# print(d)

k = d.keys()     # returns a 'list-object'
# print(k)
# for i in k:
#     print(i)

# print(d.values())

# print(d.items())

# for loop in dictionaries:
# fruits = ["Apple", "Kiwi", "Banana", "Mango"]
# for i in fruits:    # i = "Apple", "Kiwi"....

# for i in d:     # i = "Physics", "Maths"
    # same as 'for i in d.keys():'
    # print(i)

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

# Unpacking of tuples/Multiple assignment:
# stu_1, stu_2, stu_3 = ("Krushy", "Rushabh", "Alakh")
# print(stu_1)
# print(stu_2)
# print(stu_3)

# for i in d.items():     # i = ("Physics", 83), ("Maths", 92), ("Python", 99) ...

# print("Here is your result:")
# for subject, marks in d.items():
#     print(f"{marks} marks in {subject}")

# print(d.pop("Maths"))
# print(d)

# del d["Krushy"]
# d.pop("Krushy")
# print(d)

"""
a = d.popitem()
print("after first popitem:")
print(d)
print(a)
key_removed, value_removed = d.popitem()
print("after second popitem:")
print(key_removed)
print(value_removed)
print(d)
"""
# d2 = {"Environment" : 96, "Arts" : 77, "Physical Education" : 91}
# d3 = d + d2         invalid
# d.update(d2)

d = {"Physics":83, "Maths":88, "Python":99, "Computers":98, "Chemistry":84}
print(d)
# Ask a subject from the user and marks obtained. Add that subject & its marks in 'd'

sub = input("New subject: ")
marks = int(input("Marks obtained: "))

# d[sub] = marks
ret = d.setdefault(sub, marks)

print(d)
print("Returned value:", ret)

# Update your program such that if that subject exists in the dictionary then your program should ask user: "<subject> already present with <marks>, do you want to update it with new marks?"