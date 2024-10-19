import pygame
from pygame.locals import *
import sys
from queue import PriorityQueue

pygame.init()
WIDTH = 700
window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('A Star by silver oak students')

RED = (255, 0, 0)
ORANGE = (255, 168, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
AQUA = (128, 255, 255)
GREY = (128, 128, 128)
PURPLE = (128, 0, 128)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows
        self.neighbors = []

    # Type A methods: Coloring a node
    def make_start_node(self):
        self.color = ORANGE

    def make_goal_node(self):
        self.color = AQUA

    def make_barrier(self):
        self.color = BLACK

    def make_open(self):
        self.color = RED

    def make_path(self):
        self.color = PURPLE

    def clear(self):
        self.color = WHITE

    def make_grey(self):
        self.color = GREY
    
    # Type B Method: Testing a node for its color:
    def chekc_start_node(self):     
        return self.color == ORANGE

    def is_goal_node(self):
        return self.color == AQUA

    def is_barrier(self):
        return self.color == BLACK

    def is_open(self):
        return self.color == RED

    def is_path(self):
        return self.color == PURPLE

    def is_clear(self):
        return self.color == WHITE

    def is_grey(self):
        return self.color == GREY

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def get_node_position(self):
        return self.row, self.col

    def generate_neighbors(self, grid):
        # look up:
        if self.row > 0:
            node = grid[self.row - 1][self.col]
            if not node.is_barrier():
                self.neighbors.append(node)
    
        # look down:
        if self.row < self.total_rows - 1:
            node = grid[self.row + 1][self.col]
            if not node.is_barrier():
                self.neighbors.append(node)
    
        # look left:
        if self.col > 0:
            node = grid[self.row][self.col - 1]
            if not node.is_barrier():
                self.neighbors.append(node)
    
        # look right:
        if self.col < self.total_rows - 1:
            node = grid[self.row][self.col + 1]
            if not node.is_barrier():
                self.neighbors.append(node)

def make_grid(rows, width):
    grid = []
    node_width = width // rows
    for i in range(rows):
        temp = []
        for j in range(rows):
            node = Node(i, j, node_width, rows)
            temp.append(node)
        grid.append(temp)
    return grid

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
    for j in range(rows):
        pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))


def draw(window, grid, rows, width):
    window.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(window)
    draw_grid(window, rows, width)
    pygame.display.update()

def get_click_position(pos, rows, width):
    node_width = width // rows
    x, y = pos
    row = y // node_width
    col = x // node_width
    return row, col

def h(node_position, goal_position):
    x1, y1 = node_position
    x2, y2 = goal_position
    h_score = abs(x1 - x2) + abs(y1 - y2)
    return h_score

def create_path(window, grid, rows, width, backtrack, current):
    while current in backtrack:
        current.make_path()
        current = backtrack[current]
        draw(window, grid, rows, width)

def astar_algo(window, ROWS, width, grid, start, end):
    open = PriorityQueue()
    order = 0

    backtrack = {}
    g_values = {}
    f_values = {}
    for row in grid:
        for node in row:
            g_values[node] = float("inf")
            f_values[node] = float("inf")
    g_values[start] = 0
    h_start = h(start.get_node_position(), end.get_node_position())
    f_values[start] = h_start + g_values[start]
    open.put((f_values[start], h_start, order, start))
    open_simplified = {start}
    while not open.empty():
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()

        node = open.get()[3]

        if node == end:
            create_path(window, grid, ROWS, width, backtrack, end)
            node.make_goal_node()
            return True
        
        for neighbor in node.neighbors:
            g_values_temp = g_values[node] + 1
            
            if g_values_temp < g_values[neighbor]:
                g_values[neighbor] = g_values_temp
                h_value = h(neighbor.get_node_position(), end.get_node_position())
                f_values[neighbor] = g_values[neighbor] + h_value
                backtrack[neighbor] = node

            if neighbor not in open_simplified:
                open_simplified.add(neighbor)
                order += 1
                open.put((f_values[neighbor], h_value, order, neighbor))
                neighbor.make_open()

        draw(window, grid, ROWS, width)
    return False

def main(window, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    started = False
    while True:
        draw(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()

            if started == True:
                continue

            if pygame.mouse.get_pressed()[0]:    # left click
                pos = pygame.mouse.get_pos()
                row, col = get_click_position(pos, ROWS, width)
                node = grid[row][col]
                if not start:
                    start = node
                    node.make_start_node()

                elif start and not end:
                    end = node
                    node.make_goal_node()

                elif node != start and node != end:
                    node.make_barrier()

            if pygame.mouse.get_pressed()[2]:   # right click
                pos = pygame.mouse.get_pos()
                row, col = get_click_position(pos, ROWS, width)
                node = grid[row][col]
                node.clear()
                if node == start:
                    start = None
                if node == end:
                    end = None

            if event.type == KEYDOWN:
                if event.key == K_SPACE and start and end:
                    started = True
                    for row in grid:
                        for node in row:
                            node.generate_neighbors(grid)
                    
                    astar_algo(window, ROWS, width, grid, start, end)

    pygame.quit()

main(window, WIDTH)