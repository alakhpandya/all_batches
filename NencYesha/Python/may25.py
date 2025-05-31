employees = {"e_01" : "Nancy", "e_11" : "Yesha", "e_21" : "Shrina", "e_22" : "Preyasi"}
e_id = input("Employee id: ")   # e_23
name = input("Name: ")          # Neev
# employees.update(dict.fromkeys(e_id, name))
# employees[e_id] = name
var = employees.setdefault(e_id, name)
print("var =", var)
if var == name:
    print("Key-value pair added successfully!")
else:
    print(f"Key {e_id} has already been assigned value {var}")
    overwrite = input("Do you want to overwrite? Y/N: ").lower()
    if overwrite == "n":
        print("Could not add new key-value pair.")
    elif overwrite == "y":
        employees[e_id] = name
        print("Key-value pair updated.")
print(employees)

