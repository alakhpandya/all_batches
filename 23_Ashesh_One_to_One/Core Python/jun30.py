from random import choice

def randomWalks(pathLength):
    """
    x = 0
    y = 0
    directions = ["N", "E", "S", "W"]
    for i in range(pathLength):         # 
        move = choice(directions)       # "N"
        if move == "N":
            y += 1
        elif move == "S":
            y -= 1
        elif move == "E":
            x += 1
        else:
            x -= 1
    """
    x, y = 0, 0
    for i in range(pathLength):
        dx, dy = choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


number_of_walks = 10000
print("Path length\t% of no taxi")
for path_length in range(5, 30):
    no_taxi = 0
    total_distance = 0
    for i in range(number_of_walks):
        x, y = randomWalks(path_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_taxi += 1
        # print(f"x = {x}\ty = {y}\tdistance = {distance}")
        # total_distance += distance
    # avg_distance = total_distance/number_of_walks
    # print(f"{path_length}\t\t{avg_distance}")
    percentage = (no_taxi*100)/number_of_walks
    print(f"{path_length}\t\t{percentage}")