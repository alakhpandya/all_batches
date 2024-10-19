# for loop:
# numbers = [11, 22, 33, 44, 11, 9, 13, 11, -56, 7.56, -15.87, 11, 37, 11]
# for x in numbers:
#     print(x)
"""
result = [
    [45, 46, 47],
    [39, 38, 37],
    [42, 43, 44]
]
i = 1
for x, y, z in result:        # x, y, z = [45, 46, 47]
    print(f"student-{i} got {x} in Maths, {y} in Computers and {z} in Science.")
    i += 1
"""
# list comprehension
# numbers = []
# for i in range(1, 101):
#     numbers.append(i)
# numbers = {i for i in range(1, 101)}
# numbers = [i for i in range(1, 101)]
# print(numbers)

# Armstrong number program: 
# n = int(input("Enter n: "))     #  371
# power = len(str(n)) # power = 3
# digits = []
# for x in str(n):    # for x in "371":   x = "3", "7", "1"
#     digits.append(int(x) ** power)
# if sum(digits) == n:
#     print("Armstrong.")
# else:
    # print("Not Armstrong.")

# n = int(input("Enter n: "))     #  371
# print("Armstron.") if sum([int(x)**len(str(n)) for x in str(n)]) == n else print("Not Armstrong.")

# n = "1234567890"
# even = [int(x) for x in n if int(x) % 2 == 0]
# print(even)

# for-else

# prime number