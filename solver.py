from typing import List

def makeGrid(numOfRows: int, numOfColumns: int) -> List[List[bool]]:
    grid: List[List[bool]] = []
    for _ in range(0, numOfRows):
        grid.append([False] * numOfColumns)
    return grid

def getRowBlocks(row: List[bool]) -> List[int]:
    rowBlocks: List[int] = []
    length: int = 0
    for i in row:
        if i:
            length += 1
        elif length != 0:
            rowBlocks.append(length)
            length = 0
    return rowBlocks

def getColumnBlocks(grid: List[List[bool]], index: int) -> List[int]:
    columnBlocks: List[int] = []
    length: int = 0
    i: bool
    for row in grid:
        i = row[index]
        if i:
            length += 1
        elif length != 0:
            columnBlocks.append(length)
            length = 0
    return columnBlocks

def isSolvable(grid: List[List[bool]], rows: List[List[int]], columns: List[List[int]]) -> bool:
    numOfRows: int = len(rows)
    numOfColumns: int = len(columns)

    # Check each row in the grid
    rowBlock: List[int] = []
    rowCondition: List[int] = []
    for i in range(numOfRows):
        rowBlock = getRowBlocks(grid[i])
        rowCondition = rows[i]
        if len(rowBlock) > len(rowCondition):
            return False
        for j in range(len(rowBlock)):
            if rowBlock[j] > rowCondition[j]:
                return False
    
    # Check each column in the grid
    columnBlock: List[int] = []
    columnCondition: List[int] = []
    for i in range(numOfColumns):
        columnBlock = getColumnBlocks(grid, i)
        columnCondition = columns[i]
        if len(columnBlock) > len(columnCondition):
            return False
        for j in range(len(columnBlock)):
            if columnBlock[j] > columnCondition[j]:
                return False
    
    return True


def solveGrid(rows: List[List[int]], columns: List[List[int]]) -> List[List[bool]]:
    grid: List[List[bool]] = makeGrid(len(rows), len(columns))
    grid[0][0] = True
    grid[1][0] = True
    grid[2][0] = True
    print(isSolvable(grid, rows, columns))
    return grid

if __name__ == '__main__':
    # input for solver
    columns = [
        [2],
        [2, 3],
        [1, 3, 2],
        [2, 2, 1],
        [1, 5, 1],
        [1, 1, 11],
        [1, 5, 1],
        [5, 2],
        [1, 3, 3],
        [2, 3],
    ]

    rows = [
        [1],
        [1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [3, 3],
        [1, 5],
        [7],
        [5],
        [3],
        [2, 3],
        [3, 1, 1],
        [3, 1, 2],
        [2, 3],
        [4],
        [1],
        [1],
    ]
    print(solveGrid(rows, columns))