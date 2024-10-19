"""
while True:
    try:
        a = int(input("Enter two integers:\n"))
        b = int(input())
        break
    # except:             # handles every exception including keyboard interrupt
        # print("Please enter integers only... Try again.")
    except Exception:
        print("Please enter integers only... Try again.")

while True:
    operation = input("Enter operation: +, -, * or / : ")
    
    result = {
        "+" : 'print(f"{a} + {b} = {a + b}")',
        "-" : 'print(f"{a} - {b} = {a - b}")',
        "*" : 'print(f"{a} * {b} = {a * b}")',
        "/" : 'print(f"{a} / {b} = {a / b}")'
    }
    try:
        eval(result[operation])
    # except ZeroDivisionError:
    #     print("You're trying to divide by zero, please choose any other operation...")
        # print("Something went wrong, please try again...")
    # except KeyError:
    #     print("Invalid, please try again...")
    except Exception as e:
        # print("Something went wrong, please try again...")
        print(e)
"""

"""
while True:
    try:
        a = int(input("Enter two integers:\n"))
        b = int(input())
    
    except Exception:
        print("Please enter integers only... Try again.")

    else:       # will be executed only if there's no exception
        break

    finally:    # will be executed ALWAYS.
        print("Thank You!")
        # we put vital steps here like database disconnection, closing the file etc
print("Out of the loop.")
"""

# Next Class: Resource Management