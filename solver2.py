from typing import List

class MyGrid():

    def __init__(self, remainingRows: List[List[int]], columnConditions: List[List[int]], grid: List[List[bool]]):
        self.grid = grid
        self.remainingRows = remainingRows
        self.currentRow = 0
        self.columnConditions = columnConditions
    
    #TODO: implement this
    def columnsSolved(self) -> bool:
        pass
    
    #TODO: implement this
    def placeNextBlock(self, positionInRow: int):
        
        pass

    #TODO: implement this
    def isSafePlacement(self, positionInRow: int):
        # Check if placement overfills collumn
        pass
    
    #TODO: implement this
    def rowIndexes(self) -> range:
        pass
    
    #TODO: implement this
    def copy(self) -> MyGrid:
        pass

def isSolvable(myGrid: MyGrid) -> bool:
    if len(myGrid.remainingRows) <= 0:
        if myGrid.columnsSolved():
            print(myGrid.grid)
            return True
        else:
            return False
    
    gridCopy: MyGrid = myGrid.copy()
    validIndexes: range = gridCopy.rowIndexes()
    for index in validIndexes:
        if gridCopy.isSafePlacement(index):
            gridCopy.placeNextBlock(index)
            if isSolvable(gridCopy):
                return True
        
    return False




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