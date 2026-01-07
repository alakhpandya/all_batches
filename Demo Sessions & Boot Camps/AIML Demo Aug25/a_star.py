import pygame
from pygame.locals import *
from queue import PriorityQueue

EXPLORED_NODE_COL = (255, 0, 0)
START_COL = (255, 168, 0)
OBSTACLE_COL = (0, 0, 0)        # black
NODE_COL = (255, 255, 255)      # white
GOAL_COL = (128, 255, 255)
LINE_COL = (128, 128, 128)
PATH_COL = (128, 0, 128)

WIDTH = 700
ROWS = 25

# initializing pygame & creating window
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A-Star Algorithm Visualization")

class Node():
    def __init__(self, row, col, node_width):
        self.row = row
        self.col = col
        self.color = NODE_COL
        self.width = node_width
        self.x = col * self.width
        self.y = row * self.width
        self.neighbors = []

    def draw(self, WINDOW):
        pygame.draw.rect(WINDOW, self.color, (self.x, self.y, self.width, self.width))

    # Type A: Changing colors of the node   def make_obstacle: self.color = OBSTACLE_COL
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

    def make_grey(self):
        self.color = LINE_COL

    def make_path(self):
        self.color = PATH_COL


    # Type B: Checking color of the node    def is_black: return self.color == black
    def is_open(self):
        return self.color == EXPLORED_NODE_COL

    def is_barrier(self):
        return self.color == OBSTACLE_COL

    def is_white(self):
        return self.color == NODE_COL

    def is_goal_node(self):
        return self.color == GOAL_COL

    def is_grey(self):
        return self.color == LINE_COL

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

    def get_node_position(self):
        return self.row, self.col
    

def make_grid(ROWS, WIDTH):
    grid = []
    node_width = WIDTH/ROWS
    for i in range(ROWS):
        row = []
        for j in range(ROWS):
            node = Node(i, j, node_width)
            row.append(node)
        grid.append(row)
    return grid

def draw_grid(WINDOW, ROWS, WIDTH):
    gap = WIDTH // ROWS
    for i in range(ROWS):
        pygame.draw.line(WINDOW, LINE_COL, (0, i * gap), (WIDTH, i * gap))
        for j in range(ROWS):
            pygame.draw.line(WINDOW, LINE_COL, ( j * gap, 0), ( j * gap, WIDTH))


def draw(WINDOW, grid, ROWS, WIDTH):
    WINDOW.fill(NODE_COL)
    for row in grid:
        for node in row:
            node.draw(WINDOW)
    draw_grid(WINDOW, ROWS, WIDTH)
    pygame.display.update()

def get_click_position(pos, ROWS, WIDTH):
    node_width = WIDTH // ROWS
    x, y = pos
    row = y // node_width
    col = x // node_width
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

def astar(grid, start, end):
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


def main(WINDOW):
    grid = make_grid(ROWS, WIDTH)
    
    start = None
    end = None
    algo_started = False
    running = True

    while running:
        draw(WINDOW, grid, ROWS, WIDTH)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            
            if algo_started:
                continue

            if pygame.mouse.get_pressed()[0]:           # left click happened
                pos = pygame.mouse.get_pos()
                row, col = get_click_position(pos, ROWS, WIDTH)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    node.make_start_node()

                if not end and node != start:
                    end = node
                    node.make_goal_node()

                if node != start and node != end:
                    node.make_barrier()
            if pygame.mouse.get_pressed()[2]:           # right click happened
                pos = pygame.mouse.get_pos()
                row, col = get_click_position(pos, ROWS, WIDTH)
                node = grid[row][col]
                if node == start:
                    start = None
                if node == end:
                    end = None
                node.clear()
            
            if event.type == KEYDOWN and event.key == K_SPACE:
                algo_started = True
                if start and end:
                    for row in grid:
                        for node in row:
                            node.generate_neighbors(grid)
                    astar(grid, start, end)

main(WINDOW)