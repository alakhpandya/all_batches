# import area
from a_star import algo
import pygame
from pygame.locals import *
from sys import exit
from queue import PriorityQueue


# Constants/Global Variables
WIDTH = 700     # screen width

START_NODE = (255, 165, 0)
GOAL_NODE = (0, 255, 0)
OBSTACLE_NODE = (0, 0, 0)
OPEN_NODE = (255, 0, 0)
PATH_NODE = (0, 255, 255)

NODE_DEFAULT_COLOR = (255, 255, 255)
GRID_COLOR = (128, 128, 128)
PURPLE = (157, 0, 255)
BLUE = (0, 0, 255)

WINDOW = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("A-star Algorithm")


# Classes:
class Node():
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.color = NODE_DEFAULT_COLOR
        self.x = row*self.width
        self.y = col*self.width
        self.neighbors = []

    def draw(self, WINDOW):
        pygame.draw.rect(WINDOW, self.color, (self.x, self.y, self.width, self.width))

    # Methods to color a node:
    def make_start(self):
        self.color = START_NODE

    def make_goal(self):
        self.color = GOAL_NODE

    def make_obstacle(self):
        self.color = OBSTACLE_NODE

    def make_open(self):
        self.color = OPEN_NODE

    def make_path(self):
        self.color = PATH_NODE

    def make_clear(self):
        self.color = NODE_DEFAULT_COLOR

    # Methods to CHECK the color of a node:
    def is_start(self):
        return self.color == START_NODE
    
    def is_goal(self):
        return self.color == GOAL_NODE
    
    def is_obstacle(self):
        return self.color == OBSTACLE_NODE
    
    def is_open(self):
        return self.color == OPEN_NODE
    
    def is_path(self):
        return self.color == PATH_NODE
    
    def is_clear(self):
        return self.color == NODE_DEFAULT_COLOR

    def get_position(self):
        return self.row, self.col
    
    # Generating neighbors of a node
    def generate_neighbors(self, grid):
        """
        grid = [
            [a0, a1, a2],
            [b0, b1, b2],
            [c0, c1, c2]
        ]
        total = len(grid) = 3
        """
        total = len(grid)
        # top
        if self.row > 0:
            n = grid[self.row - 1][self.col]
            if not n.is_obstacle():
                self.neighbors.append(n)

        # bottom
        if self.row < total-1:
            n = grid[self.row + 1][self.col]
            if not n.is_obstacle():
                self.neighbors.append(n)

        # left
        if self.col > 0:
            n = grid[self.row][self.col - 1]
            if not n.is_obstacle():
                self.neighbors.append(n)


        # right
        if self.col < total-1:
            n = grid[self.row][self.col + 1]
            if not n.is_obstacle():
                self.neighbors.append(n)
    
# Function Area
def make_grid(ROWS, WIDTH):
    grid = []
    node_width = WIDTH / ROWS
    for i in range(ROWS):
        temp = []
        for j in range(ROWS):
            node = Node(i, j, node_width)
            temp.append(node)
        grid.append(temp)
    return grid

def draw_grid(WINDOW, ROWS, WIDTH):
    gap = WIDTH/ROWS
    for i in range(ROWS):
        pygame.draw.line(WINDOW, GRID_COLOR, (i*gap, 0), (i*gap, WIDTH))
        for j in range(ROWS):
            pygame.draw.line(WINDOW, GRID_COLOR, (0, j*gap), (WIDTH, j*gap))

def draw(WINDOW, grid, ROWS, WIDTH):
    # WINDOW.fill()
    for row in grid:
        for node in row:
            node.draw(WINDOW)
    draw_grid(WINDOW, ROWS, WIDTH)
    pygame.display.update()

def get_click_pos(pos, ROWS, WIDTH):
    x, y = pos
    gap = WIDTH/ROWS
    row = int(x // gap)
    col = int(y // gap)
    return row, col

def h(current_node, end):
    node_x, node_y = current_node.get_position()
    goal_x, goal_y = end.get_position()
    return abs(goal_x - node_x) + abs(goal_y - node_y)

def a_star(grid, start, end):
    open = PriorityQueue()

    g_value = {}
    f_value = {}
    for row in grid:
        for node in row:
            g_value[node] = float("inf")
            f_value[node] = float("inf")
    g_value[start] = 0
    f_value[start] = h(start, end)

    open.put((f_value[start], start))

    while not open.empty():
        node = open.get()[1]

        if node == end:
            # Backtrack the path
            return True

def main(WIDTH, WINDOW):
    ROWS = 7
    grid = make_grid(ROWS, WIDTH)
    
    start = False
    goal = False
    # Printing grid to check:
    """
    for row in grid:
        for node in row:
            print(node, end=", ")
        print()
    """
    while True:
        draw(WINDOW, grid, ROWS, WIDTH)

        for event in pygame.event.get():
            # print(event)
            # print(event.type)
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()

            if pygame.mouse.get_pressed()[0]:     # detecting left click
                pos = pygame.mouse.get_pos()

                row, col = get_click_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                if start and goal and node != start and node != goal:
                    node.make_obstacle()
                
                if start and not goal:
                    node.make_goal()
                    goal = node
                
                if not start:
                    node.make_start()
                    start = node

            if pygame.mouse.get_pressed()[2]:     # detecting right click
                pos = pygame.mouse.get_pos()

                row, col = get_click_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                node.make_clear()
                if node == start:
                    start = False
                if node == goal:
                    goal = False

            if event.type == KEYDOWN and event.key == K_RETURN and start and goal:
                for row in grid:
                    for node in row:
                        node.generate_neighbors(grid)
                # print(grid[0][0].neighbors)
                # algo()

# if "__name__" == "__main__":
#     main()

main(WIDTH, WINDOW)