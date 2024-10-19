# with arguments without return:
"""
def avg(num1, num2):
    average = (num1 + num2)/2
    print(f"Average of {num1} and {num2} is: {average}")

print("Enter two numbers: ")
a = int(input())
b = int(input())
avg(a, b)
"""
def avg(num1, num2):
    average = (num1 + num2)/2
    # print(f"Average of {num1} and {num2} is: {average}")
    return average

print("Enter four numbers: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
total1 = avg(a, b) 
total2 = avg(c, d)
total = total1 + total2
print(total)

# Class work:
"""
1.Make a Python program that uses a function to find average of 3 given numbers and print it on the screen.

2.Make a Python program that uses a function that finds factorial of the number given in its argument.

3.Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.

4.Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.

5.Make a Python program that asks 5 numbers from user, finds their factorials using a function that takes 1 number in its argument & returns its factorial, adds all the factorials returned by function & prints the final answer on the screen.

6.Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()

HW:
7. Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.
"""