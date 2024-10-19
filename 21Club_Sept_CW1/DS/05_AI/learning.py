"""
node = [
    [1,2,3],
    [4,5,6],
    [0,7,8]
]
# temp = [x for x in node]
# print(temp)

def hamming_distance(node, end):
    d = 0
    for i in range(len(node)):
        for j in range(len(node)):
            if node[i][j] != end[i][j] and node[i][j] != 0:
                d += 1
    return d

end = [
    [1,2,3],
    [4,5,6],
    [0,8,7]
]
print(hamming_distance(node, end))
"""
def manhattan_distance(node, end):
    d = 0
    for x1 in range(len(node)):
        for y1 in range(len(node)):
            if node[x1][y1] != 0:
                for i in range(len(node)):
                    for j in range(len(node)):
                        if node[x1][y1] == end[i][j]:
                            x2 = i
                            y2 = j
                            d += abs(y2-y1) + abs(x2-x1)
                            break
    return d

start = [
    [7,2,6],
    [5,0,4],
    [8,3,1]
]

goal = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
print(manhattan_distance(start, goal))