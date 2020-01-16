from typing import List

class MyGrid():

    def __init__(self, remainingRows: List[List[int]], columnConditions: List[List[int]], grid: List[List[bool]]=None):
        # Initialise a new grid if one is not given
        if grid == None:
            self.grid = []
            for _ in range(0, len(remainingRows)):
                self.grid.append([False] * len(columnConditions))
        else:
            self.grid = grid

        self.remainingRows = remainingRows
        self.currentRowIndex = 0
        self.columnConditions = columnConditions
    
    def getColumnBlocks(self, index: int) -> List[int]:
        columnBlocks: List[int] = []
        length: int = 0
        i: bool
        for row in self.grid:
            i = row[index]
            if i:
                length += 1
            elif length != 0:
                columnBlocks.append(length)
                length = 0
        # Add final columnBlock
        if length != 0:
            columnBlocks.append(length)
        return columnBlocks

    def columnsSolved(self) -> bool:
        # Check each column in the grid
        columnBlock: List[int] = []
        columnCondition: int = []
        for i in range(len(self.columnConditions)):
            columnBlock = self.getColumnBlocks(i)
            columnCondition = self.columnConditions[i]
            if len(columnBlock) != len(columnCondition):
                return False
            for j in range(len(columnBlock)):
                if columnBlock[j] != columnCondition[j]:
                    return False
        
        return True
    
    def placeNextBlock(self, positionInRow: int):
        blockLength = self.remainingRows[0].pop(0)
        currentRow = self.grid[self.currentRowIndex]
        if self.remainingRows[0] == []:
            self.currentRowIndex += 1
            self.remainingRows.pop(0)
        for i in range(positionInRow, positionInRow + blockLength):
            currentRow[i] = True

    def isSafePlacement(self, positionInRow: int):
        myGridCopy = self.copy()
        myGridCopy.placeNextBlock(positionInRow)

        # Check if placement overfills collumn
        columnBlock: List[int] = []
        columnCondition: int = []
        for i in range(len(myGridCopy.columnConditions)):
            columnBlock = myGridCopy.getColumnBlocks(i)
            columnCondition = myGridCopy.columnConditions[i]
            if len(columnBlock) > len(columnCondition):
                return False
            for j in range(len(columnBlock)):
                if columnBlock[j] > columnCondition[j]:
                    return False
        
        return True

    
    def validRowIndexes(self) -> range:
        currentRow = self.grid[self.currentRowIndex]
        startingIndex: int = -1
        for i in range(len(currentRow), -1, -1):
            if i == 0:
                startingIndex = 0
            if currentRow[i - 1]:
                startingIndex = i + 1
                break
        
        endIndex: int = -1
        rowsLeftover = self.remainingRows[0][1:]
        endIndex = len(self.grid[0]) - sum(rowsLeftover) - len(rowsLeftover) - self.remainingRows[0][0] + 1
        return range(startingIndex, endIndex)

    def copy(self):
        gridCopy = []
        for row in self.grid:
            gridCopy.append(row[:])
        
        remainingRowsCopy = []
        for condition in self.remainingRows:
            remainingRowsCopy.append(condition[:])
        
        columnConditionCopy = []
        for condition in self.columnConditions:
            columnConditionCopy.append(condition[:])

        myGridCopy = MyGrid(remainingRowsCopy, columnConditionCopy, gridCopy)
        myGridCopy.currentRowIndex = self.currentRowIndex
        return myGridCopy

def isSolvable(myGrid: MyGrid) -> bool:
    if len(myGrid.remainingRows) <= 0:
        if myGrid.columnsSolved():
            return True
        else:
            return False
    
    gridCopy: MyGrid = myGrid.copy()
    validIndexes: range = gridCopy.validRowIndexes()
    for index in validIndexes:
        if gridCopy.isSafePlacement(index):
            gridCopy.placeNextBlock(index)
            if isSolvable(gridCopy):
                return True
        
    return False




if __name__ == '__main__':
    # columns = [
    #     [1],
    #     [1],
    #     [1]
    # ]

    # rows = [
    #     [1, 1],
    #     [1]
    # ]
    # myGrid = MyGrid(rows, columns)
    # isSolvable(myGrid)

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
    myGrid = MyGrid(rows, columns)
    isSolvable(myGrid)