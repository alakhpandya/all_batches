d1 = {"Physics":88, "Chemistry":94, "Maths":90}
# d1.clear()
# del d1["Chemistry"]
# del d1

d2 = d1.copy()
# d3 = d1

# Write a program that creates a dictionary with names of 5 people as keys and '10000' as their values.
users = ["Amit", "Sunder", "Rekha", "Nisha", "Priyanka"]
subsidy = dict.fromkeys(users, 10000)
print(subsidy)

print(d1.get("Physics"))
print(d1.get("Computers"))

subjects = d1.keys()
# print(subjects)
marks = d1.values()
print(marks)

subject_wise_marks = d1.items()
print(subject_wise_marks)

# for x in d1.values():
#     print(x)

# print(d1.pop("Maths"))
# print(d1)

# d1.popitem()
# print(d1)

# d1.update(subsidy)
# print(d1)

# print(d1.setdefault("Computers", 98))

# d1["Maths"] = 65
# print(d1.setdefault("Maths", 65))

print(d1)

"""
result = {"Physics":88, "Chemistry":94, "Maths":90}
Ask a key and its value from the user. If that key does not exist in the dictionary, add the key value pair and show user this output- "Subject X is successfully added with marks Y."
If the key already exists with some different marks, show user a message- "Subject X is already present with marks Y. Do you want to overwrite it, Y/N?" if user chooses "Y", overwrite the marks and print a message- "Subject X has been successfully overwritten with marks Y." And if, user chooses 'N' then leave the dictionary unchanged and print a failure message- "Key-value pair could not be updated."
"""

"""

"""