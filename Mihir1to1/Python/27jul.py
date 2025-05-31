# **kwargs : key - word arguments
def func1(n):
    total_marks = 0
    for x, y in n.items():
        print(f"{x} relates {y}")
    for marks in n.values():
        total_marks += marks
    return total_marks

def avg(*args):
    return sum(args)/len(args)

def total_marks(**kwargs):
    print(kwargs)
    return sum(kwargs.values())

# myDict = {"Physics":48, "Maths":45, "English":42}
# print("Total marks :", func1(myDict))
print("Total Marks :", total_marks(Physics = 48, Maths = 45, English = 42, Biology = 35))
dict1 = {1:"Mihir", 2:"Dhiraj", 3:"Krishna"}

# Final Rule: In a function, we may take positional arguments, *args, **kwargs all together. The only rule is their order: 1st comes positional arguments, then *args & lastly **kwargs.

def func2(n1, n2, n3, *args, **kwargs):
    pass

# Next Lecture: Organizing our code in modules & packages