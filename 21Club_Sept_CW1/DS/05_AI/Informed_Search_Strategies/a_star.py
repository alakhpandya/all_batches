# import area
import pygame
from pygame.locals import *


# Constants/Global Variables
WIDTH = 700     # screen width

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
NODE_DEFAULT_COLOR = (255, 255, 255)
PURPLE = (157, 0, 255)
AQUA = (0, 255, 255)
ORANGE = (255, 165, 0)
GRID_COLOR = (128, 128, 128)

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

    def draw(self, WINDOW):
        pygame.draw.rect(WINDOW, self.color, (self.x, self.y, self.width, self.width))

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

def main(WIDTH, WINDOW):
    ROWS = 7
    grid = make_grid(ROWS, WIDTH)
    
    # Printing grid to check:
    """
    for row in grid:
        for node in row:
            print(node, end=", ")
        print()
    """
    while True:
        draw(WINDOW, grid, ROWS, WIDTH)



# if "__name__" == "__main__":
#     main()

main(WIDTH, WINDOW)