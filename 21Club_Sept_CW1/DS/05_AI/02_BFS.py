from _take_graph import takeGraph           # graph={s:[a1,a2,a3], a1:[b1,b2], a3:[b3,b4]}

def bfs(graph, start, goal):
    # queue = [s]
    # queue = [a1, a2, a3]
    # queue = [a2, a3, b1, b2]
    queue = [start]
    expanded = []
    while queue:
        current_node = queue.pop(0)
        expanded.append(current_node)
        if current_node == goal:
            return expanded
        for child in graph[current_node]:
            queue.append(child)


graph, start = takeGraph()
print(graph)
goal = input("Goal State: ")
path = bfs(graph, start, goal)
print(path)

# Try to create BFS for 8 puzzle game
"""
1. Take inputs
2. Create Rules & Restrictions
"""