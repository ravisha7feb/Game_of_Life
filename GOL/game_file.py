import random
def board(n):
    grid = []    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0,1))
        grid.append(row)
    for i in grid:
        for j in i:
            print(j, end = " ")
        print()

    return grid

board(30)
