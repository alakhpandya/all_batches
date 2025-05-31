"""
myList = []
size = int(input("How many members do you want to add in myList?"))
i = 0
while i < size:
    temp = input(f"Enter {i}th element: ")
    myList.append(temp)
    i += 1
print(myList)

i = 0
while i < len(myList):
    print(myList[i])
    i += 1
"""
# for loop in range
# range(10)   =   0,1,2,3,4,5,6,7,8 & 9
# for x in range(10):
#     print(x)
# a = int(input("Enter lower limit: "))
# b = int(input("Enter upper limit: "))
# for x in range(a+1, b+1):
#     print(x)

# for ( i = 0; i < 10; i = i + 2)
# for x in range(a, b, 2):
#     print(x)

# Classwork: Make a Python program that counts the number of digits in the number entered by user
number = input("Enter any number: ")
print(len(number))