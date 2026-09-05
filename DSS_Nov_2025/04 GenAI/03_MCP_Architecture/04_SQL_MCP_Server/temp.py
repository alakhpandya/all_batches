# a = int(input("a = "))
# b = int(input("b = "))

# print("Division =", a/b)
"""
while True:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        print("Division =", round(a/b, 2))
        break

    # except ZeroDivisionError:
    # except:
    except Exception as e:
        # print("Cannot divide by zero!")
        # print(e)
        print("Something went wrong,")
        print("Try again...")

    print("Thanks for using our program!!")

    # finally:
    #     print("Thanks for using our program!!")
"""
"""
try:
    a = int(input("a = "))
    b = int(input("b = "))
    print("Division =", round(a/b, 2))

except Exception as e:
    print(e)

# print("Thanks for using our program!!")

finally:
    print("Thanks for using our program!!")
    
"""

column_names = ["customer_id", "name", "city"]
row = (1,"Alice","Ahmedabad")

print(dict(zip(column_names, row)))