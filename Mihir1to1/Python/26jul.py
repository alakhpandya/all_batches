# Passing Collections as arguments to the functions:
# strings, lists, tuples, sets, frozen sets, dictionaries are Collections in Python
"""
def func1(n):
    print(n)

a = int(input("Enter an integer: "))
func1(a)
b = input("Enter any string: ")
func1(b)
myList = [int(input()) for x in range(5)]
func1(myList)
myTuple = tuple(myList)
mySet = set(myList)
myFz = frozenset(myList)
func1(myTuple)
func1(mySet)
func1(myFz)
myDict = dict(x = 1, y = 2, z = 3)
func1(myDict)

def avg(collection):
    sum = 0
    for x in collection:
        sum += x
    return sum/len(collection)

r = int(input("How many integers do you want to insert in tuple?"))
print("Enter", r, "intgers:")
myList = [int(input()) for x in range(r)]
myTuple = tuple(myList)
print(f"Average of elements of {myTuple} is: {avg(myTuple)}")
"""
# *args : variable length arguments
"""
def avg(*args):
    print(args, type(args))
    sum = 0
    for x in args:
        sum += x
    return sum/len(args)

print(avg(5, 4, 12, 23, 88))
"""
# We may have positional arguments as well as *args both in a function like this:-
def avg(n, *args):
    sum = 0
    for x in args:
        sum += x
    return (sum + n)/(len(args) + 1)

print(avg(12, 66, 22, 88, 93))

# We may take as many positional arguments as we want. The only rule is ALL THE POSITIONAL ARGUMENTS MUST BE WRITTEN BEFORE *args.