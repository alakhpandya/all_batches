# pass, continue & break statements
"""
fruits = ["apple", "banana", "kiwi", "grapes", "mangoes", "berries"]

# Print all the fruits in the list till "grapes" (including it)
i = 0
while i < len(fruits):
    print(fruits[i])
    if fruits[i] == "grapes":
        break
    i += 1
print("Here are all your fruits...")
"""
"""
Write a program that:
1. Ask user how many fruits they want to put in the list.
2. Take those many inputs from user and create a list of those fruits.
3. Print the list as it is.
4. Ask a fruit name from the user and print all the fruits of the list till that fruit (excluding it).
"""
"""
n = int(input("Number of fruits in the list: "))
fruits = []
i = 1
while i <= n:
    fruit = input(f"Fruit-{i}: ")
    fruits.append(fruit)
    i += 1
print(fruits)
"""



fruits = ["apple", "banana", "kiwi", "grapes", "mangoes", "berries", "grapes", "peach"]
fruit = input("Fruit that you don't like that much: ")  # grapes
i = -1
while i < len(fruits):
    i += 1
    if fruits[i] == fruit:
        continue
    print(fruits[i])
print("Here are all your fruits...")

# Output:
"""
banana, kiwi, grapes
"""