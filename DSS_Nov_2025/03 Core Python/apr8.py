"""
1. Write a Python code that takes an integer from user and prints number of digits in that integer.
2. Write down a Python code that creates a user defined list of 'n' rows & 'm' columns.
3. Write a Python code to print each of the elements of a given list in a new line.
4. Write a Python function to find factorial of a number given in its argument. Develop a main program that takes five integers from user and print sum of their factorials using that function.
5. Make a Python program that uses a function to find average of 5 given numbers and write Python main program that takes 5 integers from user, uses the factorial function that you have already written in example-4 to find factorial of each one of them and using average function print the average of factorials of them.
6. Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    arithmetic progression:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d

7. Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.
8. Create a Python application for Data Science Society Bank:

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""

# Q-1
'''
n = int(input("n: "))
print("No. of digits =", len(str(n)))
'''
# Q-2
"""
n = int(input("Rows: "))
m = int(input("Columns: "))
'''
udf = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(input(f"a[{i}][{j}]: "))
    udf.append(temp)
'''
udf = [[input(f"a[{i}][{j}]: ") for j in range(m)] for i in range(n)]
print(udf)
"""
# Q-3:
"""
lst = [1,2,3]
for member in lst:
    print(member)
"""

# Q-4 & Q-5
"""
def fact(n):
    prod = 1
    for i in range(2, n+1):
        prod = prod * i
    return prod

def avg(a, b, c, d, e):
    return (a + b + c + d + e)/5

a1 = int(input("a1 = "))
a2 = int(input("a2 = "))
a3 = int(input("a3 = "))
a4 = int(input("a4 = "))
a5 = int(input("a5 = "))

# print(f"sum = {fact(a1) + fact(a2) + fact(a3) + fact(a4) + fact(a5)}")
avg_of_fact = avg(fact(a1), fact(a2), fact(a3), fact(a4), fact(a5))
print("avg of their factorial =", avg_of_fact)
"""

# Q-6
"""
# Normal way
def ap(a, d, n):
    return a + (n-1)*d

# Recursive way
def ap(a, d, n):
    if n == 1:
        return a
    else:
        return ap(a, d, n-1) + d
    
print(ap(5, 4, 6))
"""

# Q-7
# Regular function:
"""
def gp(a, r, n):
    return a * (r ** (n-1))

# Recursive function:
def gp(a, r, n):
    if n == 1:
        return a
    else:
        return gp(a, r, n-1) * r

# 5, 15, 45, 135
print(gp(5, 3, 4))
"""

# Q-8: DSS Bank

def open_ac():
    global balance
    u_name = input("Select a user name: ")
    pwd = input("Choose a password: ")
    balance = 25000
    return u_name, pwd

def login():
    u = input("Enter your user name: ")
    p = input("Type your password: ")
    if u == u_name and p == pwd:
        return True
    return False

def deposit():
    global balance
    amount = float(input("Enter the amount you want to deposit: "))
    balance += amount

def withdrawl():
    global balance
    amount = float(input("Enter the amount you want to withdraw: "))
    if balance - amount >= 10000:
        balance = balance - amount
        print(f"Amount of ₹ {amount} has been withdrawn successfully...")
    else:
        print("Insufficient balance, please try again with a different amount...")

def balance_check():
    print(f"Your latest balance is: ₹ {balance}")

balance = 0
u_name, pwd = open_ac()
while True:
    print("""
Press 1 to login
Press 2 to exit
    """)
    choice = int(input())
    if choice == 1:
        if login():
            while True:
                print("""
Press 1 for Deposit
Press 2 for Withdrawl
Press 3 to Check Balance
Press 4 to exit
                    """)
                ch = int(input())
                if ch == 1:
                    deposit()
                elif ch == 2:
                    withdrawl()
                elif ch == 3:
                    balance_check()
                elif ch == 4:
                    break
                else:
                    print("Please provide valid choice")

        else:
            print("Incorrect username or password, please try again...")
    elif choice == 2:
        break
    else:
        print("Please provide valid choice")