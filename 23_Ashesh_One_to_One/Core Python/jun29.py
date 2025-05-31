import random
# print(dir(random))
"""
count1 = 0
count2 = 0
for i in range(10000):
    # print((random.random() * 10) + 50)
    # print(random.uniform(50, 60))
    n = random.uniform(50, 60)
    if 50 <= n < 51:
        count1 += 1
    elif 51 <= n < 52:
        count2 += 1
print(count1)
print(count2)
"""
"""
for i in range(10):
    print(random.normalvariate(55, 1))
"""
# for i in range(10):
    # print(int(random.uniform(1, 7)))
    # print(random.randint(1, 6))
    # print(random.randrange(1, 7))


options = ["Rock", "Paper", "Scissors"]
for i in range(10):
    print(random.choice(options))