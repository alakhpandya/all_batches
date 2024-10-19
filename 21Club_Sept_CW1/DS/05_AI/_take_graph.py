def takeGraph():
    graph = {}
    root = input("Start state: ")
    no_of_children = int(input(f"No. of children of {root}: "))     # 3
    children = []
    for x in range(no_of_children):    # for x in range(3): for(x=0; x<3; x++)
        child = input(f"child-{x+1}: ")
        children.append(child)
    # print(children)
    graph[root] = children
    masterList = list(graph.values())
    # print("MasterList:", masterList)     # [[b1, b2, b3], [c1]]
    for nodeList in masterList:     # nodeList = [b1, b2, b3]
        # print("Nodelist:", nodeList)
        for node in nodeList:       # node = b1, b2, b3
            num_of_children = int(input(f"No. of children of {node}: "))
            childrenList = []
            for x in range(num_of_children):
                child = input(f"child-{x+1}: ")
                childrenList.append(child)
            # print("ChildrenList:", childrenList)
            masterList.append(childrenList)
            # if childrenList:
            graph[node] = childrenList

    return graph, root

if __name__ == "__main__":
    g = {"A":"B1", "A":"B2", "A":"B3"}
    g = {"B1":"A", "B2":"A", "B3":"A", "C1":"B1", "C2":"B2", "C3":"B2"}
    print(g)
    g = {"A":["B1", "B2", "B3"]}
    print(g)
    print(takeGraph())