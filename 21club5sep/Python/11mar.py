"""
fruits = ["Apple", "Banana", "Kiwi", "Mango", "Grapes", "Orange"]
asia = ["India", "Nepal", "Shrilanka", "South Korea", "China", "Pakistan"]
for fruit in fruits:    # i = "Apple", "Banana", "Kiwi", "Mango", "Grapes", "Orange"
    if fruits.index(fruit)%2 != 0:
        print(fruit)

for country in asia:
    print(country)
"""
# for loop in strings
"""
s1 = "PM is visiting our town today."
for character in s1:
    print(character)
"""
"""
for(i=0; i<10; i++)
"""
# range(5): 0,1,2,3,4
# for loop in range:
"""
for x in range(10):
    print(x)
"""
"""
for(i=-10; i<=10; i++)
"""
"""
for x in range(-10, 11):
    print(x)
"""
"""
for(i=-10; i<=10; i = i + 2)
"""
"""
for x in range(-10, 11, 2):
    print(x)

for x in range(10, -11, -1):
    print(x)
"""
# for-else: break-else
"""
n = int(input("Enter n = "))
for x in range(2, n):
    if n % x == 0:
        print("Not Prime.")
        break
else:
    print("Prime.")
"""
# 3 x 3 Matrix
# m1 = [[1,2,3], [4,5,6], [7,8,9]]
"""
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(m1)
# for x in m1:    # x = [1,2,3], [4,5,6]
#     for y in x:
#         print(y)
print(m1[0][2])
for row in m1:
    for number in row:
        print(number, end="\t")
    print()
"""
result = [
    ["Vishva", 96, "AI"],
    ["Rushir", 78, "Data Science"],
    ["Anuj", 83, "Machine Learning"],
    ["Neepa", 89, "Web Development"]
]

# x, y = ["Vishva", 96]
for x, y, z in result:    # x, y = ["Vishva", 96]
    print(f"{x} got {y} marks in {z}")