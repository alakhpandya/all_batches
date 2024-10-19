# 
"""
fav_cars = {"Dhiraj":"Ferrari", "Ashehsh":"Audi S7", "Alakh":"Evoque", "Rahul":"Bugati"}
print("Dhiraj" in fav_cars.keys())
print("Audi S7" in fav_cars.values())
print("Tejas" in fav_cars)
"""
# Explicit Memoization

cache = {}      # cache = {2:1, 1:0, 3:1, 4:2, 5:3}
def improved_fibonacci(n):      # n = 5, 4, 3, 2, 1
    if n in cache:
        return cache[n]

    if n == 1:
        cache[n] = 0    # {1 : 0}
        return 0
    
    elif n == 2:
        cache[n] = 1    # {1 : 0, 2 : 1}
        return 1

    else:
        temp = improved_fibonacci(n-1) + improved_fibonacci(n-2)    # f(4)+f(3), f(3)+f(2), f(2)+f(1)
        cache[n] = temp
        return temp

t = int(input("Enter t: "))
print(f"Fibonacci sequence till {t}th term are:")
# print(improved_fibonacci(40))
print("Term No\tValue")
for x in range(1, t+1):
    print(f"{x}\t{improved_fibonacci(x)}")

print(cache)