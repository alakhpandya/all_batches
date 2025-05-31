from _take_graph import takeGraph

expanded = []
def dfs(graph, start, goal):
    node = start
    if goal not in expanded:
        expanded.append(node)
        for child in graph[node]:
            dfs(graph, child, goal)
    return expanded


l = 2
def dls(graph, start, goal, count_of_level):
    if count_of_level > l:
        return expanded
    node = start
    if goal not in expanded:
        expanded.append(node)
        for child in graph[node]:
            dls(graph, child, goal, count_of_level+1)
    return expanded


# main:
# graph, start = takeGraph()
graph = {'s': ['a1', 'a2', 'a3'], 'a1': ['b1', 'b2', 'b3'], 'a2': ['b4'], 'a3': ['b5', 'b6'], 'b1': ['c1', 'c2'], 'b2': [], 'b3': ['c3'], 'b4': ['c4', 'c5', 'c6'], 'b5': [], 'b6': ['c7', 'c8'], 'c1': [], 'c2': [], 'c3': [], 'c4': [], 'c5': [], 'c6': [], 'c7': [], 'c8': []}
start = 's'
goal = 'c1'
# print(graph)
# goal = input("Goal State: ")
# path = dfs(graph, start, goal)

path = dls(graph, start, goal, 0)
print(path)