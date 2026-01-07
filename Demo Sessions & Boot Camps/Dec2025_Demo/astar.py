import pygame
from pygame.locals import *
from queue import PriorityQueue

WIDTH = 700
ROWS = 10
NODE_WIDTH = WIDTH // ROWS

NODE_COL = (255, 255, 255)
OBSTACLE_COL = (0, 0, 0)
START_COL = (255, 155, 0)
GOAL_COL = (0, 255, 255)
EXPLORED_NODE_COL = (255, 0, 0)
PATH_COL = (255, 0, 255)
LINE_COL = (128, 128, 128)


pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A-star Visualization By Alakh Pandya")

class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = NODE_COL
        self.x = NODE_WIDTH * self.col
        self.y = NODE_WIDTH * self.row
        self.neighbors = []

    def draw_node(self, WINDOW):
        pygame.draw.rect(WINDOW, self.color, (self.x, self.y, NODE_WIDTH, NODE_WIDTH))

    # Methods to set the color of a node:
    def make_start(self):
        self.color = START_COL

    def make_goal(self):
        self.color = GOAL_COL

    def make_obstacle(self):
        self.color = OBSTACLE_COL

    def make_explored(self):
        self.color = EXPLORED_NODE_COL

    def make_path(self):
        self.color = PATH_COL

    def clear(self):
        self.color = NODE_COL

    def check_obstacle(self):
        return self.color == OBSTACLE_COL
    
    def generate_neighbors(self, grid):
        # look up
        if self.row > 0:
            neighbor = grid[self.row - 1][self.col]
            if not neighbor.check_obstacle():
                self.neighbors.append(neighbor)

        # look down
        if self.row < len(grid)-1:
            neighbor = grid[self.row + 1][self.col]
            if not neighbor.check_obstacle():
                self.neighbors.append(neighbor)

        # look left
        if self.col > 0:
            neighbor = grid[self.row][self.col - 1]
            if not neighbor.check_obstacle():
                self.neighbors.append(neighbor)

        # look right
        if self.col < len(grid)-1:
            neighbor = grid[self.row][self.col + 1]
            if not neighbor.check_obstacle():
                self.neighbors.append(neighbor)

def make_grid(ROWS):
    grid = []
    for j in range(ROWS):
        node_list = []
        for i in range(ROWS):  # i = 0, 1, 2
            new_node = Node(j, i)
            node_list.append(new_node)
        grid.append(node_list)
    return grid

def draw_grid(WINDOW, grid, ROWS):
    for i in range(ROWS):       # i = 0,1,2,3
        pygame.draw.line(WINDOW, LINE_COL, (0, i*NODE_WIDTH), (WIDTH, i*NODE_WIDTH))
        pygame.draw.line(WINDOW, LINE_COL, (i*NODE_WIDTH, 0), (i*NODE_WIDTH, WIDTH))

def draw(WINDOW, grid, ROWS):
    WINDOW.fill(NODE_COL)
    
    for row in grid:
        for node in row:
            node.draw_node(WINDOW)
    
    draw_grid(WINDOW, grid, ROWS)
    pygame.display.update()
    
def get_click_pos(coord, NODE_WIDTH):
    x, y = coord
    col = x // NODE_WIDTH
    row = y // NODE_WIDTH
    return row, col

def h(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def find_path(backtrack, start, goal):
    node = backtrack[goal]
    while node != start:
        node.make_path()
        node = backtrack[node]

def astar_algo(grid, start, goal):
    open = PriorityQueue()

    order = 0
    f_value = {}
    g_value = {}

    for row in grid:
        for node in row:
            f_value[node] = float("inf")
            g_value[node] = float("inf")
        
    g_value[start] = 0
    f_value[start] = h(start, goal)

    backtrack = {}

    open_simplified = {start}
    open.put((f_value[start], h(start, goal), order, start))
    while not open.empty():
        node = open.get()[3]

        if node == goal:
            # print("Reached goal")
            find_path(backtrack, start, goal)
            node.make_goal()
            return True

        for neighbor in node.neighbors:
            temp = g_value[node] + 1

            if temp < g_value[neighbor]:
                g_value[neighbor] = temp
                f_value[neighbor] = g_value[neighbor] + h(neighbor, goal)
                backtrack[neighbor] = node

            if neighbor not in open_simplified:
                order += 1
                open.put((f_value[neighbor], h(neighbor, goal), order, neighbor))
                open_simplified.add(neighbor)
                neighbor.make_explored()

        draw(WINDOW, grid, ROWS)
    return False

def main():
    grid = make_grid(ROWS)

    running = True
    start = None
    goal = None
    while running:
        draw(WINDOW, grid, ROWS)

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

            if pygame.mouse.get_pressed()[0]:
                click_coord = pygame.mouse.get_pos()
                row, col = get_click_pos(click_coord, NODE_WIDTH)
                node = grid[row][col]
                if not start and node != goal:
                    node.make_start()
                    start = node

                if not goal and node != start:
                    node.make_goal()
                    goal = node

                if node != start and node != goal:
                    node.make_obstacle()

            if pygame.mouse.get_pressed()[2]:
                click_coord = pygame.mouse.get_pos()
                row, col = get_click_pos(click_coord, NODE_WIDTH)
                node = grid[row][col]
                if node == start:
                    start = None

                if node == goal:
                    goal = None

                node.clear()

            if event.type == KEYDOWN and event.key == K_SPACE:
                if start and goal:
                    for row in grid:
                        for node in row:
                            node.generate_neighbors(grid)
                    print(astar_algo(grid, start, goal))
main()