from dec28_BFS import graph

opened = []
def dfs(node):
    global opened
    if node not in opened:
        print(node, end=" ")
        opened.append(node)

        for child in graph[node]:
            dfs(child)

# main
dfs('a')