# Passing a collection to the function
"""
def avg(n):
    return sum(n)/len(n)

l = int(input("How many numbers?\n"))
print(f"Enter {l} integers:")
myList = [int(input()) for x in range(l)]
myTuple = tuple(myList)
print(avg(myTuple))

marks = [23, 47, 49, 44, 38, 35]
print(avg(marks))
"""
# Variable length arguments
# Positional Arguments
# def avg(x, y):
#     pass

# avg(23, 45, 47)

# Default Arguments
"""
def avg(first_number = 0, *args):
    print("first =", first_number)
    print("args =", args)
    return (sum(args) + first_number)/(len(args)+1)

# print(avg(23, 47, 49, 44, 38, 35))
# print(avg(12, 14))
print(avg(23, 47, 49, 44, 38, 35))
# print(avg())
"""
"""
marks = {"English" : 23, "Science" : 47, "Maths" : 49, "Computers" : 44, "Physical Education" : 38}

def avg(result_dict):
    sum = 0
    for marks in result_dict.values():
        sum += marks
    return sum/len(result_dict)

print(avg(marks))
"""
# keyword arguments
"""
def printResult(**kwargs):
    # print(kwargs)
    print("Subject\tMarks".expandtabs(16))
    for sub, marks in kwargs.items():
        print(f"{sub}\t{marks}".expandtabs(16))

# printResult("English" = 23, Science : 47, 12 = 49, Physical Training = 38, computers = 43)
printResult(English = 23, Science = 47, Maths = 49, PT = 38, computers = 43)
"""
"""
first: All positional arguments
next: All default arguments
next: *args
last: **kwargs
"""