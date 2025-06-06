import random

# generating random numbers in interval [10, 90]
# for i in range(20):
#     print(random.random() * 80 + 10)
"""
count1 =0
count2 = 0
for i in range(100000):
    number = random.uniform(10, 90)
    if number >= 50:
        count1 += 1
    else:
        count2 += 1
print(count1)
print(count2)
"""
# normal distribution
# for i in range(20):
#     print(random.normalvariate(50, 1))

# print(dir(random))
# for i in range(10):
    # print(random.randint(1, 6))
    # print(random.randrange(1, 7))

# sample_set = ("Rock", "Paper", "Scissors")
# for i in range(10):
#     print(random.choice(sample_set))

# Monte Carlo simulation
"""
def random_walk(length):
    x = 0
    y = 0

    for i in range(length):
        move = random.choice(("N", "E", "W", "S"))
        if move == "N":
            y += 1
        elif move == "E":
            x += 1
        elif move == "W":
            x -= 1
        else:
            y -= 1
    # print(f"({x}, {y})")
    return (x, y)

for i in range(10):
    x, y = random_walk(6)
    distance = abs(x) + abs(y)
    print(distance)
"""
"""
Which is the longest path that leads to no-taxi on an average.
"""
"""
def random_walk(length):
    x, y = 0, 0
    for i in range(length):
        dx, dy = random.choice(((0, 1), (1, 0), (-1, 0), (0, -1)))
        x += dx
        y += dy
    return (x, y)

number_of_walks = 10000
sum = 0
# path_length = 12
print("Path length\tPercentage")
for path_length in range(10, 41):
    no_taxi = 0
    for i in range(number_of_walks):
        x, y = random_walk(path_length)
        distance = abs(x) + abs(y)
        if distance <= 5:
            no_taxi += 1
    percentage = no_taxi * 100 / number_of_walks
    print(f"{path_length}\t\t{percentage}")
"""
# Next class: Organizing our code in modules and packages