import random
from itertools import product
def board(n):
    grid = []
    for line in open("game_file.txt", "r"):
        row = []
        for cell in line[:-1].split(" "):
            row.append(int(cell))
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
n = 20
command = input("Enter X to view next gen")
while command != "X":
    command = input("Enter X to view next gen:")
    n += 1

output = new_gen(n)
print(board_view(output))








