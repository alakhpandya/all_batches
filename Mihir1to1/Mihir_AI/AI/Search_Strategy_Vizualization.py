from AI_search_strategies import A_star as algorithm
from AI_search_strategies import dfs as algorithm
from AI_search_strategies import bfs as algorithm

# ----------------- Import Section -----------------
import pygame
from pygame.locals import *
from queue import PriorityQueue


# ----------------- Global Constants/Variables Section -----------------
pygame.init()
WIDTH = 700
ROWS = int(input("Rows: "))

WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Visualization")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 168, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
AQUA = (128, 255, 255)
GREY = (128, 128, 128)
PURPLE = (128, 0, 128)


# ----------------- Classes & Function Section -----------------
class Node():
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.color = WHITE
        self.neighbors = []
        self.x = col * width
        self.y = row * width
        # self.f = float("inf")
        # self.g = float("inf")

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def get_position(self):
        return self.row, self.col
    
    # ----------------- Make Methods -----------------
    def make_red(self):
        self.color = RED
        
    def make_open(self):
        self.color = GREEN

    def make_blue(self):
        self.color = BLUE

    def make_start(self):
        self.color = ORANGE

    def make_yellow(self):
        self.color = YELLOW

    def make_obstacle(self):
        self.color = BLACK

    def reset(self):
        self.color = WHITE

    def make_end(self):
        self.color = AQUA

    def make_grey(self):
        self.color = GREY

    def make_path(self):
        self.color = PURPLE

    # ----------------- Check Methods -----------------
    def is_red(self):
        return self.color == RED
        
    def is_open(self):
        return self.color == GREEN

    def is_blue(self):
        return self.color == BLUE

    def is_start(self):
        return self.color == ORANGE

    def is_yellow(self):
        return self.color == YELLOW

    def is_obstacle(self):
        return self.color == BLACK

    def is_white(self):
        return self.color == WHITE

    def is_end(self):
        return self.color == AQUA

    def is_grey(self):
        return self.color == GREY

    def is_path(self):
        return self.color == PURPLE

    def generate_neighbors(self, grid):
        # look up, down, right & left make neighbor if not obstacle
        # look up:
        if self.row > 0:
            node = grid[self.row - 1][self.col]
            if not node.is_obstacle():
                self.neighbors.append(node)

        # look down:
        if self.row < self.total_rows - 1:
            node = grid[self.row + 1][self.col]
            if not node.is_obstacle():
                self.neighbors.append(node)

        # look left:
        if self.col > 0:
            node = grid[self.row][self.col - 1]
            if not node.is_obstacle():
                self.neighbors.append(node)

        # look right:
        if self.col < self.total_rows - 1:
            node = grid[self.row][self.col + 1]
            if not node.is_obstacle():
                self.neighbors.append(node)

def make_grid(rows, width):
    node_width = width // rows
    grid = []
    for i in range(rows):
        temp = []
        for j in range(rows):
            node = Node(i, j, node_width, rows)
            temp.append(node)
        grid.append(temp)
    return grid

def draw_grid(window, grid, width, rows):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (gap * i, 0), (gap * i, width))
        for j in range(rows):
            pygame.draw.line(window, GREY, (0, gap*j), (width, gap*j))

def draw(window, grid, rows, width):
    window.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(window)
    draw_grid(window, grid, width, rows)
    pygame.display.update()

def get_clicked_node(x, y, rows, width):
    node_width = width // rows
    row = y // node_width
    col = x // node_width
    return row, col


def h(current_node, goal_node):
    x, y = goal_node.get_position()
    x1, y1 = current_node.get_position()
    return abs(x - x1) + abs(y - y1)


def create_path(backtrack, end, window, grid, rows, width):
    node = end
    while node in backtrack:
        node = backtrack[node]
        node.make_path()
        draw(window, grid, rows, width)

# def algorithm(window, grid, width, rows, start, end):
#     open = PriorityQueue()
#     order = 1
#     h_start = h(start, end)
#     open.put((h_start, h_start, order, start))
#     f_values = {}
#     g_values = {}
#     backtrack = {}
#     simplified_queue = {start}
#     for row in grid:
#         for node in row:
#             f_values[node] = float("inf")
#             g_values[node] = float("inf")

#     f_values[start] = h_start
#     g_values[start] = 0

#     while not open.empty():

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()

#         node = open.get()[3]

        
#         for current in node.neighbors:
#             # print("for started")
#             temp_g = g_values[node] + 1

#             if node == end:
#                 create_path(backtrack, end, window, grid, rows, width)
#                 start.make_start()
#                 return True


#             if temp_g < g_values[current]:
#                 g_values[current] = temp_g
#                 h_value = h(current, end)
#                 f_values[current] = g_values[current] + h_value
#                 backtrack[current] = node

#                 if current not in simplified_queue:
#                     order += 1
#                     open.put((f_values[current], h_value, order, current))
#                     simplified_queue.add(current)
#                     node.make_open()

#         draw(window, grid, rows, width)


def main(width, window, ROWS):
    grid = make_grid(ROWS, width)

    start = None
    end = None

    running = True
    started = False

    while running:
        draw(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                row, col = get_clicked_node(x, y, ROWS, width)
                node = grid[row][col]

                if not start and node != end:
                    node.make_start()
                    start = node

                elif node != start and not end:
                    node.make_end()
                    end = node

                elif node != start and node != end:
                    node.make_obstacle()

            if pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                row, col = get_clicked_node(x, y, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                if node == end:
                    end = None

            if event.type == KEYDOWN:
                if event.key == K_SPACE and not started:
                    # generate neighbors
                    for row in grid:
                        for node in row:
                            node.generate_neighbors(grid)

                    algorithm(window, grid, width, ROWS, start, end)
                
                if event.key == K_ESCAPE:
                    grid = make_grid(ROWS, width)

                    start = None
                    end = None

                    running = True
                    started = False
 

    pygame.quit()


main(WIDTH, WINDOW, ROWS)