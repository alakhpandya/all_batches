import pygame
from pygame.locals import *
from queue import PriorityQueue

pygame.init()

WIDTH=500
HEIGHT=500
ROWS = 10
NODE_WIDTH = WIDTH // ROWS

EXPLORED_NODE_COL = (255, 0, 0)     # Red
START_COL = (255, 168, 0)           # Orange
OBSTACLE_COL = (0, 0, 0)            # Black
NODE_COL = (255, 255, 255)          # White
GOAL_COL = (128, 255, 255)          # Aqua
LINE_COL = (128, 128, 128)          # Grey   
PATH_COL = (128, 0, 128)            # Purple


WINDOW=pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Visualizing A-Star Algorithm By _________")


class Node():
    def __init__(self, row, col):
        self.color = NODE_COL
        self.width = NODE_WIDTH
        self.x = col * self.width
        self.y = row * self.width
        self.neighbors = []

    def draw_node(self):
        pygame.draw.rect(WINDOW, self.color, (self.x, self.y, self.width, self.width))
    
    # First type of methods: to "set" a node as start/goal/obstacle etc
    def make_open(self):
        self.color = EXPLORED_NODE_COL

    def make_start_node(self):
        self.color = START_COL

    def make_barrier(self):
        self.color = OBSTACLE_COL

    def clear(self):
        self.color = NODE_COL

    def make_goal_node(self):
        self.color = GOAL_COL

    # def make_grey(self):
    #     self.color = LINE_COL

    def make_path(self):
        self.color = PATH_COL

    # Second type of method: to "test"/"check" if a node is start/goal/obstacle etc
    def is_open(self):
        return self.color == EXPLORED_NODE_COL

    def is_barrier(self):
        return self.color == OBSTACLE_COL

    def is_white(self):
        return self.color == NODE_COL

    def is_goal_node(self):
        return self.color == GOAL_COL

    # def is_grey(self):
    #     return self.color == LINE_COL

    def is_start(self):
        return self.color == START_COL
    
    def generate_neighbors(self, grid):
        # Looking upwards:
        if self.row > 0:
            neighbor = grid[self.row - 1][self.col]
            if not neighbor.is_barrier():
                self.neighbors.append(neighbor)

        # Looking downwards:
        if self.row < ROWS-1:
            neighbor = grid[self.row + 1][self.col]
            if not neighbor.is_barrier():
                self.neighbors.append(neighbor)

        # Looking rightwards:
        if self.col < ROWS-1:
            neighbor = grid[self.row][self.col + 1]
            if not neighbor.is_barrier():
                self.neighbors.append(neighbor)

        # Looking leftwards:
        if self.col > 0:
            neighbor = grid[self.row][self.col - 1]
            if not neighbor.is_barrier():
                self.neighbors.append(neighbor)  

def make_grid(ROWS):
    grid = []
    for row in range(ROWS):     # row: 0,1,2,3, .., 9
        new_row = []
        for col in range(ROWS):     # col: 0,1,2,3, .., 9
            node = Node(row, col)
            new_row.append(node)
        grid.append(new_row)
    return grid

def draw_grid():
    for i in range(ROWS):
        pygame.draw.line(WINDOW, LINE_COL, (0, i * NODE_WIDTH), (WIDTH, i * NODE_WIDTH))
        for j in range(ROWS):
            pygame.draw.line(WINDOW, LINE_COL, ( j * NODE_WIDTH, 0), ( j * NODE_WIDTH, WIDTH))

def draw(grid):
    WINDOW.fill(NODE_COL)
    for row in grid:
        for node in row:
            node.draw_node()
    draw_grid()
    pygame.display.update()

def get_click_pos(pos):
    row = pos[1] // NODE_WIDTH
    col = pos[0] // NODE_WIDTH
    return row, col

def h(start_node, goal_node):
    node_x, node_y = start_node.get_node_position()
    goal_x, goal_y = goal_node.get_node_position()
    heruistic = abs(goal_x - node_x) + abs(goal_y - node_y)
    return heruistic

def find_path(backtrack, end, start):
    node = backtrack[end]
    while node != start:
        node.make_path()
        node = backtrack[node]
        
def a_star_algo(grid, start, end):
    open = PriorityQueue()
    order = 0
    g_value = {}
    f_value = {}
    # setting all nodes f & g values to inf:
    for row in grid:
        for node in row:
            g_value[node] = float("inf")
            f_value[node] = float("inf")

    g_value[start] = 0
    f_value[start] = h(start, end)

    backtrack = {}

    open_simplified = {start}

    open.put((f_value[start], f_value[start], order, start))
    while not open.empty():
        node = open.get()[3]

        if node == end:
            print("Now create shortest path using back tracking")
            node.make_goal_node()
            find_path(backtrack, end, start)
            return True

        for neighbor in node.neighbors:
            temp = g_value[node] + 1

            if temp < g_value[neighbor]:
                g_value[neighbor] = temp
                f_value[neighbor] = g_value[neighbor] + h(neighbor, end)
                backtrack[neighbor] = node

            if neighbor not in open_simplified:
                order += 1
                open_simplified.add(neighbor)
                open.put( (f_value[neighbor], h(neighbor, end), order, neighbor) )
                neighbor.make_open()

        draw(WINDOW, grid, ROWS, WIDTH)

def main():
    grid = make_grid(ROWS)
    # print(grid)

    running = True
    start = None
    goal = None
    algo_started = False

    while running:
        draw(grid)

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

            if algo_started:
                continue

            if pygame.mouse.get_pressed()[0]:        # Left-click
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos)
                node = grid[row][col]

                if not start and node != goal:
                    start = node
                    node.make_start_node()

                if not goal and node != start:
                    goal = node
                    node.make_goal_node()    

                if node != start and node != goal:
                    node.make_barrier()   

            if pygame.mouse.get_pressed()[2]:        # Left-click
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos)
                node = grid[row][col]

                if node == start:
                    start = None

                if node == goal:
                    goal = None

                node.clear()

            if event.type == KEYDOWN and event.key == K_SPACE:
                if start and goal:
                    algo_started = True
                    for row in grid:
                        for node in row:
                            node.generate_neighbors(grid)

                    a_star_algo(grid, start, goal)
                

main()