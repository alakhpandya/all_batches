# Creating nested sets:
"""
s1 = {
    45,
    57.5,
    -0.8,
    (13, 14),
    "Nancy-Yesha",
    # {1,2,3}   Problem
    # [1,2,3]   Problem
    frozenset({1,2,3}),
    # {11 : 94, 12 : 89, 13 : 77}   # Problem
}

# We cannot nest mutable collections inside unordered collections.

print(s1)
"""
d1 = {1 : "Nancy", 21 : "Yesha", 3 : "Shrina", 4 : "Preyasi"}
# print(d1[21])
result = {
    "Math 140" : 3.9,
    "CMPSC 121" : 2.8,
    "ENGL 15" : 3,
    "PHYS 211" : 3.8
}


# print(d1)

# An empty dictionary:
empty = {}

# d1.clear()
# d2 = d1.copy()
# d2 = d1
# d1[3] = "New Person"
# print("d1=", d1)
# print("d2=", d2)

staff = ["Nancy", "Yesha", "Krishna", "Mahakksh", "Shrina", "Neev"]

# Adding a key:value pair to a dictionary:
# bonus["Nancy"] = 10000
# bonus["Yesha"] = 10000

# bonus = {}
# for x in staff:
#     bonus[x] = 10000

# bonus = dict.fromkeys(staff, 10000)
# print(bonus)

# print(result["ENGL 15"])
# print(result.get("ENGL 15"))

# all_subjects = result.keys()
# all_subjects.append("Mass Communication")
# all_subjects_list = list(result.keys())
# all_subjects_tuple = tuple(result.keys())

# import sys

# print("list size:", sys.getsizeof(all_subjects_list), "Bytes")
# print("tuple size:", sys.getsizeof(all_subjects_tuple), "Bytes")
# print("object size:", sys.getsizeof(all_subjects), "Bytes")

# print(all_subjects[0])
# for subject in all_subjects:
#     print(subject)


# credits = result.values()
# print(credits)

# print(result.items())

# for sub in result.keys():
#     print(sub)

# for credit in result.values():
#     print(credit)

# test = {
#     "Python" : (22, 24, 100)
# }
# items: ("Python", (22, 24, 100))

# for subject, credit in result.items():
#     print(f"Nancy & Yesha got {credit} credits in {subject}.")

d1 = {1 : "Nancy", 21 : "Yesha", 3 : "Shrina", 4 : "Preyasi"}
# print(d1)
# removed_employee = d1.pop(4)
# print(d1)
# print(removed_employee)

# removed_emp_id, removed_emp_name = d1.popitem()
# print(d1)
# print("Emp id that has been removed:", removed_emp_id)
# print("Name of that employee:", removed_emp_name)
# new_recruits = {
#     5 : "Mahakksh",
#     6 : "Neev"
# }
# d1.update(new_recruits)
# print(d1)

# Next class: setdefault