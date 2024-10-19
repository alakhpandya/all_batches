# PriorityQueue
from queue import PriorityQueue
"""
q = PriorityQueue()
q.put((2, 'B1'))
q.put((1, 'B2'))
q.put((3, 'B3'))
q.queue.clear()
# print(q.get())
# print(q.get())
# print(q.get())
print(q.empty())
"""

class Problem():
    def __init__(self):
        # self.graph = {}
        # self.getGraph()
        self.graph = {
            'A' : [(2, 'B1'), (1, 'B2'), (3, 'B3')],
            'B1' : [(5, 'C1'), (1, 'C2')],
            'B2' : [(3, 'C3')],
            'B3' : [(6, 'C4'), (0, 'C5')],
            'C1' : [(2, 'D1')],
            'C2' : [],
            'C3' : [(1, 'D2'), (3, 'D3')],
            'C4' : [],
            'C5' : [(3, 'D4')],
            'D1' : [],
            'D2' : [],
            'D3' : [],
            'D4' : []
        }

    def getGraph(self):
        node = input("Enter root node: ")
        no_of_children = int(input("Enter no of children of root node: "))
        print("Enter child nodes of root node:")
        root_children = []
        for n in range(no_of_children):
            child_node = input("Node: ")
            child_cost = int(input("Cost: "))
            root_children.append((child_cost, child_node))
        self.graph[node] = root_children
        master_list = []
        master_list.append(root_children)
        for children in master_list:    # children is a list of tuples
            if len(children) > 0:
                for child in children:  # child is a tuple like (2, 'B')
                    no = int(input(f"Enter no of children of {child[1]}:"))
                    if no > 0:
                        print(f"Enter child nodes of {child[1]}:")
                    child_nodes = []
                    for n in range(no):
                        child_node = input("Node: ")
                        child_cost = int(input("Cost: "))
                        child_nodes.append((child_cost, child_node))
                    master_list.append(child_nodes)
                    self.graph[child[1]] = child_nodes

    def isGoalState(self, node, goal):
        return node == goal

    def ucs(self):
        visited = []
        pq = PriorityQueue()
        start = input("Start State: ")
        goal = input("Goal State: ")
        pq.put((0, start))

        while not pq.empty():
            child = pq.get()
            current_node = child[1]
            current_node_cost = child[0]
            if self.isGoalState(current_node, goal):
                print(current_node)
                pq.queue.clear()

            else:
                if current_node in visited:
                    continue
                print(current_node)
                visited.append(current_node)
                for child in self.graph[current_node]: # for child in [(2, 'B1'), (1, 'B2'), (3, 'B3')]:
                    child_node = child[1]
                    child_cost = child[0] + current_node_cost
                    pq.put((child_cost, child_node))

p1 = Problem()
# print(p1.graph)
p1.ucs()