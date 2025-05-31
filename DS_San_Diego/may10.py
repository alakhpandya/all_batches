import random

# myList = []
# for i in range(1000):
#     n = random.randint(100, 2000)
#     myList.append(n)

# List Comprehension
myList = [random.randint(100, 2000) for i in range(1000)]
print(min(myList))
print(max(myList))