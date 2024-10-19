# Python sum() function
"""
a = 15
b = 30
myList = [40, 50, 60]

print(myList)               # valid
print(sum(myList, a))       # valid
print(sum(myList, a+b))     # valid
print(sum(myList, a, b))    # invalid
"""

# Passing lists, tuples and dictionaries to a function

def avg(inputList):
    if len(inputList)==0:
        return 0
    else:
        return sum(inputList)/(len(inputList))

myList = [40, 50, 60]
avg(myList)

def percent(resultDictionary):
    sum = 0
    for marks in resultDictionary.values():
        sum += marks
    per = sum / len(resultDictionary)
    return round(per, 2)

result = {"Physics":98, "Computers":100, "Biology":80}
print(percent(result))

# How a function differentiate whether the input provided in the argument is a list or a tuple or a set? - It cannot/does not differentiate.