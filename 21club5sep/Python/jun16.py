# Example: Banking app
# users = []
# users.append("Name,Mobile no,User name,Password,Balance\n")
fp = open("account_holders.csv", "r")
users = fp.readlines()
fp.close()

while True:
    print("Press 1 to open new account")
    print("Press 2 to check balance of your account")
    print("Press 3 to deposite money")
    print("Press 4 to withdraw")
    print("Press 5 to exit")
    choice = int(input())
    if choice == 1:
        print("Enter the following details:")
        name = input("Name: ")
        mobile = input("Mobile No: ")
        user_name = input("User Name: ")
        password = input("Password: ")
        balance = "25000"
        users.append(f"{len(users)},{name},{mobile},{user_name},{password},{balance}\n")

    elif choice == 2:
        crn = input("Enter the following details:\nCRN: ")
        sr_no = int(crn[2:4])
        uName = input("User name: ")
        pwd = input("Password: ")
        user = users[sr_no].split(",")
        count = 3
        if user[3] == uName and user[4] == pwd:
            print("Your current balance is:", user[5])
        else:
            print("Incorrect username/password. Attempts left:", count)
            count -= 1
            if count == 0:
                print("Your account is blocked! Please contact your nearest branch.")

    elif choice == 3:
        pass

    elif choice == 4:
        pass

    elif choice == 5:
        break

print(users)

fp = open("account_holders.csv", "w")
users = fp.writelines(users)
fp.close()