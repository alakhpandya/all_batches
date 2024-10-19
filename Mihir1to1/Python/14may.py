# Entry control loops: for & while
# There are no Exit control loops in Python
"""
number = int(input("Enter the number whose table you want to print: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    # There is nothing like i++ in Python
    i += 1
print("Thanks for using our program!")


print("Enter two numbers:")
number1 = float(input())
number2 = float(input())
while True:             # while (1)
    print("Enter:")
    print("1 to add")
    print("2 to subtract")
    print("3 to multiply")
    print("4 to divide")
    print("q to quit")
    choice = input()
    if choice == '1':
        print(f"{number1} + {number2} = {number1 + number2}")
    elif choice == '2':
        print(f"{number1} - {number2} = {number1 - number2}")
    elif choice == '3':
        print(f"{number1} * {number2} = {number1 * number2}")
    elif choice == '4':
        print(f"{number1} / {number2} = {number1 / number2}")
    elif choice == 'q' or choice == 'Q':
        break
    else:
        print("Invalid operation.. please try again!")
print("Thanks for using our program!")

"""

# for loop / for each loop / for in loop
fruits = ["Mango", "Apple", "Banana", "Kiwi", "Watermelon", "Guava"]
"""
for ( i = 0; i < 6; i++)
{
    printf(myList[i]);
}

for x in myList:
    if x == "Kiwi":
        # break
        continue
    else:
        pass
    print(x)
"""
for fruit in fruits:
    print(fruit)

# for loop in strings:
myString = "Happy Friday!"
for x in myString:
    print(x)