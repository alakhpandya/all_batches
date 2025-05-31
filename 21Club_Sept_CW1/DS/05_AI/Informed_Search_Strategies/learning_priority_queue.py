from queue import PriorityQueue

# q = PriorityQueue()
# print(q)

# print(q.empty())    # returns True if the queue is empty
# q.put(250)
# q.put(205)
# q.put(75)
# q.put(125)
# q.put(253)

# while not q.empty():
#     x = q.get()
#     print(x)


# q.put((250, "A"))
# q.put((205, "C"))
# q.put((75, "P"))
# q.put((125, "B"))
# q.put((253, "D"))
# while not q.empty():
#     x = q.get()
#     print(x)


# creating "infinite" in Python
"""
a = float("inf")
# print(a)
b = float(input("b = "))
if a > b:
    print(f"{a} > {b}")
else:
    print(f"{a} < {b}")
"""


# Handling "Tie" in priority queue:
q = PriorityQueue()
q.put((250, 300, "A"))
q.put((250, 300, "D"))
q.put((205, 400, "C"))
q.put((205, 350, "D"))
print(q.get())

# l1 = {"a", "b", "c"}
# print("b" in l1)
# print("b" in q)