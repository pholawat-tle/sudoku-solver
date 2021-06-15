grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def cloneGrid(grid):
    newList = []
    for row in grid:
        newList.append(row[:])

    return newList


def cloneRow(row):
    newRow = []
    for member in row:
        newRow.append(member)

    return newRow


def rotateGrid(grid):
    rotatedGrid = []

    for i in range(9):
        rotatedGrid.append([])
        for j in range(9):
            rotatedGrid[i].append(grid[j][i])

    return rotatedGrid


def extrackSmallGrid(grid):
    smallGrids = []
    for i in range(3):
        for j in range(3):
            smallGrid = []
            smallGrid.append(grid[i*3][j*3])
            smallGrid.append(grid[i*3][j*3+1])
            smallGrid.append(grid[i*3][j*3+2])
            smallGrid.append(grid[i*3+1][j*3])
            smallGrid.append(grid[i*3+1][j*3+1])
            smallGrid.append(grid[i*3+1][j*3+2])
            smallGrid.append(grid[i*3+2][j*3])
            smallGrid.append(grid[i*3+2][j*3+1])
            smallGrid.append(grid[i*3+2][j*3+2])
            smallGrids.append(smallGrid)
    return smallGrids


def checkRowsLegal(grid):
    gridClone = cloneGrid(grid)

    answer = True
    for row in gridClone:
        rowAnswer = checkRowLegal(row)
        answer = answer and rowAnswer
        if answer == False:
            break
    return answer


def checkRowLegal(row):
    temp = []
    rowClone = cloneRow(row)
    for _ in row:
        child = rowClone.pop()
        if child != 0:
            if child not in temp:
                temp.append(child)
            else:
                return False
    return True


def checkSmallGridLegal(grid):
    # [0,0][0,1][0,2] [0,3] [0,4] [0,5]
    # [1,0][1,1][1,2] [1,3] [1,4] [1,5]
    # [2,0][2,1][2,2] [2,3] [2,4] [2,5]
    return checkRowsLegal(extrackSmallGrid(grid))


def checkColumnsLegal(grid):
    return checkRowsLegal(rotateGrid(grid))


def checkGridLegal(grid):
    smallGrids = checkSmallGridLegal(grid)
    rows = checkRowsLegal(grid)
    columns = checkColumnsLegal(grid)
    return smallGrids and rows and columns


def checkCompleteGrid(grid):
    if(not checkGridLegal(grid)):
        return False
    for row in grid:
        if 0 in row:
            return False

    return True


def possible(grid, x, y, n):
    gridClone = cloneGrid(grid)
    gridClone[y][x] = n
    return checkGridLegal(gridClone)


def prettyGrid(grid):
    for row in grid:
        print(row)
    print()


def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid, x, y, n):
                        grid[y][x] = n
                        if solve(grid):
                            return True
                        else:
                            grid[y][x] = 0
                return False

    return True


solve(grid)
prettyGrid(grid)
