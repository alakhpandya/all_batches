# days = ["Mon", "Wed"]
# print("days list (before):", days)
# days.append("Fri")

# new_day = input("Which day do you want to add?\n")
# days.append(new_day)
# print("days list (after):", days)


# Try-except:
"""
while True:
    q = input("Enter 'exit' to quit or any other key to continue...\n")
    if q.lower() == "exit":
        break
    a = input("a : ")
    b = input("b : ")
    try:
        a = int(a)
        b = int(b)
        try:
            print("a / b =", a/b)
        except Exception as e:
            print("You are trying to divide by zero (which is impossible)! Please try again...")
            # print(e)
    except Exception as e:
        print("Your inputs are not possible to be converted to integers... Please try again!")

"""

# split()
st = "I am going to shift our luggage tomorrow."
words = st.split()
print(words)
print(words[:5])
print(" ".join(words[:5]))