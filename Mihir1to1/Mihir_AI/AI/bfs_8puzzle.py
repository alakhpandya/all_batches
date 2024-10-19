def generate_children(node):
    # sliding empty up
    neighbor = node
    if not 0 in node[0]:
        #  empty in row1
        if 0 in node[1]:
            ind = node[1].index(0)
            neighbor[0][ind], neighbor[1][ind] = neighbor[1][ind], neighbor[0][ind]
        if 0 in node[2]:
            ind = node[2].index(0)
            neighbor[2][ind], neighbor[1][ind] = neighbor[1][ind], neighbor[2][ind]
    
    # sliding empty down
    if not 0 in node[2]:
        #  empty in row1
        if 0 in node[1]:
            ind = node[1].index(0)
            neighbor[0][ind], neighbor[1][ind] = neighbor[1][ind], neighbor[0][ind]
        if 0 in node[0]:
            ind = node[0].index(0)
            neighbor[0][ind], neighbor[1][ind] = neighbor[1][ind], neighbor[0][ind]

    # sliding empty left
    # if node[0][0] != 0 and node[1][0] != 0 and node[2][0] != 0:
    #     if 0 in node[0][1] or 0 in node[1][1] or 0 in node[2][1]:


def create_graph():
    start = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ]

    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    node = start
    no_of_children = generate_children(node)

def bfs(node):
        global queue, opened
        queue.append(node)
        while queue:
            temp = queue.pop(0)
            print(temp, end=" ")
            for child in graph[temp]:
                if child not in opened:
                    opened.append(child)
                    queue.append(child)


if __name__ == '__main__':
    queue = []
    opened = []
    
    # graph = create_graph()
    # bfs('a')

    start = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ]

    for row in range(3):
        ind = []
        if 0 in start[row]:
            ind.append(row)
            ind.append(start[row].index(0))
    print(ind)