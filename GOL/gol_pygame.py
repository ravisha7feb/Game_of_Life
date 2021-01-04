import random
from itertools import product
import pygame
from time import sleep

def board(n):
    grid = []
    for line in open("game_file.txt", "r"):
        row = [int(cell) for cell in line[:-1].split() if cell != '']
        grid.append(row)
    return grid
#print(board(10))
def neighbours(block, n):
    for c in product(*(range(i - 1, i + 2) for i in block)):
        if c != block and all(0 <= j < n for j in c):
            yield c

    
def rule1(n, block):
    live_count = 0
    for (i, j) in list(neighbours(block, n)):
        if board(n)[i][j] == 1:
            live_count += 1
    return True if live_count in {2, 3} else False


def rule2(n, block):
    live_count = 0
    for i, j in list(neighbours(block, n)):
        if board(n)[i][j] == 1:
            live_count += 1
    return True if live_count == 3 else False


def new_gen(n):
    updated_board = []
    for i in range(n):
        updated_board.append([])
    if n > 20:
        grid = new_gen(n-1)
    else:
        grid = board(n)
    for row_num in range(len(grid)):
        for col_num in range(len(grid)):
            if len(list(neighbours((row_num,col_num), n))) == 8:

                if board(n)[row_num][col_num] == 1:
                    if rule1(n, (row_num, col_num)):
                        updated_board[row_num].append(1)
                    else:
                        updated_board[row_num].append(0)
                if board(n)[row_num][col_num] == 0:
                    if rule2(n, (row_num, col_num)):
                        updated_board[row_num].append(1)
                    else:
                        updated_board[row_num].append(0)

    return updated_board

def board_view(grid):
    for i in grid:
        for j in i:
            print(j, end= " ")
        print()

#print(board_view(board(10)))
#print(board_view(new_gen(10)))
#continue = "Y" stop = "X" if user enters X we display output
"""
n = 20
command = input("Enter X to view next gen")
while command != "X":
    command = input("Enter X to view next gen:")
    n += 1

output = new_gen(n)
print(board_view(output))
"""
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

def game_display(rows, cols):
    grid = board(rows)
    user_choice = ''
    while user_choice != 'x':
        
        color = random.choice(COLORS)
        for x in range(rows):
            for y in range(cols):
                cell = grid[x][y]
                cell_color = color if cell == 1 else WHITE
                draw_square(x, y, cell_color)

        grid = new_gen(rows + 1)
        pygame.display.flip()

        sleep(0.5)
        user_choice = input("Press x to quit and any other key to move towards the next generation: ")
        

game_display(20, 20)




