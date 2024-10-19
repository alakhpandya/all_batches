"""
Make a Python program to print the following pattern using loops:
  *
 ***
*****
 ***
  *
"""

"""
# import math
from math import ceil

while True:
    row = int(input("Enter number of rows in star diamond: "))
    if row % 2 == 0:
        print("You can take only odd numbers as row! Please try again...")
    else:
        break
half_row = ceil(row/2)
row_no = 1
for x in range(1, row+1, 2):       # x = 1,3,5
    for i in range(half_row - row_no):
        print(" ", end = "")
    for y in range(x):
        print("*", end = "")
    print()
    row_no += 1
for x in range(row-2, 0, -2):
    for i in range(row_no - half_row):
        print(" ", end = "")
    for y in range(x):
        print("* ", end = "")
    print()
    row_no += 1
"""

"""
Make a Python program to print the following pattern using loops:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
"""