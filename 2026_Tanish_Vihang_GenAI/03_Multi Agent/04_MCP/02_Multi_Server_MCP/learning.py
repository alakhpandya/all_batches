my_dict = {
    1 : "Python",
    2 : "C++",
    3 : "java",
    "course" : "Data Science"
}

# print(my_dict[2])
# print(my_dict["course"])
# print(my_dict["batch"])

# print(my_dict.get("course"))
# print(my_dict.get("batch", "Bad request."))
print(my_dict.get(3, "Bad request."))