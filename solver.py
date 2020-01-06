from typing import List

def makeGrid(numOfRows: int, numOfColumns: int) -> List[List[bool]]:
    grid: List[List[bool]] = []
    for _ in range(0, numOfRows):
        grid.append([False] * numOfColumns)
    return grid

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

def isSolvable(grid: List[List[bool]], columns: List[List[int]]) -> bool:
    numOfColumns: int = len(columns)
    
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

def isSolved(grid: List[List[bool]], columns: List[List[int]]) -> bool:
    numOfColumns: int = len(columns)
    
    # Check each column in the grid
    columnBlock: List[int] = []
    columnCondition: List[int] = []
    for i in range(numOfColumns):
        columnBlock = getColumnBlocks(grid, i)
        columnCondition = columns[i]
        if len(columnBlock) != len(columnCondition):
            return False
        for j in range(len(columnBlock)):
            if columnBlock[j] != columnCondition[j]:
                return False
    
    return True

def getRowStartingIndex(row: List[bool]):
    for i in range(0, len(row)):
        if row[i]:
            if i + 1 >= len(row):
                return -1
            else:
                return i + 1
    return 0

def getRemainingBlockLength(rowBlocks: List[int]):
    length: int = 0
    for i in rowBlocks:
        length += i + 1
    return length

def solveGrid(
    rowsToAdd: List[List[int]],
    numberOfRows: int,
    columnConditions: List[List[int]],
    currentGrid: List[List[bool]]=None) -> List[List[bool]]:
    # Make a new grid at the start of call chain
    if currentGrid == None:
        currentGrid = makeGrid(len(rowsToAdd), len(columnConditions))

    if isSolved(currentGrid, columnConditions):
        print(currentGrid)
        return currentGrid
    
    blockLength: int = rowsToAdd[0].pop(0)
    if len(rowsToAdd[0]) == 0:
        rowsToAdd.pop(0)
    if len(rowsToAdd) == 0:
        return
    otherBlocksLength: int = getRemainingBlockLength(rowsToAdd[0])
    currentRowIndex: int = numberOfRows - len(rowsToAdd)
    firstFreeIndex: int = getRowStartingIndex(currentGrid[currentRowIndex])

    gridCopy: List[List[bool]]
    for i in range(firstFreeIndex, len(currentGrid[currentRowIndex]) - otherBlocksLength - blockLength):
        gridCopy = [row[:] for row in currentGrid]
        for j in range(0, blockLength):
            gridCopy[currentRowIndex][i + j] = True
        if isSolvable(gridCopy, columnConditions):
            solveGrid(rowsToAdd, numberOfRows, columnConditions, currentGrid=gridCopy)

    return [1]

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
    print(solveGrid(rows, len(rows), columns))