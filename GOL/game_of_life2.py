#this was for finite board, also has a bug so ignore
import random
from itertools import product
def board(n):
    row = []
    for i in range(n):
        col = []
        for j in range(n):
            col.append(random.randint(0, 1))
        row.append(col)

    for i in row:
        for j in i:
            print(j, end=" ")
        print()
    return row

print(board(5))
size = 5


def neighbours(block, n):
    for c in product(*(range(i - 1, i + 2) for i in block)):
        if c != block and all(0 <= j < n for j in c):
            yield c


print(list(neighbours((2, 2), 5)))
grocery = [["a", "b", "c"], ["f", "g", "h"], ["i", "j", "k"]]


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
    for row_num in range(len(board(n))):
        for col_num in range(len(board(n)[row_num])):
            if board(n)[row_num][col_num] == 1:
                if rule1(n, (row_num, col_num)):
                    updated_board[row_num][col_num] = 1
                else:
                    updated_board[row_num][col_num] = 0
            if board(n)[row_num][col_num] == 0:
                if rule2(n, (row_num, col_num)):
                    updated_board[row_num][col_num] = 1
                else:
                    updated_board[row_num][col_num] = 0
            else:
                updated_board[row_num][col_num] = 0

    return updated_board


print(rule1(5, (2, 2)))
print(rule2(5, (1, 2)))
print(new_gen(5))









