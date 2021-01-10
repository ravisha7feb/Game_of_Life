import random
from itertools import product
import pygame
from time import sleep

def board():
    grid = []
    for line in open("game_file.txt", "r"):
        row = [int(cell) for cell in line.split() if cell != '']
        grid.append(row)
    return grid
#print(board(10))
def neighbours(block, n):
    neighbr_cells = [c for c in ((product(*(range(i - 1, i + 2) for i in block)))) if c != block and all(0 <= j < n for j in c)]
    return neighbr_cells

def rule1(n, block, grid):
    live_count = 0
    for i, j in neighbours(block, n):
        if grid[i][j] == 1:
            live_count += 1
    return (live_count in {2, 3})

def rule2(n, block, grid):
    live_count = 0
    for i, j in neighbours(block, n):
        if grid[i][j] == 1:
            live_count += 1
    return (live_count == 3)

def new_gen(grid):
    n = len(grid[0])
    updated_board = []
    for row_num in range(n):
        row = []
        for col_num in range(n):

                if grid[row_num][col_num] == 1:
                    if rule1(n, (row_num, col_num), grid):
                        row.append(1)
                        
                    else:
                        row.append(0)
                        
                if grid[row_num][col_num] == 0:
                    if rule2(n, (row_num, col_num), grid):
                        row.append(1)
                        
                    else:
                        row.append(0)
                       
        updated_board.append(row)
    return updated_board

def board_view(grid):
    for i in grid:
        for j in i:
            print(j, end= " ")
        print()

#pygame code:

GREEN = (0, 153, 0)
PINK = (255, 0, 127)
BLUE = (102, 0, 0)
YELLOW = (204, 204, 0)
WHITE = (255, 255, 255)

COLORS = [GREEN, PINK, BLUE, YELLOW]
pygame.init()
height = 700
width = 700
screen = pygame.display.set_mode((width, height))
size = 30
screen.fill(WHITE)
ALIVE = ['*', '#', '$'] #if colors can't show up
def draw_square(x, y, color):
    left, top = x * size, y * size
    if color != WHITE:
        pygame.draw.rect(screen, WHITE, (top - 1, left - 1, size, size), 1)

    pygame.draw.rect(screen, color, (top, left, size, size))

def game_display(rows):
    this_gen = board()
    user_choice = ''
    #while user_choice != 'x':
    while True:
        #color = random.choice(COLORS)
        for x in range(rows):
            for y in range(rows - 1):
                color = random.choice(COLORS)
                cell = this_gen[x][y]
                cell_color = color if cell == 1 else WHITE
                draw_square(x, y, cell_color)
        
        
        this_gen = new_gen(this_gen)
        pygame.display.flip()
        sleep(0.5)
        #user_choice = input("Press x to quit and any other key to move towards the next generation: ") 
        
game_display(30)
