import random

# print(dir(random))
"""
krushy_acharya - Variable Names/Function Names
krushyAcharya - Variable Names/Function Names
KrushyAcharya - Class Names
iPhone, eBay
"""

# for i in range(20):
#     x = random.random()     # returns a random number in the interval [0, 1)
#     print(x)

"""
count = 0
for i in range(1000000):
    x = random.random()
    if x == 0:
        count+=1
print(count)
"""

# Write a program that generates random numbers in the interval [5, 6)
# for i in range(20):
#     x = random.random() + 5
#     print(x)

# min: 0 + 5 = 5
# max: 0.999 + 5 = 5.999

# Write a program that generates random numbers in the interval [0, 10)
# for i in range(20):
#     x = random.random() * 10
#     print(x)

# min: 0 * 10 = 0
# max: 1 * 10 = 10

# Write a program that generates random numbers in the interval [5, 15)
# for i in range(20):
#     x = random.random() * 10 + 5
#     print(x)

# min: 0 * 10 + 5 = 5
# max: 1 * 10 + 5 = 15

# Write a program that generates random numbers in the interval [a, b)
# a = int(input())
# b = int(input())
# for i in range(20):
#     x = random.random() * (b - a) + a
#     print(x)

# Alternative to this in random module:
# for i in range(20):
#     print(random.uniform(25, 75))

# Write a program that generates random integers in the interval [1, 7)
# import math

# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(20):
#     # x = round(random.random() * (b - a) + a, 0)     # doesn't work
#     # x = int(random.random() * (b - a) + a)     # works with bugs
#     # x = math.floor(random.random() * (b - a) + a)     # works fine!
#     print(x)


# Write a program that generates random integers in the interval [-8, -2)
# min: (random.random() * (6)) - 8  = (0*6) - 8 = -8
# max: (random.random() * (6)) - 8  = (0.999*6) - 8 = 5.999 - 8 = -2.000001
# int(-2.00001) = -2
# floor(-2.00001) = -3

# dice_roll = []
# for i in range(20):
#     # print(random.randrange(1, 7))
#     dice_roll.append(random.randint(a=1, b=6))         # includes both a & b
# print(dice_roll)

# Why the name "uniform"?
"""
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for i in range(1000000):
    x = random.uniform(1, 101)
    if x <= 25: c1 += 1
    elif 25 < x <= 50: c2 += 1
    elif 50 < x <= 75: c3 += 1
    else: c4 += 1
print("c1 =", c1)
print("c2 =", c2)
print("c3 =", c3)
print("c4 =", c4)
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x = np.random.uniform(low=1, high=101, size=10000)
# sns.histplot(data=x)
# plt.show()

# alakh = np.array([50, 45, 40, 35, 30])
# krushy = np.array([38, 39, 40, 41, 42])
# print(alakh.mean())
# print(krushy.mean())

# for i in range(20):
#     print(random.normalvariate(mu=50, sigma=1))       # mu = mean, sigma = std. deviation

# x = np.random.normal(50, 2, size=10000)
# sns.histplot(data=x)
# plt.show()

# options = ["Rock", "Paper", "Scissors"]
# for i in range(20):
#     x = random.choice(options)
#     print(x)

# HW-1: Simulate a game where we ask user to choose from "Rock", "Paper" & "Scissors" then computer will choose one of them, if computer wins, 1 will be added to the score of computer & if user wins, 1 will be added to his/her score. If it is a tie then nothing to be added to anyone's score. The game will conduct such 20 rounds and at the end it will print both the scores, and also should declare the final winner.
"""
Rock Vs. Paper => Paper wins
Paper Vs. Scissors => Scissors win
Scissors Vs. Rock => Rock wins
"""

# HW-2: Do the above code without using random.choice()
"""
comp=0
user=0
options=["Rock","Paper","Scissors"]
for i in range(2):
    print("Round: ",i+1)
    uchoice=input().capitalize()
    cchoice=random.choice(options)
    print(cchoice)
    if (uchoice=="Rock" and cchoice=="Paper") or (uchoice=="Paper" and cchoice=="Scissors") or (uchoice=="Scissors" and cchoice=="Rock"):
        comp+=1
    elif (uchoice=="Rock" and cchoice=="Scissors") or (uchoice=="Scissors" and cchoice=="Paper") or (uchoice=="Paper" and cchoice=="Rock"):
        user+=1
if comp>user:
    print("Computer Wins")
else: 
    print("User Wins!")
print("Comp Score: ",comp, "User score: ", user)
"""