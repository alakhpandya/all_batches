"""
val1=int(input("Enter number 1: "))
val2=int(input("Enter number 2: "))
if val1==1:
    val1+=1
while val1<=val2:
    flag= False
    i=2
    while i<=val1**0.5:
        if val1%i == 0:
            flag=True
            break
        i+=1
    if flag == False:
        print(val1,end=", ")
    val1+=1
print("\b\b.")
"""

# while else = break-else
# if-else
"""
n = int(input("n: "))   # 23
i = 2
while i < n:
    if n % i == 0:
        print("Composite.")
        break
    i += 1
else:
    print("Prime.")

    
fruits = ["apple", "mango", "banana", "cherries", "kiwi"]
fruit = input("Fruit name: ")
if fruit in fruits:
    print("Found!")
else:
    print("Not Found...")


i = 0
while i < len(fruits):
    if fruits[i] == fruit:
        print("Found!")
        break
    i += 1
else:
    print("Not Found...")
"""
# for loop
"""
fruits = ["apple", "mango", "banana", "cherries", "kiwi"]

# for(i = 0; i < len(fruits); i++)      i = 0,1,2,3,4
#   fruits[i]
favourite = input("Your favourite fruit: ")
for fruit in fruits:    # i = "apple", "mango", "banana", "cherries", "kiwi"
    print(fruit)
    if fruit == favourite:
        break
"""
"""
countries = ["India", "US", "UK", "Russia", "Brazil", "Japan"]
for country in countries:
    print(country)
"""

# range
range(5)    # 0 to 5: first included, last excluded
# print(range(5))

# for i in range(5):      # i = 0,1,2,3,4
# for i in range(5, 15):      # i = 5,6,7,8....,14
# for i in range(5, 15, 2):      # i = 5,7,9,11,...13

for i in range(15, 5, -1):  # i = 15, 14, 13.... 6
    print(i)


# Next Lectuer: Show me your leap year program.
    
"""
3. Write a Python program to find the largest of three numbers. 
Test Data : 12 25 52
Expected Execution:
1st Number = 12
2nd Number = 25
3rd Number = 52

52 is the largest number.

4. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 
Test Data : 
x-coordinate: 7
y-coordinate: 9
Expected Output :
The coordinate point (7,9) lies in the First quadrant.

5. Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
Eligibility Criteria : 
Marks in Maths must be atleast 65,
Marks in Phy must be atleast 55,
Marks in Chem must be atleast 50 and 
Total marks all three subject must be atleast 190 or Total in Maths and Physics >=140
Input the marks obtained in Mathematics :72 
Input the marks obtained in Physics :65 
Input the marks obtained in Chemistry :51 
Total marks of Maths, Physics and Chemistry : 188 
Total marks of Maths and Physics : 137 
The candidate is not eligible.


6. Take values of length and breadth of a rectangle from user and check if it is square or not.

7. A shop gives discount of 10% if the cost of purchased quantity is more than Rs.1000.
Ask user for quantity
Assume each item costs 100.
Calculate and print total amount to be paid by user.

8. In above program, ask user for his/her name, mobile number, quantity and price of each item, then decide whether he/she is eligible for discount and based on that print the invoice in the following format:
case 1- when customer is not eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              50          3               150
item-2              100         4               400
item-3              40          5               200
                                                ---------
                                Final Amount:   750
----------------Thanks for shopping with us!---------------

case 2- when customer is eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              90          3               270
item-2              100         4               400
item-3              40          10              400
                                                ---------
                                Grand Total:    1070
                                Discount:        107
                                                ---------
                                Final Amount:    963
----------------Thanks for shopping with us!---------------

9. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and years of service and print the final salary.
        
"""