# filter(), reduce(), all(), any()
import random 

# Create a function that checks whether the number given in its argument is an armstrong number or not. Use that function and 'myList' to generate a new list i.e. 'yourList' which comprises only of armstrong numbers from 'myList'
"""
def armstrong(x):
    sum=0
    tmp=x
    while tmp>0:
        sum+=(tmp%10)**len(str(x))
        tmp=tmp//10
    if sum==x:
        return True
    else:
        return False

myList=[random.randint(10,10000) for i in range(10000)]

# yourList=[]
# for number in myList:
#     if armstrong(number):
#         yourList.append(number)

yourList = filter(armstrong, myList)

print(yourList)
"""

# Reduce:
"""
def absoluteAdd(a, b):
    return abs(a) + abs(b)

transactions = [random.randint(-1000, 1000) for i in range(5)]
print(transactions)
first_val = transactions[0]
# Write your code here that uses a for loop and the function 'absoluteAdd' to generate total transaction amount.
sum = absoluteAdd(first_val, transactions[1])
for i in range(2, len(transactions)):
    sum = absoluteAdd(sum, transactions[i])
print(sum)
"""
"""
transactions = [random.randint(-1000, 1000) for i in range(20)]
sum = 0
for number in transactions:
    sum += abs(number)
"""
"""
from functools import reduce

def absoluteAdd(a, b):
    return abs(a) + abs(b)

transactions = [random.randint(-1000, 1000) for i in range(5)]
reduce(absoluteAdd, transactions)
"""
"""
temp = absoluteAdd(t[0], t[1])
temp = absoluteAdd(temp, t[2])
temp = absoluteAdd(temp, t[3])
"""