# Learn PriorityQueue

from queue import PriorityQueue

def hamming_distance(node, end):
    d = 0
    for i in range(len(node)):
        for j in range(len(node)):
            if node[i][j] != end[i][j] and node[i][j] != 0:
                d += 1
    return d

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

def generateChildren(node):
    children = []

    # finding location of empty:
    for i in range(len(node)):
        for j in range(len(node)):
            if node[i][j] == 0:
                row, col = i, j
                break

    # moving empty up:
    if row > 0:
        temp = [row[:] for row in node]    # creating deep copy
        temp[row][col] = temp[row-1][col]
        temp[row-1][col] = 0
        children.append(temp)

    # moving empty down:
    if row < len(node)-1:
        temp = [row[:] for row in node]
        temp[row][col] = temp[row+1][col]
        temp[row+1][col] = 0
        children.append(temp)

    # moving empty right:
    if col < len(node)-1:
        temp = [row[:] for row in node]
        temp[row][col] = temp[row][col+1]
        temp[row][col+1] = 0
        children.append(temp)

    # moving empty left:
    if col > 0:
        temp = [row[:] for row in node]
        temp[row][col] = temp[row][col-1]
        temp[row][col-1] = 0
        children.append(temp)

    return children

def bfs(start, end):
    path=[]
    visited=[]
    queue=[]
    queue.append(start)
    visited.append(start)

    while queue:
        node=queue.pop(0)
        path.append(node)
        if node == end:
            print(f"BFS got: {node}")
            return path
        child_nodes=generateChildren(node)      # child_nodes=[c1, c2, c3]
        # print("Child nodes=", child_nodes)
        for child in child_nodes:   # child=c1
            if child not in visited:
                # print(child)
                queue.append(child)
                visited.append(child)
                
        # print()
    return False

# main
start = [
    [1,2,3],
    [4,5,6],
    [0,7,8]
]
end = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]
print("Start state:", start)
path = bfs(start, end)
for state in path:
    print(state)