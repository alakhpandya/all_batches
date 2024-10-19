# for-else  :   break-else
"""
n = int(input("Enter n: "))
for x in range(2, n):
    if n % x == 0:
        print("Not Prime.")
        break
else:
    print("Prime.")
"""
"""
if codition:
    # code line 1
    # code line 2
else:
    # code line 3
    # code line 4
"""
# while loop:
"""
i = 1
n = int(input("Enter n: "))
while i <= n:
    print(i)
    i += 1
"""
# infinte loops
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))

while True:
    print("Press 1 to add")
    print("Press 2 to subtract")
    print("Press 3 to multiply")
    print("Press 4 to divide")
    print("Press 9 to exit")
    choice = int(input())
    if choice == 1:
        print(f"{n1} + {n2} = {n1+n2}")
    elif choice == 2:
        print(f"{n1} - {n2} = {n1-n2}")
    elif choice == 3:
        print(f"{n1} * {n2} = {n1*n2}")
    elif choice == 4:
        print(f"{n1} / {n2} = {n1/n2}")
    elif choice == 9:
        break
    else:
        print("Invalid choice, please try again...")
"""

# while - else: same as for-else (break-else)

# break, continue & pass
"""
vegetables = ["tomato", "potato", "cabbage", "spinach", "Onion", "Lady finger", "", "cucumber", "Lemon"]
for veg in vegetables:
    if veg == "Onion":
        # break
        # continue
        pass
    print(veg)
"""
# tuple: Ordered & Immutable collections of members
"""
t1 = (11, 22, 33, 44, 11, 9, 13, 11, -56, 7.56, -15.87, 11, 37, 11)
t2 = 11, 22, 33, 44, 11, 9, 13, 11, -56, 7.56, -15.87, 11, 37, 11
print(t1)
print(t2)
t3 = ("Mumbai",)
print(t3)
print(type(t3))
t4 = 93,
print(t4)
print(type(t4))
# slicing is same as in other ordered collections, it gives you a new tuple.
# t1[5] = 500
print(t1.count(11))
# print(t1.count(11, 5, 10))        Error
print(t1.index(-15.87))
print(t1.index(11, 5, 10))
"""
# Unpacking of collections:
student_data = ["Ashesh", "Male", 24]

# name, gender, age = student_data
# print(f"Name:\t{name}\nAge:\t{age}\nGender:\t{gender}")

# name, gender, age, hobby = student_data
name, gender, age = student_data


# Homework:
"""
Loop examples:
1. Write a Python code that takes an integer from user and prints number of digits in that integer.
2. Write down a Python code that creates a user defined list
3. Write a Python code to print each of the elements of a given list in a new line
4. Write a Python program that prints whther the number given is a prime number or not.
5. Write a Python program that prints whther the number given is a perfect number or not.
6. Write a Python program that prints whther the number given is an Armstrong number or not.
7. Write a Python program that prints all the prime numbers between two integers given by user.
8. Write a Python program that prints all the perfect numbers between two integers given by user.
9. Write a Python program that prints all the Armstrong numbers between two integers given by user.
"""