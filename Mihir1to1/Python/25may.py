# while else/ for else
"""
fruits = ["apple", "banana", "kiwi", "guava", "mango"]
choice = input("Enter name of the fruit: ")        # kiwi : kiwi is in the list    papaya : papaya is not in the list
flag = 0
for fruit in fruits:
    if fruit == choice:
        flag = 1
if flag == 1:
    print(f"{choice} is in the list")
else:
    print(f"{choice} is not in the list")
"""
"""
# using for... else
fruits = ["apple", "banana", "kiwi", "guava", "mango"]
choice = input("Enter name of the fruit: ")        # kiwi : kiwi is in the list    papaya : papaya is not in the list
for fruit in fruits:
    if choice == fruit:
        print(f"{choice} is in the list")
        break
else:
    print(f"{choice} is not in the list")
print("Thanks for using our program!")
"""
fruits = ["apple", "banana", "kiwi", "guava", "mango"]
choice = input("Enter name of the fruit: ")   
i = 0
while i < len(fruits):
    if choice == fruits[i]:
        print(f"{choice} is in the list")
        break
    i += 1
else:
    print(f"{choice} is not in the list")

"""
fruits = ["apple", "banana", "kiwi", "guava", "mango"]
choice = input("Enter name of the fruit: ")        # kiwi : kiwi is in the list    papaya : papaya is not in the list
if choice in fruits:
    print(f"{choice} is in the list")
else:
    print(f"{choice} is not in the list")
"""