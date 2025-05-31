l = [12, 15.43, ["Mumbai", 10, -0.75], "San Diego", 12, "Ahmedabad", -26.4, 0, "USA", 12, 33, "India", 45, 12, 59]

# print(l.index("Ahmedabad"))
# print(l.index(12))
# print(l.index("Mumbai"))

# print(l.index(12, 1))

# A list is given to us where every element (integer) of the list is repeated at least 3 times. Write a program that takes an integer input from the user and prints index number of third occurance of that integer.
"""
myList = [10, 15, 10, 29, 13, 14, 10, 15, 15, 29, 15, 10, 13, 45, 13, 14, 29, 45, 14, 45]
print(myList)
a = int(input("a: "))
p = myList.index(a)
q = myList.index(a, p+1)
r = myList.index(a, q+1)
print(f"Index number of third occurrance of {a} is: {r}")
"""
myList = [10, 15, 10, 29, 13, 14, 10, 15, 15, 29, 15, 10, 13, 45, 13, 14, 29, 45, 14, 45]
"""
myList.insert(5, 500)
print(myList)

print(myList.pop())        # will pop out the last element
print(myList.pop(5))       # will pop out the element at index 5

print(myList.remove(29))   # remove first occurrance of 29
print(myList)
"""

print(myList)
# myList.reverse()
# print(myList)

# myList.sort(reverse=True)
# myList.reverse()
# print(myList)

sorted_list = sorted(myList, reverse=True)
print(myList)
print(sorted_list)

myString = "Ahmedabad"
print(sorted(myString))
yourString = "Surat is a nice city!"
print(sorted(yourString))
# output: ['S', 'a', 'r', 't', 'u']

print(max(myList))
print(min(myList))

fruits = ["apple", "mango", "banana", "cherries", "kiwi"]
print(sorted(fruits))