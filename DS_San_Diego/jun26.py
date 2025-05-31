# Monte Carlo Problem

# Generating random paths of length 7
"""
def GetRandomPath(path_len):
    from random import choice
    options = ["up", "down", "left", "right"]
    # path = []
    x, y = 0, 0
    for i in range(path_len):
        ch = choice(options)
        # path.append(ch)
        if ch == "up":
            y += 1
        elif ch == "down":
            y -= 1
        elif ch == "left":
            x -= 1
        else:
            x += 1
    # return path, x, y
    d = abs(x) + abs(y)
    return d

d = 0
n = 10
for i in range(10000):
    d = d + GetRandomPath(n)
avg_d = d/10000
print("Average distance from the hotel =", avg_d)
"""
def GetRandomPath(path_len):
    from random import choice
    x, y = 0, 0
    options = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for i in range(path_len):
        dx, dy = choice(options)    # dx = 0, dy = 1
        x = x + dx                  # x = 1, x = 2, x = 2
        y = y + dy                  # y = 0, y = 0, y = 1
    d = abs(x) + abs(y)
    return d

for path_len in range(10, 25):  # path_len=10,11,12 ... 24
    d = 0
    for i in range(10000):
        d = d + GetRandomPath(path_len)
    avg_d = d/10000
    print(f"Average distance from the hotel for path of length {path_len} =", avg_d)