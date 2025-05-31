import random       # pseudo random number generator

# print(dir(random))
"""
c1 = 0
c2 = 0
c3 = 0
c4 = 0

for i in range(10000):
    # print(random.random())      # generates random number in the interval [0, 1)
    # print(random.random()*7 + 5)      # to generate random number in the interval [5, 12)
    # to generate random numbers in the interval [a, b): (b - a) * random.random() + a

    # number = random.random()*8 + 5  # in [5,13)
    # if number < 9:
    #     c1 += 1
    # else:
    #     c2 += 1

    # number = random.random()*4 + 5
    # if number < 6:
    #     c1 += 1
    
    # elif 6 <= number < 7:
    #     c2 += 1
    
    # elif 7 <= number < 8:
    #     c3 += 1
    
    # elif 8 <= number < 9:
    #     c4 += 1
    

print("c1 =", c1)
print("c2 =", c2)
print("c3 =", c3)
print("c4 =", c4)
"""

# print(random.uniform(5, 13))

"""
cypher: 
todays lecture

ceasor's cypher
wrg dbv ohf wxu h


RSA Encryption: two random prime numbers each of minimum 200 digits
"""
# u = 10
# sig = 1
# for i in range(30):
#     print(random.normalvariate(u, sig))

# from cmath import floor

# for i in range(20):
    # print(random.randint(1, 6))
    # print(random.randrange(1, 7))
"""
options = ["Rock", "Paper", "Scissors"]
# options[random.randrange(0, 3)]
for i in range(20):
    print(random.choice(options))
"""

# Monte Carlo Simulation