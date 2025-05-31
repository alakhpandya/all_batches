# Taking graph input:
# graph = {}

graph = {
    'a' : ['b1', 'b2', 'b3'],
    'b1' : ['c1'],
    'b2' : [],
    'b3' : ['c2', 'c3', 'c4'],
    'c1' : ['d1', 'd2'],
    'c2' : ['d3'],
    'c3' : ['d4', 'd5'],
    'c4' : [],
    'd1' : [],
    'd2' : [],
    'd3' : [],
    'd4' : [],
    'd5' : []
}


def graph_input():
    global graph
    node = input("Enter root node: ")
    no_of_children = int(input("Enter no of children of root node: "))
    print("Enter child nodes of root node:")
    root_children = [input() for x in range(no_of_children)]
    graph[node] = root_children
    master_list = []
    master_list.append(root_children)
    for children in master_list:
        if len(children) > 0:
            for child in children:
                no = int(input(f"Enter no of children of {child}:"))
                if no > 0:
                    print(f"Enter child nodes of {child}:")
                child_nodes = [input() for x in range(no)]
                master_list.append(child_nodes)
                graph[child] = child_nodes

# def bfs(node):
#     queue = []
#     opened = []
#     queue.append(node)
#     for node_to_expand in queue:
#         for child in graph[node_to_expand]:
#             queue.append(child)
#             # print("\n\nqueue:", queue)
#             # print("opened:", opened)
#         # queue.pop(0)
#         opened.append(node_to_expand)
#         # print("\n\nqueue:", queue)
    # print("opened:", opened)

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
    
    # Main
    # graph_input()
    # print(graph)
    bfs('a')

    # test = [11,21,13,41,51,16]
    # test.pop(0)
    # print(test)

    """
    dfs o/p: a b1 c1 d1 d2 b2 b3 c2 d3 c3 d4 d5 c4

    """