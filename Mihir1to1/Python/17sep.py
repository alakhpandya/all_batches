# Exception Handling
"""
while True:
    while True:
        print("Enter two integers:")
        try:
            a = int(input())
            b = int(input())
            break
        except ValueError:
            print("Only itegers please...")
    print("Press 1 to add")
    print("Press 2 to sub")
    print("Press 3 to mul")
    print("Press 4 to div")
    print("Press 5 to exit")
    choice = int(input())
    if choice == 1:
        print(f"{a} + {b} = {a+b}")
    elif choice == 2:
        print(f"{a} - {b} = {a-b}")
    elif choice == 3:
        print(f"{a} * {b} = {a*b}")
    elif choice == 4:
        try:
            print(f"{a} / {b} = {a/b}")
        except ZeroDivisionError:
            print("Can not divide by zero, please try with another value of 'b'.")
    elif choice == 5:
        break
    else:
        print("Invalid Operation, please try again...")
"""
"""
print("Enter two integers:")
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("Only itegers please...")
except ZeroDivisionError:
    print("Can not divide by zero, please try with another value of 'b'.")
"""
"""
print("Enter two integers:")
try:
    a = int(input())
    b = int(input())
    print(a / b)
except:
    print("Something went wrong... Please try again!")

print("Enter two integers:")
try:
    a = int(input())
    b = int(input())
    print(a / b)

except Exception as e:
    print(e)

else:
    print("This will be executed only if there is no excepetion.")

finally:
    print("This will be executed always")
"""
"""
while True:
    print("Enter two integers:")
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        print("Only itegers please...")
    else:
        print("Press 1 to add")
        print("Press 2 to sub")
        print("Press 3 to mul")
        print("Press 4 to div")
        print("Press 5 to exit")
        choice = int(input())
        if choice == 1:
            print(f"{a} + {b} = {a+b}")
        elif choice == 2:
            print(f"{a} - {b} = {a-b}")
        elif choice == 3:
            print(f"{a} * {b} = {a*b}")
        elif choice == 4:
            try:
                print(f"{a} / {b} = {a/b}")
            except ZeroDivisionError:
                print("Can not divide by zero, please try with another value of 'b'.")
        elif choice == 5:
            break
        else:
            print("Invalid Operation, please try again...")
"""
print("Enter two integers:")
try:
    a = int(input())
    b = int(input())
except ValueError:
    print("Only itegers please...")
else:
    print("Press 1 to do a + b")
    print("Press 2 to do a - b")
    print("Press 3 to do a * b")
    print("Press 4 to do a / b")
    choice = int(input())
    if choice == 1:
        if a < 0:
            raise Exception("Negative Not Allowed")
        print(f"{a} + {b} = {a+b}")
    elif choice == 2:
        print(f"{a} - {b} = {a-b}")
    elif choice == 3:
        print(f"{a} * {b} = {a*b}")
    elif choice == 4:
        print(f"{a} / {b} = {a/b}")
    else:
        print("Invalid Operation... Please try again")