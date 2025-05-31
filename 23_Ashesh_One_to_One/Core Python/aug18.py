# Exception Handling
# print("Hello World!)

# eval("print('Happy Thursday!')")
while True:
    try:
        a = int(input("Enter two integers:\n"))
        b = int(input())
        break
    except ValueError:
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
    except ZeroDivisionError:
        print("You're trying to divide by zero, please choose any other operation...")
        # print("Something went wrong, please try again...")
    except KeyError:
        print("Invalid, please try again...")

    """
    if operation == "+":
        print(f"{a} + {b} = {a + b}")
    elif operation == "-":
        print(f"{a} - {b} = {a - b}")
    elif operation == "*":
        print(f"{a} * {b} = {a * b}")
    elif operation == "/":
        try:
            print(f"{a} / {b} = {a / b}")
        except ZeroDivisionError:
            print("You're trying to divide by zero, please choose any other operation...")
    else:
        print("Invalid, please try again...")
    """
    quit = input("Press 'q' to quit or 'Enter' to repeat: ").lower()
    if quit == 'q':
        break